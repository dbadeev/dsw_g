"""Клиент детектора галлюцинаций: OpenAI-совместимый вызов vLLM.

Поддерживает два режима:
- enable_thinking=False (по умолчанию): модель сразу генерирует один бинарный
  токен ('0'/'1'), max_tokens мал (по умолчанию 2). Вероятность считается
  через softmax по логитам '1' и '0' первого подходящего токена.
- enable_thinking=True: max_tokens увеличен (max_tokens_thinking), поиск
  классификационного токена — с конца сгенерированной последовательности.

Обработка ошибок: BadRequestError (400) — это ПОСТОЯННАЯ ошибка клиента
(например, превышен max_model_len для конкретного длинного примера).
Повторные попытки её не исправят, поэтому она НЕ ретраится — сразу
возвращается None, а вызывающий код (evaluate.py) считает такой пример
неудачным (n_unparsed_none), но не прерывает весь прогон. Ретраятся только
временные ошибки (сеть, 5xx, таймауты).
"""
from __future__ import annotations

import math
import time
from typing import Optional

from openai import OpenAI, BadRequestError


def _score_from_top(top: list) -> Optional[float]:
    """top: list[(token, logprob)] -> P('1') через softmax по '1'/'0'."""
    def best(ch: str):
        vals = [lp for t, lp in top if t.strip() == ch]
        return max(vals) if vals else None

    l1, l0 = best("1"), best("0")
    if l1 is None and l0 is None:
        return None
    if l0 is None:
        return 1.0
    if l1 is None:
        return 0.0
    m = max(l1, l0)
    e1, e0 = math.exp(l1 - m), math.exp(l0 - m)
    return e1 / (e1 + e0)


class DetectorClient:
    def __init__(
        self,
        model: str,
        system_prompt: str,
        base_url: str,
        api_key: str = "EMPTY",
        top_logprobs: int = 20,
        retries: int = 4,
        enable_thinking: bool = False,
        max_tokens_default: int = 2,
        max_tokens_thinking: int = 1024,
        request_timeout: float = 120.0,
    ):
        self.model = model
        self.system_prompt = system_prompt
        self.top_logprobs = top_logprobs
        self.retries = retries
        self.enable_thinking = enable_thinking
        self.max_tokens_default = max_tokens_default
        self.max_tokens_thinking = max_tokens_thinking
        self._client = OpenAI(base_url=base_url, api_key=api_key, timeout=request_timeout)
        self._extra = {"chat_template_kwargs": {"enable_thinking": enable_thinking}}

    def score(self, text: str, max_tokens: Optional[int] = None) -> Optional[float]:
        """Вероятность галлюцинации для одного примера, или None если:
        - ответ не распарсился (нет '0'/'1' в логпробах);
        - пример перманентно отбракован API (400, например переполнение контекста)."""
        mt = max_tokens if max_tokens is not None else (
            self.max_tokens_thinking if self.enable_thinking else self.max_tokens_default
        )
        msgs = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": text},
        ]
        last = None
        for attempt in range(self.retries):
            try:
                r = self._client.chat.completions.create(
                    model=self.model,
                    messages=msgs,
                    temperature=0.0,
                    max_tokens=mt,
                    logprobs=True,
                    top_logprobs=self.top_logprobs,
                    extra_body=self._extra,
                )
            except BadRequestError:
                # Постоянная ошибка клиента (например, превышен context length
                # для этого конкретного примера) — ретраить бессмысленно.
                return None
            except Exception as e:  # noqa: BLE001 — ретраим сетевые/серверные ошибки
                last = e
                time.sleep(min(2 ** attempt, 30))
                continue

            lp = r.choices[0].logprobs
            if not lp or not lp.content:
                return None

            if self.enable_thinking:
                for tok in reversed(lp.content):
                    if tok.token.strip() in ("0", "1"):
                        return _score_from_top(
                            [(t.token, t.logprob) for t in tok.top_logprobs]
                        )
                return None
            else:
                for tok in lp.content:
                    if tok.token.strip() in ("0", "1"):
                        return _score_from_top(
                            [(t.token, t.logprob) for t in tok.top_logprobs]
                        )
                return _score_from_top(
                    [(t.token, t.logprob) for t in lp.content[0].top_logprobs]
                )

        raise RuntimeError(f"API failed after {self.retries} retries: {last}") from last
