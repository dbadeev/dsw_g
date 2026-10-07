"""
26_diagnostic_before_third_guess.py — ПЕРЕД третьей попыткой угадать причину
добавляем прямую диагностику: печатаем РЕАЛЬНЫЕ top-5 токенов и их logprob
для нескольких строк. Это единственный способ узнать точно, что модель
физически генерирует первым токеном, вместо очередной гипотезы, которая
может снова не сработать и потратить ещё один холодный старт (~7-9 минут).

Заодно фикс логической ошибки: fallback-значение при "токен не найден"
больше не 0.5 (что при threshold=0.5 всегда резолвится в label=1 из-за
строгого >=), а None с явной пометкой ошибки — как и для реальных
исключений API. Такая строка получит тот же обрабатываемый путь, что и
context-length ошибки, а не тихо исказит метрику.

Замените _score_one в 13_modal_app_multi_model.py на версию ниже.
"""
import math


def _normalize_token(token: str) -> str:
    return token.strip().lstrip("\u2581\u0120")


async def _score_one(client, semaphore, system_prompt: str, user_prompt: str,
                      disable_thinking: bool, debug_label: str | None = None) -> tuple[float, str | None]:
    async with semaphore:
        try:
            kwargs = {}
            if disable_thinking:
                kwargs["extra_body"] = {"chat_template_kwargs": {"enable_thinking": False}}
            completion = await client.chat.completions.create(
                model="judge",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                max_tokens=1,
                temperature=0.0,
                logprobs=True,
                top_logprobs=20,
                **kwargs,
            )
        except Exception as e:  # noqa: BLE001
            return 1.0, f"{type(e).__name__}: {e}"

        top = completion.choices[0].logprobs.content[0].top_logprobs

        # === ДИАГНОСТИКА: печатаем реальные топ-5 токенов для первых N строк ===
        if debug_label is not None:
            import sys
            top5 = sorted(top, key=lambda t: -t.logprob)[:5]
            print(f"[DEBUG {debug_label}] top-5 токенов: "
                  f"{[(repr(t.token), round(t.logprob, 2)) for t in top5]}", file=sys.stderr)

        logprob_1 = next((t.logprob for t in top if _normalize_token(t.token) == "1"), None)
        logprob_0 = next((t.logprob for t in top if _normalize_token(t.token) == "0"), None)

        if logprob_1 is None and logprob_0 is None:
            # Ни "1", ни "0" вообще не встретились в top-20 -- это не 50/50
            # неопределённость, а ПОЛНЫЙ провал формата ответа модели.
            # Возвращаем score=None-эквивалент через отдельный маркер ошибки,
            # а не молчаливый fallback 0.5 (который при threshold=0.5 через
            # >= ВСЕГДА резолвится в label=1 -- это и есть источник бага).
            return 1.0, "no_digit_token_in_top20"

        logprob_1 = logprob_1 if logprob_1 is not None else -100.0
        logprob_0 = logprob_0 if logprob_0 is not None else -100.0
        e1, e0 = math.exp(logprob_1), math.exp(logprob_0)
        score = e1 / (e1 + e0) if (e1 + e0) > 0 else 0.5
        return score, None


"""
Использование для диагностики (добавить в _score_batch/run_predict):

    tasks = [
        _score_one(client, semaphore, sp, up, cfg["needs_disable_thinking"],
                   debug_label=task_id if i < 3 else None)  # первые 3 строки -- с debug
        for i, (task_id, sp, up) in enumerate(row_data)
    ]

После запуска в логе будет видно РЕАЛЬНЫЙ первый токен, который генерирует
saiga8b/yandexgpt5lite -- например, если там что-то вроде
[('Ответ', -0.1), (':', -0.3), (' ', -1.2), ...] -- это прямое доказательство,
что модель игнорирует инструкцию "верни один символ" и генерирует обычный
ответ, а не служебный токен.

ВАЖНО: даже с этой правкой n_llm_errors теперь ПОКАЖЕТ реальное число строк
с provalom формата (сейчас они маскировались под "успешные" score=0.5).
Ожидаемо: этот показатель окажется БЛИЗОК к 37 (то есть почти весь llm-only
объём) -- если гипотеза верна, метрики P/R для этих двух моделей в текущем
виде промпта не имеют смысла, и single-token judge-подход, работающий для
Qwen, может быть просто НЕСОВМЕСТИМ с этими конкретными instruct-моделями
без дополнительного prompt-engineering или few-shot примеров.
"""
