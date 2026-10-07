# Отчёт о структуре данных


## Обзор

Всего файлов: 5898

## downloaded_domains_data/banking_knowledge/secondary_source/README.md

Размер: 11.4 КБ
Тип: текст, 11637 символов, 182 строк
- head: `samples/downloaded_domains_data__banking_knowledge__secondary_source__README.md.txt`

## downloaded_domains_data/banking_knowledge/secondary_source/db.json

Размер: 1440.7 КБ
Тип: JSON dict (len=2)
Схема:
```
$: dict
$.active_customer: NoneType
$.customers: dict
$.customers.{*}: 197 keys | dict
$.customers.{*}.profile: dict
$.customers.{*}.profile.name: str
$.customers.{*}.profile.age: int
$.customers.{*}.profile.gender: str
$.customers.{*}.profile.senior_citizen: bool
$.customers.{*}.profile.segment: str
$.customers.{*}.profile.profession: str
$.customers.{*}.profile.sector: str
$.customers.{*}.profile.employer: str
$.customers.{*}.profile.marital_status: str
$.customers.{*}.profile.monthly_income: int
$.customers.{*}.profile.kyc_status: str
$.customers.{*}.profile.email: str
$.customers.{*}.profile.phone: str
$.customers.{*}.profile.communication_address: dict
$.customers.{*}.profile.communication_address.line1: str
$.customers.{*}.profile.communication_address.line2: str
$.customers.{*}.profile.communication_address.city: str
$.customers.{*}.profile.communication_address.state: str
$.customers.{*}.profile.communication_address.pincode: str
$.customers.{*}.profile.permanent_address: dict
$.customers.{*}.profile.permanent_address.line1: str
$.customers.{*}.profile.permanent_address.line2: str
$.customers.{*}.profile.permanent_address.city: str
$.customers.{*}.profile.permanent_address.state: str
$.customers.{*}.profile.permanent_address.pincode: str
$.customers.{*}.login_context: dict
$.customers.{*}.login_context.customer_id: str
$.customers.{*}.login_context.linked_accounts: len~1 | len~2 | list
$.customers.{*}.login_context.linked_accounts[]: str
$.customers.{*}.login_context.linked_products: len~3 | len~5 | list
$.customers.{*}.login_context.linked_products[]: str
$.customers.{*}.login_context.linked_cards: len~1 | len~2 | list
$.customers.{*}.login_context.linked_cards[]: str
$.customers.{*}.accounts: dict
$.customers.{*}.accounts.SB5438989427: dict
$.customers.{*}.accounts.SB5438989427.account_id: str
$.customers.{*}.accounts.SB5438989427.account_type: str
$.customers.{*}.accounts.SB5438989427.status: str
$.customers.{*}.accounts.SB5438989427.ifsc: str
$.customers.{*}.accounts.SB5438989427.home_branch: str
$.customers.{*}.accounts.SB5438989427.holders: len~2 | list
$.customers.{*}.accounts.SB5438989427.holders[]: str
$.customers.{*}.accounts.SB5438989427.nominee: dict
$.customers.{*}.accounts.SB5438989427.nominee.name: str
$.customers.{*}.accounts.SB5438989427.nominee.relationship: str
$.customers.{*}.accounts.SB5438989427.open_date: str
$.customers.{*}.accounts.SB5438989427.available_balance: float
$.customers.{*}.accounts.SB5438989427.hold_amount: float
$.customers.{*}.accounts.SB5438989427.currency: str
$.customers.{*}.accounts.SB5438989427.transactions: len~6 | list
$.customers.{*}.accounts.SB5438989427.transactions[]: dict
$.customers.{*}.accounts.SB5438989427.transactions[].reference_id: str
$.customers.{*}.accounts.SB5438989427.transactions[].date: str
$.customers.{*}.accounts.SB5438989427.transactions[].description: str
$.customers.{*}.accounts.SB5438989427.transactions[].amount: float
$.customers.{*}.accounts.SB5438989427.transactions[].direction: str
$.customers.{*}.accounts.SB5438989427.transactions[].channel: str
$.customers.{*}.accounts.SB5438989427.transactions[].balance_after: float
$.customers.{*}.accounts.SB5438989427.cheques: len~2 | list
$.customers.{*}.accounts.SB5438989427.cheques[]: dict
$.customers.{*}.accounts.SB5438989427.cheques[].cheque_number: str
$.customers.{*}.accounts.SB5438989427.cheques[].status: str
$.customers.{*}.accounts.CA2434606277: dict
$.customers.{*}.accounts.CA2434606277.account_id: str
$.customers.{*}.accounts.CA2434606277.account_type: str
$.customers.{*}.accounts.CA2434606277.status: str
$.customers.{*}.accounts.CA2434606277.ifsc: str
$.customers.{*}.accounts.CA2434606277.home_branch: str
$.customers.{*}.accounts.CA2434606277.holders: len~2 | list
$.customers.{*}.accounts.CA2434606277.holders[]: str
$.customers.{*}.accounts.CA2434606277.nominee: NoneType
$.customers.{*}.accounts.CA2434606277.open_date: str
$.customers.{*}.accounts.CA2434606277.available_balance: float
$.customers.{*}.accounts.CA2434606277.hold_amount: float
$.customers.{*}.accounts.CA2434606277.currency: str
$.customers.{*}.accounts.CA2434606277.transactions: len~4 | list
$.customers.{*}.accounts.CA2434606277.transactions[]: dict
$.customers.{*}.accounts.CA2434606277.transactions[].reference_id: str
$.customers.{*}.accounts.CA2434606277.transactions[].date: str
$.customers.{*}.accounts.CA2434606277.transactions[].description: str
$.customers.{*}.accounts.CA2434606277.transactions[].amount: float
$.customers.{*}.accounts.CA2434606277.transactions[].direction: str
$.customers.{*}.accounts.CA2434606277.transactions[].channel: str
$.customers.{*}.accounts.CA2434606277.transactions[].balance_after: float
$.customers.{*}.accounts.CA2434606277.cheques: len~0 | list
$.customers.{*}.deposits: dict
$.customers.{*}.deposits.RD959328: dict
$.customers.{*}.deposits.RD959328.deposit_id: str
$.customers.{*}.deposits.RD959328.kind: str
$.customers.{*}.deposits.RD959328.monthly_installment: float
$.customers.{*}.deposits.RD959328.rate: float
$.customers.{*}.deposits.RD959328.tenure_months: int
$.customers.{*}.deposits.RD959328.installments_paid: int
$.customers.{*}.deposits.RD959328.total_deposited: float
$.customers.{*}.deposits.RD959328.start_date: str
$.customers.{*}.deposits.RD959328.maturity_date: str
$.customers.{*}.deposits.RD959328.maturity_amount: float
$.customers.{*}.deposits.RD959328.maturity_instruction: str
$.customers.{*}.deposits.RD959328.status: str
$.customers.{*}.deposits.RD959328.source_account: str
$.customers.{*}.deposits.RD959328.payout_account: str
$.customers.{*}.deposits.RD959328.nominee: dict
$.customers.{*}.deposits.RD959328.nominee.name: str
$.customers.{*}.deposits.RD959328.nominee.relationship: str
$.customers.{*}.deposits.RD902990: dict
$.customers.{*}.deposits.RD902990.deposit_id: str
$.customers.{*}.deposits.RD902990.kind: str
$.customers.{*}.deposits.RD902990.monthly_installment: float
$.customers.{*}.deposits.RD902990.rate: float
$.customers.{*}.deposits.RD902990.tenure_months: int
$.customers.{*}.deposits.RD902990.installments_paid: int
$.customers.{*}.deposits.RD902990.total_deposited: float
$.customers.{*}.deposits.RD902990.start_date: str
$.customers.{*}.deposits.RD902990.maturity_date: str
$.customers.{*}.deposits.RD902990.maturity_amount: float
$.customers.{*}.deposits.RD902990.maturity_instruction: str
$.customers.{*}.deposits.RD902990.status: str
$.customers.{*}.deposits.RD902990.source_account: str
$.customers.{*}.deposits.RD902990.payout_account: str
$.customers.{*}.deposits.RD902990.nominee: dict
$.customers.{*}.deposits.RD902990.nominee.name: str
$.customers.{*}.deposits.RD902990.nominee.relationship: str
$.customers.{*}.loans: dict
$.customers.{*}.cards: dict
$.customers.{*}.cards.CARD10433: dict
$.customers.{*}.cards.CARD10433.card_id: str
$.customers.{*}.cards.CARD10433.card_type: str
$.customers.{*}.cards.CARD10433.network: str
$.customers.{*}.cards.CARD10433.status: str
$.customers.{*}.cards.CARD10433.credit_limit: int
$.customers.{*}.cards.CARD10433.available_limit: int
$.customers.{*}.cards.CARD10433.linked_account: str
$.customers.{*}.cards.CARD10433.controls: dict
$.customers.{*}.cards.CARD10433.controls.atm: dict
$.customers.{*}.cards.CARD10433.controls.atm.domestic: dict
$.customers.{*}.cards.CARD10433.controls.atm.domestic.enabled: bool
$.customers.{*}.cards.CARD10433.controls.atm.domestic.daily_limit: int
$.customers.{*}.cards.CARD10433.controls.atm.international: dict
$.customers.{*}.cards.CARD10433.controls.atm.international.enabled: bool
$.customers.{*}.cards.CARD10433.controls.online: dict
$.customers.{*}.cards.CARD10433.controls.online.domestic: dict
$.customers.{*}.cards.CARD10433.controls.online.domestic.enabled: bool
$.customers.{*}.cards.CARD10433.controls.online.domestic.daily_limit: int
$.customers.{*}.cards.CARD10433.controls.online.international: dict
$.customers.{*}.cards.CARD10433.controls.online.international.enabled: bool
$.customers.{*}.cards.CARD10433.controls.pos: dict
$.customers.{*}.cards.CARD10433.controls.pos.domestic: dict
$.customers.{*}.cards.CARD10433.controls.pos.domestic.enabled: bool
$.customers.{*}.cards.CARD10433.controls.pos.domestic.daily_limit: int
$.customers.{*}.cards.CARD10433.controls.pos.international: dict
$.customers.{*}.cards.CARD10433.controls.pos.international.enabled: bool
$.customers.{*}.cards.CARD10433.controls.pos.international.daily_limit: int
$.customers.{*}.mandates: len~1 | len~2 | list
$.customers.{*}.mandates[]: dict
$.customers.{*}.mandates[].mandate_id: str
$.customers.{*}.mandates[].account_id: str
$.customers.{*}.mandates[].payee: str
$.customers.{*}.mandates[].amount: int
$.customers.{*}.mandates[].frequency: str
$.customers.{*}.mandates[].next_debit_date: str
$.customers.{*}.mandates[].status: str
$.customers.{*}.mandates[].type: str
$.customers.{*}.insurance: dict
$.customers.{*}.insurance.POL936843: dict
$.customers.{*}.insurance.POL936843.policy_id: str
$.customers.{*}.insurance.POL936843.policy_name: str
$.customers.{*}.insurance.POL936843.insurer: str
$.customers.{*}.insurance.POL936843.sum_assured: float
$.customers.{*}.insurance.POL936843.premium: float
$.customers.{*}.insurance.POL936843.frequency: str
$.customers.{*}.insurance.POL936843.status: str
$.customers.{*}.insurance.POL936843.next_premium_date: str
$.customers.{*}.insurance.POL936843.nominee: dict
$.customers.{*}.insurance.POL936843.nominee.name: str
$.customers.{*}.insurance.POL936843.nominee.relationship: str
$.customers.{*}.requests: dict
$.customers.{*}.requests.SR-83363930: dict
$.customers.{*}.requests.SR-83363930.request_id: str
$.customers.{*}.requests.SR-83363930.category: str
$.customers.{*}.requests.SR-83363930.description: str
$.customers.{*}.requests.SR-83363930.related_transaction_id: NoneType
$.customers.{*}.requests.SR-83363930.account_id: str
$.customers.{*}.requests.SR-83363930.status: str
$.customers.{*}.requests.SR-83363930.priority: str
$.customers.{*}.requests.SR-83363930.created_at: str
$.customers.{*}.requests.SR-83363930.eta: str
$.customers.{*}.offers: len~2 | list
$.customers.{*}.offers[]: dict
$.customers.{*}.offers[].offer_id: str
$.customers.{*}.offers[].type: str
$.customers.{*}.offers[].title: str
$.customers.{*}.offers[].detail: str
$.customers.{*}.offers[].indicative: bool
$.customers.{*}.accounts.SB8054014323: dict
$.customers.{*}.accounts.SB8054014323.account_id: str
$.customers.{*}.accounts.SB8054014323.account_type: str
$.customers.{*}.accounts.SB8054014323.status: str
$.customers.{*}.accounts.SB8054014323.ifsc: str
$.customers.{*}.accounts.SB8054014323.home_branch: str
$.customers.{*}.accounts.SB8054014323.holders: len~1 | list
$.customers.{*}.accounts.SB8054014323.holders[]: str
$.customers.{*}.accounts.SB8054014323.nominee: dict
$.customers.{*}.accounts.SB8054014323.nominee.name: str
$.customers.{*}.accounts.SB8054014323.nominee.relationship: str
$.customers.{*}.accounts.SB8054014323.open_date: str
$.customers.{*}.accounts.SB8054014323.available_balance: float
$.customers.{*}.accounts.SB8054014323.hold_amount: float
$.customers.{*}.accounts.SB8054014323.currency: str
$.customers.{*}.accounts.SB8054014323.transactions: len~7 | list
$.customers.{*}.accounts.SB8054014323.transactions[]: dict
$.customers.{*}.accounts.SB8054014323.transactions[].reference_id: str
$.customers.{*}.accounts.SB8054014323.transactions[].date: str
$.customers.{*}.accounts.SB8054014323.transactions[].description: str
$.customers.{*}.accounts.SB8054014323.transactions[].amount: float
$.customers.{*}.accounts.SB8054014323.transactions[].direction: str
$.customers.{*}.accounts.SB8054014323.transactions[].channel: str
$.customers.{*}.accounts.SB8054014323.transactions[].balance_after: float
$.customers.{*}.accounts.SB8054014323.cheques: len~0 | list
$.customers.{*}.deposits.RD130260: dict
$.customers.{*}.deposits.RD130260.deposit_id: str
$.customers.{*}.deposits.RD130260.kind: str
$.customers.{*}.deposits.RD130260.monthly_installment: float
$.customers.{*}.deposits.RD130260.rate: float
$.customers.{*}.deposits.RD130260.tenure_months: int
$.customers.{*}.deposits.RD130260.installments_paid: int
$.customers.{*}.deposits.RD130260.total_deposited: float
$.customers.{*}.deposits.RD130260.start_date: str
$.customers.{*}.deposits.RD130260.maturity_date: str
$.customers.{*}.deposits.RD130260.maturity_amount: float
$.customers.{*}.deposits.RD130260.maturity_instruction: str
$.customers.{*}.deposits.RD130260.status: str
$.customers.{*}.deposits.RD130260.source_account: str
$.customers.{*}.deposits.RD130260.payout_account: str
$.customers.{*}.deposits.RD130260.nominee: dict
$.customers.{*}.deposits.RD130260.nominee.name: str
$.customers.{*}.deposits.RD130260.nominee.relationship: str
$.customers.{*}.deposits.RD541262: dict
$.customers.{*}.deposits.RD541262.deposit_id: str
$.customers.{*}.deposits.RD541262.kind: str
$.customers.{*}.deposits.RD541262.monthly_installment: float
$.customers.{*}.deposits.RD541262.rate: float
$.customers.{*}.deposits.RD541262.tenure_months: int
$.customers.{*}.deposits.RD541262.installments_paid: int
$.customers.{*}.deposits.RD541262.total_deposited: float
$.customers.{*}.deposits.RD541262.start_date: str
$.customers.{*}.deposits.RD541262.maturity_date: str
$.customers.{*}.deposits.RD541262.maturity_amount: float
$.customers.{*}.deposits.RD541262.maturity_instruction: str
$.customers.{*}.deposits.RD541262.status: str
$.customers.{*}.deposits.RD541262.source_account: str
$.customers.{*}.deposits.RD541262.payout_account: str
$.customers.{*}.deposits.RD541262.nominee: dict
$.customers.{*}.deposits.RD541262.nominee.name: str
$.customers.{*}.deposits.RD541262.nominee.relationship: str
$.customers.{*}.loans.LN41343: dict
$.customers.{*}.loans.LN41343.loan_id: str
$.customers.{*}.loans.LN41343.loan_type: str
$.customers.{*}.loans.LN41343.outstanding: float
$.customers.{*}.loans.LN41343.rate: float
$.customers.{*}.loans.LN41343.emi: float
$.customers.{*}.loans.LN41343.remaining_tenure_months: int
$.customers.{*}.loans.LN41343.next_due_date: str
$.customers.{*}.loans.LN41343.status: str
$.customers.{*}.cards.CARD81377: dict
$.customers.{*}.cards.CARD81377.card_id: str
$.customers.{*}.cards.CARD81377.card_type: str
$.customers.{*}.cards.CARD81377.network: str
$.customers.{*}.cards.CARD81377.status: str
$.customers.{*}.cards.CARD81377.credit_limit: int
$.customers.{*}.cards.CARD81377.available_limit: int
$.customers.{*}.cards.CARD81377.linked_account: str
$.customers.{*}.cards.CARD81377.controls: dict
$.customers.{*}.cards.CARD81377.controls.atm: dict
$.customers.{*}.cards.CARD81377.controls.atm.domestic: dict
$.customers.{*}.cards.CARD81377.controls.atm.domestic.enabled: bool
$.customers.{*}.cards.CARD81377.controls.atm.domestic.daily_limit: int
$.customers.{*}.cards.CARD81377.controls.atm.international: dict
$.customers.{*}.cards.CARD81377.controls.atm.international.enabled: bool
$.customers.{*}.cards.CARD81377.controls.atm.international.daily_limit: int
$.customers.{*}.cards.CARD81377.controls.online: dict
$.customers.{*}.cards.CARD81377.controls.online.domestic: dict
$.customers.{*}.cards.CARD81377.controls.online.domestic.enabled: bool
$.customers.{*}.cards.CARD81377.controls.online.domestic.daily_limit: int
$.customers.{*}.cards.CARD81377.controls.online.international: dict
$.customers.{*}.cards.CARD81377.controls.online.international.enabled: bool
$.customers.{*}.cards.CARD81377.controls.online.international.daily_limit: int
$.customers.{*}.cards.CARD81377.controls.pos: dict
$.customers.{*}.cards.CARD81377.controls.pos.domestic: dict
$.customers.{*}.cards.CARD81377.controls.pos.domestic.enabled: bool
$.customers.{*}.cards.CARD81377.controls.pos.domestic.daily_limit: int
$.customers.{*}.cards.CARD81377.controls.pos.international: dict
$.customers.{*}.cards.CARD81377.controls.pos.international.enabled: bool
$.customers.{*}.requests.SR-93601033: dict
$.customers.{*}.requests.SR-93601033.request_id: str
$.customers.{*}.requests.SR-93601033.category: str
$.customers.{*}.requests.SR-93601033.description: str
$.customers.{*}.requests.SR-93601033.related_transaction_id: NoneType
$.customers.{*}.requests.SR-93601033.account_id: str
$.customers.{*}.requests.SR-93601033.status: str
$.customers.{*}.requests.SR-93601033.priority: str
$.customers.{*}.requests.SR-93601033.created_at: str
$.customers.{*}.requests.SR-93601033.eta: str
$.customers.{*}.accounts.SB2246923283: dict
$.customers.{*}.accounts.SB2246923283.account_id: str
$.customers.{*}.accounts.SB2246923283.account_type: str
$.customers.{*}.accounts.SB2246923283.status: str
$.customers.{*}.accounts.SB2246923283.ifsc: str
$.customers.{*}.accounts.SB2246923283.home_branch: str
$.customers.{*}.accounts.SB2246923283.holders: len~1 | list
$.customers.{*}.accounts.SB2246923283.holders[]: str
$.customers.{*}.accounts.SB2246923283.nominee: dict
$.customers.{*}.accounts.SB2246923283.nominee.name: str
$.customers.{*}.accounts.SB2246923283.nominee.relationship: str
$.customers.{*}.accounts.SB2246923283.open_date: str
$.customers.{*}.accounts.SB2246923283.available_balance: float
$.customers.{*}.accounts.SB2246923283.hold_amount: float
$.customers.{*}.accounts.SB2246923283.currency: str
$.customers.{*}.accounts.SB2246923283.transactions: len~6 | list
$.customers.{*}.accounts.SB2246923283.transactions[]: dict
$.customers.{*}.accounts.SB2246923283.transactions[].reference_id: str
$.customers.{*}.accounts.SB2246923283.transactions[].date: str
$.customers.{*}.accounts.SB2246923283.transactions[].description: str
$.customers.{*}.accounts.SB2246923283.transactions[].amount: float
$.customers.{*}.accounts.SB2246923283.transactions[].direction: str
$.customers.{*}.accounts.SB2246923283.transactions[].channel: str
$.customers.{*}.accounts.SB2246923283.transactions[].balance_after: float
$.customers.{*}.accounts.SB2246923283.cheques: len~0 | list
$.customers.{*}.accounts.CA4178158747: dict
$.customers.{*}.accounts.CA4178158747.account_id: str
$.customers.{*}.accounts.CA4178158747.account_type: str
$.customers.{*}.accounts.CA4178158747.status: str
$.customers.{*}.accounts.CA4178158747.ifsc: str
$.customers.{*}.accounts.CA4178158747.home_branch: str
$.customers.{*}.accounts.CA4178158747.holders: len~1 | list
$.customers.{*}.accounts.CA4178158747.holders[]: str
$.customers.{*}.accounts.CA4178158747.nominee: NoneType
$.customers.{*}.accounts.CA4178158747.open_date: str
$.customers.{*}.accounts.CA4178158747.available_balance: float
$.customers.{*}.accounts.CA4178158747.hold_amount: float
$.customers.{*}.accounts.CA4178158747.currency: str
$.customers.{*}.accounts.CA4178158747.transactions: len~6 | list
$.customers.{*}.accounts.CA4178158747.transactions[]: dict
$.customers.{*}.accounts.CA4178158747.transactions[].reference_id: str
$.customers.{*}.accounts.CA4178158747.transactions[].date: str
$.customers.{*}.accounts.CA4178158747.transactions[].description: str
$.customers.{*}.accounts.CA4178158747.transactions[].amount: float
$.customers.{*}.accounts.CA4178158747.transactions[].direction: str
$.customers.{*}.accounts.CA4178158747.transactions[].channel: str
$.customers.{*}.accounts.CA4178158747.transactions[].balance_after: float
$.customers.{*}.accounts.CA4178158747.cheques: len~0 | list
$.customers.{*}.deposits.FD963953: dict
$.customers.{*}.deposits.FD963953.deposit_id: str
$.customers.{*}.deposits.FD963953.kind: str
$.customers.{*}.deposits.FD963953.principal: float
$.customers.{*}.deposits.FD963953.rate: float
$.customers.{*}.deposits.FD963953.tenure_months: int
$.customers.{*}.deposits.FD963953.start_date: str
$.customers.{*}.deposits.FD963953.maturity_date: str
$.customers.{*}.deposits.FD963953.maturity_amount: float
$.customers.{*}.deposits.FD963953.payout_type: str
$.customers.{*}.deposits.FD963953.maturity_instruction: str
$.customers.{*}.deposits.FD963953.status: str
$.customers.{*}.deposits.FD963953.payout_account: str
$.customers.{*}.deposits.FD963953.nominee: dict
$.customers.{*}.deposits.FD963953.nominee.name: str
$.customers.{*}.deposits.FD963953.nominee.relationship: str
$.customers.{*}.deposits.FD621974: dict
$.customers.{*}.deposits.FD621974.deposit_id: str
$.customers.{*}.deposits.FD621974.kind: str
$.customers.{*}.deposits.FD621974.principal: float
$.customers.{*}.deposits.FD621974.rate: float
$.customers.{*}.deposits.FD621974.tenure_months: int
$.customers.{*}.deposits.FD621974.start_date: str
$.customers.{*}.deposits.FD621974.maturity_date: str
$.customers.{*}.deposits.FD621974.maturity_amount: float
$.customers.{*}.deposits.FD621974.payout_type: str
$.customers.{*}.deposits.FD621974.maturity_instruction: str
$.customers.{*}.deposits.FD621974.status: str
$.customers.{*}.deposits.FD621974.payout_account: str
$.customers.{*}.deposits.FD621974.nominee: dict
$.customers.{*}.deposits.FD621974.nominee.name: str
$.customers.{*}.deposits.FD621974.nominee.relationship: str
$.customers.{*}.deposits.FD563479: dict
$.customers.{*}.deposits.FD563479.deposit_id: str
$.customers.{*}.deposits.FD563479.kind: str
$.customers.{*}.deposits.FD563479.principal: float
$.customers.{*}.deposits.FD563479.rate: float
$.customers.{*}.deposits.FD563479.tenure_months: int
$.customers.{*}.deposits.FD563479.start_date: str
$.customers.{*}.deposits.FD563479.maturity_date: str
$.customers.{*}.deposits.FD563479.maturity_amount: float
$.customers.{*}.deposits.FD563479.payout_type: str
$.customers.{*}.deposits.FD563479.maturity_instruction: str
$.customers.{*}.deposits.FD563479.status: str
$.customers.{*}.deposits.FD563479.payout_account: str
... (+101 lines)
```
- sample: `samples/downloaded_domains_data__banking_knowledge__secondary_source__db.json` (188 KB)

## downloaded_domains_data/banking_knowledge/secondary_source/kb.json

Размер: 117.7 КБ
Тип: JSON dict (len=1)
Схема:
```
$: dict
$.articles: len~59 | list
$.articles[]: dict
$.articles[].id: str
$.articles[].title: str
$.articles[].category: str
$.articles[].content: str
$.articles[].keywords: len~10 | len~11 | len~12 | len~9 | list
$.articles[].keywords[]: str
$.articles[].source: str
$.articles[].last_updated: str
```
- sample: `samples/downloaded_domains_data__banking_knowledge__secondary_source__kb.json` (79 KB)

## downloaded_domains_data/banking_knowledge/secondary_source/train.jsonl

Размер: 5682.1 КБ
Тип: JSONL; прочитано строк: 250 (битых: 0, лимит 20000)
Схема (объединение по первым записям):
```
$: dict
$.responses_create_params: dict
$.responses_create_params.input: len~1 | list
$.responses_create_params.input[]: dict
$.responses_create_params.input[].role: str
$.responses_create_params.input[].content: str
$.responses_create_params.tools: len~34 | list
$.responses_create_params.tools[]: dict
$.responses_create_params.tools[].type: str
$.responses_create_params.tools[].name: str
$.responses_create_params.tools[].description: str
$.responses_create_params.tools[].parameters: dict
$.responses_create_params.tools[].parameters.type: str
$.responses_create_params.tools[].parameters.properties: dict
$.responses_create_params.tools[].parameters.properties.query: dict
$.responses_create_params.tools[].parameters.properties.query.type: str
$.responses_create_params.tools[].parameters.properties.bank_id: dict
$.responses_create_params.tools[].parameters.properties.bank_id.type: str
$.responses_create_params.tools[].parameters.properties.category: dict
$.responses_create_params.tools[].parameters.properties.category.type: str
$.responses_create_params.tools[].parameters.properties.top_k: dict
$.responses_create_params.tools[].parameters.properties.top_k.type: str
$.responses_create_params.tools[].parameters.required: len~0 | len~1 | len~2 | len~3 | len~5 | list
$.responses_create_params.tools[].parameters.required[]: str
$.responses_create_params.tools[].strict: bool
$.responses_create_params.tools[].parameters.properties.account_ids: dict
$.responses_create_params.tools[].parameters.properties.account_ids.type: str
$.responses_create_params.tools[].parameters.properties.account_ids.items: dict
$.responses_create_params.tools[].parameters.properties.account_ids.items.type: str
$.responses_create_params.tools[].parameters.properties.account_id: dict
$.responses_create_params.tools[].parameters.properties.account_id.type: str
$.responses_create_params.tools[].parameters.properties.from_date: dict
$.responses_create_params.tools[].parameters.properties.from_date.type: str
$.responses_create_params.tools[].parameters.properties.to_date: dict
$.responses_create_params.tools[].parameters.properties.to_date.type: str
$.responses_create_params.tools[].parameters.properties.type: dict
$.responses_create_params.tools[].parameters.properties.type.type: str
$.responses_create_params.tools[].parameters.properties.type.enum: len~3 | len~6 | list
$.responses_create_params.tools[].parameters.properties.type.enum[]: str
$.responses_create_params.tools[].parameters.properties.channel: dict
$.responses_create_params.tools[].parameters.properties.channel.type: str
$.responses_create_params.tools[].parameters.properties.channel.enum: len~8 | list
$.responses_create_params.tools[].parameters.properties.channel.enum[]: str
$.responses_create_params.tools[].parameters.properties.limit: dict
$.responses_create_params.tools[].parameters.properties.limit.type: str
$.responses_create_params.tools[].parameters.properties.offset: dict
$.responses_create_params.tools[].parameters.properties.offset.type: str
$.responses_create_params.tools[].parameters.properties.deposit_ids: dict
$.responses_create_params.tools[].parameters.properties.deposit_ids.type: str
$.responses_create_params.tools[].parameters.properties.deposit_ids.items: dict
$.responses_create_params.tools[].parameters.properties.deposit_ids.items.type: str
$.responses_create_params.tools[].parameters.properties.product_type: dict
$.responses_create_params.tools[].parameters.properties.product_type.type: str
$.responses_create_params.tools[].parameters.properties.product_type.enum: len~5 | list
$.responses_create_params.tools[].parameters.properties.product_type.enum[]: str
$.responses_create_params.tools[].parameters.properties.tenure_months: dict
$.responses_create_params.tools[].parameters.properties.tenure_months.type: str
$.responses_create_params.tools[].parameters.properties.amount: dict
$.responses_create_params.tools[].parameters.properties.amount.type: str
$.responses_create_params.tools[].parameters.properties.principal_amount: dict
$.responses_create_params.tools[].parameters.properties.principal_amount.type: str
$.responses_create_params.tools[].parameters.properties.rate: dict
$.responses_create_params.tools[].parameters.properties.rate.type: str
$.responses_create_params.tools[].parameters.properties.payout_type: dict
$.responses_create_params.tools[].parameters.properties.payout_type.type: str
$.responses_create_params.tools[].parameters.properties.payout_type.enum: len~3 | list
$.responses_create_params.tools[].parameters.properties.payout_type.enum[]: str
$.responses_create_params.tools[].parameters.properties.monthly_installment: dict
$.responses_create_params.tools[].parameters.properties.monthly_installment.type: str
$.responses_create_params.tools[].parameters.properties.source_account: dict
$.responses_create_params.tools[].parameters.properties.source_account.type: str
$.responses_create_params.tools[].parameters.properties.maturity_instruction: dict
$.responses_create_params.tools[].parameters.properties.maturity_instruction.type: str
$.responses_create_params.tools[].parameters.properties.maturity_instruction.enum: len~3 | list
$.responses_create_params.tools[].parameters.properties.maturity_instruction.enum[]: str
$.responses_create_params.tools[].parameters.properties.nominee: dict
$.responses_create_params.tools[].parameters.properties.nominee.type: str
$.responses_create_params.tools[].parameters.properties.deposit_id: dict
$.responses_create_params.tools[].parameters.properties.deposit_id.type: str
$.responses_create_params.tools[].parameters.properties.payout_account: dict
$.responses_create_params.tools[].parameters.properties.payout_account.type: str
$.responses_create_params.tools[].parameters.properties.instruction: dict
$.responses_create_params.tools[].parameters.properties.instruction.type: str
$.responses_create_params.tools[].parameters.properties.instruction.enum: len~3 | list
$.responses_create_params.tools[].parameters.properties.instruction.enum[]: str
$.responses_create_params.tools[].parameters.properties.loan_ids: dict
$.responses_create_params.tools[].parameters.properties.loan_ids.type: str
$.responses_create_params.tools[].parameters.properties.loan_ids.items: dict
$.responses_create_params.tools[].parameters.properties.loan_ids.items.type: str
$.responses_create_params.tools[].parameters.properties.as_of_date: dict
$.responses_create_params.tools[].parameters.properties.as_of_date.type: str
$.responses_create_params.tools[].parameters.properties.principal: dict
$.responses_create_params.tools[].parameters.properties.principal.type: str
$.responses_create_params.tools[].parameters.properties.purity_karat: dict
$.responses_create_params.tools[].parameters.properties.purity_karat.type: str
$.responses_create_params.tools[].parameters.properties.purity_karat.enum: len~3 | list
$.responses_create_params.tools[].parameters.properties.purity_karat.enum[]: int
$.responses_create_params.tools[].parameters.properties.gold_grams: dict
$.responses_create_params.tools[].parameters.properties.gold_grams.type: str
$.responses_create_params.tools[].parameters.properties.gold_rate_per_gram: dict
$.responses_create_params.tools[].parameters.properties.gold_rate_per_gram.type: str
$.responses_create_params.tools[].parameters.properties.card_ids: dict
$.responses_create_params.tools[].parameters.properties.card_ids.type: str
$.responses_create_params.tools[].parameters.properties.card_ids.items: dict
$.responses_create_params.tools[].parameters.properties.card_ids.items.type: str
$.responses_create_params.tools[].parameters.properties.card_id: dict
$.responses_create_params.tools[].parameters.properties.card_id.type: str
$.responses_create_params.tools[].parameters.properties.state: dict
$.responses_create_params.tools[].parameters.properties.state.type: str
$.responses_create_params.tools[].parameters.properties.state.enum: len~2 | list
$.responses_create_params.tools[].parameters.properties.state.enum[]: str
$.responses_create_params.tools[].parameters.properties.reason: dict
$.responses_create_params.tools[].parameters.properties.reason.type: str
$.responses_create_params.tools[].parameters.properties.reason.enum: len~3 | len~4 | list
$.responses_create_params.tools[].parameters.properties.reason.enum[]: str
$.responses_create_params.tools[].parameters.properties.atm: dict
$.responses_create_params.tools[].parameters.properties.atm.type: str
$.responses_create_params.tools[].parameters.properties.online: dict
$.responses_create_params.tools[].parameters.properties.online.type: str
$.responses_create_params.tools[].parameters.properties.pos: dict
$.responses_create_params.tools[].parameters.properties.pos.type: str
$.responses_create_params.tools[].parameters.properties.status: dict
$.responses_create_params.tools[].parameters.properties.status.type: str
$.responses_create_params.tools[].parameters.properties.status.enum: len~4 | list
$.responses_create_params.tools[].parameters.properties.status.enum[]: str
$.responses_create_params.tools[].parameters.properties.mandate_id: dict
$.responses_create_params.tools[].parameters.properties.mandate_id.type: str
$.responses_create_params.tools[].parameters.properties.cheque_numbers: dict
$.responses_create_params.tools[].parameters.properties.cheque_numbers.type: str
$.responses_create_params.tools[].parameters.properties.cheque_numbers.items: dict
$.responses_create_params.tools[].parameters.properties.cheque_numbers.items.type: str
$.responses_create_params.tools[].parameters.properties.leaves: dict
$.responses_create_params.tools[].parameters.properties.leaves.type: str
$.responses_create_params.tools[].parameters.properties.delivery_address: dict
$.responses_create_params.tools[].parameters.properties.delivery_address.type: str
$.responses_create_params.tools[].parameters.properties.delivery_mode: dict
$.responses_create_params.tools[].parameters.properties.delivery_mode.type: str
$.responses_create_params.tools[].parameters.properties.delivery_mode.enum: len~2 | list
$.responses_create_params.tools[].parameters.properties.delivery_mode.enum[]: str
$.responses_create_params.tools[].parameters.properties.address_type: dict
$.responses_create_params.tools[].parameters.properties.address_type.type: str
$.responses_create_params.tools[].parameters.properties.address_type.enum: len~2 | list
$.responses_create_params.tools[].parameters.properties.address_type.enum[]: str
$.responses_create_params.tools[].parameters.properties.line1: dict
$.responses_create_params.tools[].parameters.properties.line1.type: str
$.responses_create_params.tools[].parameters.properties.city: dict
$.responses_create_params.tools[].parameters.properties.city.type: str
$.responses_create_params.tools[].parameters.properties.pincode: dict
$.responses_create_params.tools[].parameters.properties.pincode.type: str
$.responses_create_params.tools[].parameters.properties.line2: dict
$.responses_create_params.tools[].parameters.properties.line2.type: str
$.responses_create_params.tools[].parameters.properties.description: dict
$.responses_create_params.tools[].parameters.properties.description.type: str
$.responses_create_params.tools[].parameters.properties.category.enum: len~7 | list
$.responses_create_params.tools[].parameters.properties.category.enum[]: str
$.responses_create_params.tools[].parameters.properties.related_transaction_id: dict
$.responses_create_params.tools[].parameters.properties.related_transaction_id.type: str
$.responses_create_params.tools[].parameters.properties.request_id: dict
$.responses_create_params.tools[].parameters.properties.request_id.type: str
$.responses_create_params.tools[].parameters.properties.policy_ids: dict
$.responses_create_params.tools[].parameters.properties.policy_ids.type: str
$.responses_create_params.tools[].parameters.properties.policy_ids.items: dict
$.responses_create_params.tools[].parameters.properties.policy_ids.items.type: str
$.responses_create_params.tools[].parameters.properties.summary: dict
$.responses_create_params.tools[].parameters.properties.summary.type: str
$.responses_create_params.tools[].parameters.properties.summary.description: str
$.responses_create_params.parallel_tool_calls: bool
$.task_id: str
$.customer: str
$.user_scenario: dict
$.user_scenario.persona: str
$.user_scenario.instructions: dict
$.user_scenario.instructions.domain: str
$.user_scenario.instructions.reason_for_call: str
$.user_scenario.instructions.known_info: str
$.user_scenario.instructions.unknown_info: str
$.user_scenario.instructions.task_instructions: str
$.evaluation_criteria: dict
$.evaluation_criteria.actions: len~0 | len~1 | len~2 | len~3 | len~4 | len~5 | len~6 | list
$.evaluation_criteria.communicate_info: len~0 | len~1 | len~2 | list
$.evaluation_criteria.nl_assertions: len~1 | len~2 | list
$.evaluation_criteria.nl_assertions[]: str
$.evaluation_criteria.reward_basis: len~2 | len~3 | len~4 | list
$.evaluation_criteria.reward_basis[]: str
$.initial_state: dict
$.initial_state.initialization_data: dict
$.initial_state.initialization_data.agent_data: dict
$.initial_state.initialization_data.agent_data.active_customer: str
$.initial_state.initialization_data.user_data: NoneType
$.initial_state.initialization_actions: NoneType
$.initial_state.message_history: NoneType
$.opening_message: str
$.evaluation_criteria.actions[]: dict
$.evaluation_criteria.actions[].action_id: str
$.evaluation_criteria.actions[].name: str
$.evaluation_criteria.actions[].arguments: dict
$.evaluation_criteria.actions[].arguments.description: str
$.evaluation_criteria.actions[].arguments.category: str
$.evaluation_criteria.actions[].compare_args: NoneType | len~0 | len~1 | len~2 | len~3 | len~4 | list
$.evaluation_criteria.actions[].compare_args[]: str
$.evaluation_criteria.communicate_info[]: str
$.evaluation_criteria.actions[].arguments.deposit_ids: len~1 | len~3 | list
$.evaluation_criteria.actions[].arguments.deposit_ids[]: str
$.evaluation_criteria.actions[].arguments.account_ids: len~1 | len~2 | list
$.evaluation_criteria.actions[].arguments.account_ids[]: str
$.evaluation_criteria.actions[].arguments.account_id: str
$.evaluation_criteria.actions[].arguments.from_date: str
$.evaluation_criteria.actions[].arguments.to_date: str
$.evaluation_criteria.actions[].arguments.query: str
$.evaluation_criteria.actions[].arguments.cheque_numbers: len~1 | list
$.evaluation_criteria.actions[].arguments.cheque_numbers[]: str
$.evaluation_criteria.actions[].arguments.leaves: int
$.evaluation_criteria.actions[].arguments.product_type: str
$.evaluation_criteria.actions[].arguments.tenure_months: int
$.evaluation_criteria.actions[].arguments.principal_amount: int
$.evaluation_criteria.actions[].arguments.rate: float | int
$.evaluation_criteria.actions[].arguments.source_account: str
$.evaluation_criteria.actions[].arguments.deposit_id: str
$.evaluation_criteria.actions[].arguments.payout_account: str
$.evaluation_criteria.actions[].arguments.purity_karat: int
$.evaluation_criteria.actions[].arguments.gold_grams: int
$.evaluation_criteria.actions[].arguments.gold_rate_per_gram: int
$.evaluation_criteria.actions[].arguments.card_id: str
$.evaluation_criteria.actions[].arguments.reason: str
$.evaluation_criteria.actions[].arguments.online: dict
$.evaluation_criteria.actions[].arguments.online.international: dict
$.evaluation_criteria.actions[].arguments.online.international.enabled: bool
$.evaluation_criteria.actions[].arguments.request_id: str
$.evaluation_criteria.actions[].arguments.instruction: str
$.evaluation_criteria.actions[].arguments.address_type: str
$.evaluation_criteria.actions[].arguments.line1: str
$.evaluation_criteria.actions[].arguments.city: str
$.evaluation_criteria.actions[].arguments.state: str
$.evaluation_criteria.actions[].arguments.pincode: str
$.evaluation_criteria.actions[].arguments.policy_ids: len~1 | list
$.evaluation_criteria.actions[].arguments.policy_ids[]: str
$.evaluation_criteria.max_tool_calls: int
$.evaluation_criteria.actions[].arguments.mandate_id: str
$.evaluation_criteria.actions[].arguments.principal: int
$.evaluation_criteria.actions[].arguments.card_ids: len~1 | len~2 | list
$.evaluation_criteria.actions[].arguments.card_ids[]: str
$.evaluation_criteria.actions[].arguments.monthly_installment: int
$.evaluation_criteria.actions[].arguments.related_transaction_id: str
$.evaluation_criteria.actions[].arguments.pos: dict
$.evaluation_criteria.actions[].arguments.pos.international: dict
$.evaluation_criteria.actions[].arguments.pos.international.enabled: bool
$.evaluation_criteria.actions[].arguments.status: str
$.evaluation_criteria.actions[].arguments.loan_ids: len~1 | list
$.evaluation_criteria.actions[].arguments.loan_ids[]: str
$.evaluation_criteria.actions[].arguments.type: str
$.evaluation_criteria.actions[].arguments.online.domestic: dict
$.evaluation_criteria.actions[].arguments.online.domestic.enabled: bool
$.evaluation_criteria.actions[].arguments.online.domestic.daily_limit: int
$.evaluation_criteria.actions[].arguments.delivery_mode: str
```
- sample: `samples/downloaded_domains_data__banking_knowledge__secondary_source__train.jsonl__line0.json` (30 KB)
- sample: `samples/downloaded_domains_data__banking_knowledge__secondary_source__train.jsonl__FULL_line0.json` (33 KB)

## downloaded_domains_data/banking_knowledge/secondary_source/validation.jsonl

Размер: 1133.4 КБ
Тип: JSONL; прочитано строк: 50 (битых: 0, лимит 20000)
Схема (объединение по первым записям):
```
$: dict
$.responses_create_params: dict
$.responses_create_params.input: len~1 | list
$.responses_create_params.input[]: dict
$.responses_create_params.input[].role: str
$.responses_create_params.input[].content: str
$.responses_create_params.tools: len~34 | list
$.responses_create_params.tools[]: dict
$.responses_create_params.tools[].type: str
$.responses_create_params.tools[].name: str
$.responses_create_params.tools[].description: str
$.responses_create_params.tools[].parameters: dict
$.responses_create_params.tools[].parameters.type: str
$.responses_create_params.tools[].parameters.properties: dict
$.responses_create_params.tools[].parameters.properties.query: dict
$.responses_create_params.tools[].parameters.properties.query.type: str
$.responses_create_params.tools[].parameters.properties.bank_id: dict
$.responses_create_params.tools[].parameters.properties.bank_id.type: str
$.responses_create_params.tools[].parameters.properties.category: dict
$.responses_create_params.tools[].parameters.properties.category.type: str
$.responses_create_params.tools[].parameters.properties.top_k: dict
$.responses_create_params.tools[].parameters.properties.top_k.type: str
$.responses_create_params.tools[].parameters.required: len~0 | len~1 | len~2 | len~3 | len~5 | list
$.responses_create_params.tools[].parameters.required[]: str
$.responses_create_params.tools[].strict: bool
$.responses_create_params.tools[].parameters.properties.account_ids: dict
$.responses_create_params.tools[].parameters.properties.account_ids.type: str
$.responses_create_params.tools[].parameters.properties.account_ids.items: dict
$.responses_create_params.tools[].parameters.properties.account_ids.items.type: str
$.responses_create_params.tools[].parameters.properties.account_id: dict
$.responses_create_params.tools[].parameters.properties.account_id.type: str
$.responses_create_params.tools[].parameters.properties.from_date: dict
$.responses_create_params.tools[].parameters.properties.from_date.type: str
$.responses_create_params.tools[].parameters.properties.to_date: dict
$.responses_create_params.tools[].parameters.properties.to_date.type: str
$.responses_create_params.tools[].parameters.properties.type: dict
$.responses_create_params.tools[].parameters.properties.type.type: str
$.responses_create_params.tools[].parameters.properties.type.enum: len~3 | len~6 | list
$.responses_create_params.tools[].parameters.properties.type.enum[]: str
$.responses_create_params.tools[].parameters.properties.channel: dict
$.responses_create_params.tools[].parameters.properties.channel.type: str
$.responses_create_params.tools[].parameters.properties.channel.enum: len~8 | list
$.responses_create_params.tools[].parameters.properties.channel.enum[]: str
$.responses_create_params.tools[].parameters.properties.limit: dict
$.responses_create_params.tools[].parameters.properties.limit.type: str
$.responses_create_params.tools[].parameters.properties.offset: dict
$.responses_create_params.tools[].parameters.properties.offset.type: str
$.responses_create_params.tools[].parameters.properties.deposit_ids: dict
$.responses_create_params.tools[].parameters.properties.deposit_ids.type: str
$.responses_create_params.tools[].parameters.properties.deposit_ids.items: dict
$.responses_create_params.tools[].parameters.properties.deposit_ids.items.type: str
$.responses_create_params.tools[].parameters.properties.product_type: dict
$.responses_create_params.tools[].parameters.properties.product_type.type: str
$.responses_create_params.tools[].parameters.properties.product_type.enum: len~5 | list
$.responses_create_params.tools[].parameters.properties.product_type.enum[]: str
$.responses_create_params.tools[].parameters.properties.tenure_months: dict
$.responses_create_params.tools[].parameters.properties.tenure_months.type: str
$.responses_create_params.tools[].parameters.properties.amount: dict
$.responses_create_params.tools[].parameters.properties.amount.type: str
$.responses_create_params.tools[].parameters.properties.principal_amount: dict
$.responses_create_params.tools[].parameters.properties.principal_amount.type: str
$.responses_create_params.tools[].parameters.properties.rate: dict
$.responses_create_params.tools[].parameters.properties.rate.type: str
$.responses_create_params.tools[].parameters.properties.payout_type: dict
$.responses_create_params.tools[].parameters.properties.payout_type.type: str
$.responses_create_params.tools[].parameters.properties.payout_type.enum: len~3 | list
$.responses_create_params.tools[].parameters.properties.payout_type.enum[]: str
$.responses_create_params.tools[].parameters.properties.monthly_installment: dict
$.responses_create_params.tools[].parameters.properties.monthly_installment.type: str
$.responses_create_params.tools[].parameters.properties.source_account: dict
$.responses_create_params.tools[].parameters.properties.source_account.type: str
$.responses_create_params.tools[].parameters.properties.maturity_instruction: dict
$.responses_create_params.tools[].parameters.properties.maturity_instruction.type: str
$.responses_create_params.tools[].parameters.properties.maturity_instruction.enum: len~3 | list
$.responses_create_params.tools[].parameters.properties.maturity_instruction.enum[]: str
$.responses_create_params.tools[].parameters.properties.nominee: dict
$.responses_create_params.tools[].parameters.properties.nominee.type: str
$.responses_create_params.tools[].parameters.properties.deposit_id: dict
$.responses_create_params.tools[].parameters.properties.deposit_id.type: str
$.responses_create_params.tools[].parameters.properties.payout_account: dict
$.responses_create_params.tools[].parameters.properties.payout_account.type: str
$.responses_create_params.tools[].parameters.properties.instruction: dict
$.responses_create_params.tools[].parameters.properties.instruction.type: str
$.responses_create_params.tools[].parameters.properties.instruction.enum: len~3 | list
$.responses_create_params.tools[].parameters.properties.instruction.enum[]: str
$.responses_create_params.tools[].parameters.properties.loan_ids: dict
$.responses_create_params.tools[].parameters.properties.loan_ids.type: str
$.responses_create_params.tools[].parameters.properties.loan_ids.items: dict
$.responses_create_params.tools[].parameters.properties.loan_ids.items.type: str
$.responses_create_params.tools[].parameters.properties.as_of_date: dict
$.responses_create_params.tools[].parameters.properties.as_of_date.type: str
$.responses_create_params.tools[].parameters.properties.principal: dict
$.responses_create_params.tools[].parameters.properties.principal.type: str
$.responses_create_params.tools[].parameters.properties.purity_karat: dict
$.responses_create_params.tools[].parameters.properties.purity_karat.type: str
$.responses_create_params.tools[].parameters.properties.purity_karat.enum: len~3 | list
$.responses_create_params.tools[].parameters.properties.purity_karat.enum[]: int
$.responses_create_params.tools[].parameters.properties.gold_grams: dict
$.responses_create_params.tools[].parameters.properties.gold_grams.type: str
$.responses_create_params.tools[].parameters.properties.gold_rate_per_gram: dict
$.responses_create_params.tools[].parameters.properties.gold_rate_per_gram.type: str
$.responses_create_params.tools[].parameters.properties.card_ids: dict
$.responses_create_params.tools[].parameters.properties.card_ids.type: str
$.responses_create_params.tools[].parameters.properties.card_ids.items: dict
$.responses_create_params.tools[].parameters.properties.card_ids.items.type: str
$.responses_create_params.tools[].parameters.properties.card_id: dict
$.responses_create_params.tools[].parameters.properties.card_id.type: str
$.responses_create_params.tools[].parameters.properties.state: dict
$.responses_create_params.tools[].parameters.properties.state.type: str
$.responses_create_params.tools[].parameters.properties.state.enum: len~2 | list
$.responses_create_params.tools[].parameters.properties.state.enum[]: str
$.responses_create_params.tools[].parameters.properties.reason: dict
$.responses_create_params.tools[].parameters.properties.reason.type: str
$.responses_create_params.tools[].parameters.properties.reason.enum: len~3 | len~4 | list
$.responses_create_params.tools[].parameters.properties.reason.enum[]: str
$.responses_create_params.tools[].parameters.properties.atm: dict
$.responses_create_params.tools[].parameters.properties.atm.type: str
$.responses_create_params.tools[].parameters.properties.online: dict
$.responses_create_params.tools[].parameters.properties.online.type: str
$.responses_create_params.tools[].parameters.properties.pos: dict
$.responses_create_params.tools[].parameters.properties.pos.type: str
$.responses_create_params.tools[].parameters.properties.status: dict
$.responses_create_params.tools[].parameters.properties.status.type: str
$.responses_create_params.tools[].parameters.properties.status.enum: len~4 | list
$.responses_create_params.tools[].parameters.properties.status.enum[]: str
$.responses_create_params.tools[].parameters.properties.mandate_id: dict
$.responses_create_params.tools[].parameters.properties.mandate_id.type: str
$.responses_create_params.tools[].parameters.properties.cheque_numbers: dict
$.responses_create_params.tools[].parameters.properties.cheque_numbers.type: str
$.responses_create_params.tools[].parameters.properties.cheque_numbers.items: dict
$.responses_create_params.tools[].parameters.properties.cheque_numbers.items.type: str
$.responses_create_params.tools[].parameters.properties.leaves: dict
$.responses_create_params.tools[].parameters.properties.leaves.type: str
$.responses_create_params.tools[].parameters.properties.delivery_address: dict
$.responses_create_params.tools[].parameters.properties.delivery_address.type: str
$.responses_create_params.tools[].parameters.properties.delivery_mode: dict
$.responses_create_params.tools[].parameters.properties.delivery_mode.type: str
$.responses_create_params.tools[].parameters.properties.delivery_mode.enum: len~2 | list
$.responses_create_params.tools[].parameters.properties.delivery_mode.enum[]: str
$.responses_create_params.tools[].parameters.properties.address_type: dict
$.responses_create_params.tools[].parameters.properties.address_type.type: str
$.responses_create_params.tools[].parameters.properties.address_type.enum: len~2 | list
$.responses_create_params.tools[].parameters.properties.address_type.enum[]: str
$.responses_create_params.tools[].parameters.properties.line1: dict
$.responses_create_params.tools[].parameters.properties.line1.type: str
$.responses_create_params.tools[].parameters.properties.city: dict
$.responses_create_params.tools[].parameters.properties.city.type: str
$.responses_create_params.tools[].parameters.properties.pincode: dict
$.responses_create_params.tools[].parameters.properties.pincode.type: str
$.responses_create_params.tools[].parameters.properties.line2: dict
$.responses_create_params.tools[].parameters.properties.line2.type: str
$.responses_create_params.tools[].parameters.properties.description: dict
$.responses_create_params.tools[].parameters.properties.description.type: str
$.responses_create_params.tools[].parameters.properties.category.enum: len~7 | list
$.responses_create_params.tools[].parameters.properties.category.enum[]: str
$.responses_create_params.tools[].parameters.properties.related_transaction_id: dict
$.responses_create_params.tools[].parameters.properties.related_transaction_id.type: str
$.responses_create_params.tools[].parameters.properties.request_id: dict
$.responses_create_params.tools[].parameters.properties.request_id.type: str
$.responses_create_params.tools[].parameters.properties.policy_ids: dict
$.responses_create_params.tools[].parameters.properties.policy_ids.type: str
$.responses_create_params.tools[].parameters.properties.policy_ids.items: dict
$.responses_create_params.tools[].parameters.properties.policy_ids.items.type: str
$.responses_create_params.tools[].parameters.properties.summary: dict
$.responses_create_params.tools[].parameters.properties.summary.type: str
$.responses_create_params.tools[].parameters.properties.summary.description: str
$.responses_create_params.parallel_tool_calls: bool
$.task_id: str
$.customer: str
$.user_scenario: dict
$.user_scenario.persona: str
$.user_scenario.instructions: dict
$.user_scenario.instructions.domain: str
$.user_scenario.instructions.reason_for_call: str
$.user_scenario.instructions.known_info: str
$.user_scenario.instructions.unknown_info: NoneType | str
$.user_scenario.instructions.task_instructions: str
$.evaluation_criteria: dict
$.evaluation_criteria.actions: len~0 | len~1 | len~2 | len~3 | len~4 | len~5 | len~6 | list
$.evaluation_criteria.actions[]: dict
$.evaluation_criteria.actions[].action_id: str
$.evaluation_criteria.actions[].name: str
$.evaluation_criteria.actions[].arguments: dict
$.evaluation_criteria.actions[].arguments.card_ids: len~1 | len~2 | list
$.evaluation_criteria.actions[].arguments.card_ids[]: str
$.evaluation_criteria.actions[].compare_args: NoneType | len~0 | len~1 | len~2 | len~3 | list
$.evaluation_criteria.communicate_info: len~0 | len~1 | list
$.evaluation_criteria.nl_assertions: len~1 | len~2 | list
$.evaluation_criteria.nl_assertions[]: str
$.evaluation_criteria.reward_basis: len~2 | len~3 | len~4 | list
$.evaluation_criteria.reward_basis[]: str
$.initial_state: dict
$.initial_state.initialization_data: dict
$.initial_state.initialization_data.agent_data: dict
$.initial_state.initialization_data.agent_data.active_customer: str
$.initial_state.initialization_data.user_data: NoneType
$.initial_state.initialization_actions: NoneType
$.initial_state.message_history: NoneType
$.opening_message: str
$.evaluation_criteria.actions[].arguments.policy_ids: len~1 | list
$.evaluation_criteria.actions[].arguments.policy_ids[]: str
$.evaluation_criteria.communicate_info[]: str
$.evaluation_criteria.actions[].arguments.card_id: str
$.evaluation_criteria.actions[].arguments.state: str
$.evaluation_criteria.actions[].arguments.deposit_ids: len~1 | list
$.evaluation_criteria.actions[].arguments.deposit_ids[]: str
$.evaluation_criteria.actions[].arguments.deposit_id: str
$.evaluation_criteria.actions[].arguments.payout_account: str
$.evaluation_criteria.actions[].arguments.principal_amount: int
$.evaluation_criteria.actions[].arguments.tenure_months: int
$.evaluation_criteria.actions[].arguments.source_account: str
$.evaluation_criteria.actions[].compare_args[]: str
$.evaluation_criteria.require_transfer: bool
$.evaluation_criteria.actions[].arguments.purity_karat: int
$.evaluation_criteria.actions[].arguments.query: str
$.evaluation_criteria.actions[].arguments.description: str
$.evaluation_criteria.actions[].arguments.category: str
$.evaluation_criteria.actions[].arguments.account_ids: len~1 | list
$.evaluation_criteria.actions[].arguments.account_ids[]: str
$.evaluation_criteria.actions[].arguments.type: str
$.evaluation_criteria.actions[].arguments.account_id: str
$.evaluation_criteria.actions[].arguments.from_date: str
$.evaluation_criteria.actions[].arguments.to_date: str
$.evaluation_criteria.actions[].arguments.delivery_mode: str
$.evaluation_criteria.actions[].arguments.reason: str
$.evaluation_criteria.actions[].arguments.product_type: str
$.evaluation_criteria.actions[].arguments.related_transaction_id: str
$.evaluation_criteria.actions[].arguments.loan_ids: len~1 | list
$.evaluation_criteria.actions[].arguments.loan_ids[]: str
$.evaluation_criteria.actions[].arguments.monthly_installment: int
$.evaluation_criteria.actions[].arguments.principal: int
$.evaluation_criteria.actions[].arguments.rate: float
$.evaluation_criteria.actions[].arguments.gold_grams: int
$.evaluation_criteria.actions[].arguments.gold_rate_per_gram: int
$.evaluation_criteria.actions[].arguments.cheque_numbers: len~1 | list
$.evaluation_criteria.actions[].arguments.cheque_numbers[]: str
$.evaluation_criteria.actions[].arguments.instruction: str
$.evaluation_criteria.actions[].arguments.status: str
$.evaluation_criteria.actions[].arguments.mandate_id: str
$.evaluation_criteria.actions[].arguments.address_type: str
$.evaluation_criteria.actions[].arguments.line1: str
$.evaluation_criteria.actions[].arguments.city: str
$.evaluation_criteria.actions[].arguments.pincode: str
```
- sample: `samples/downloaded_domains_data__banking_knowledge__secondary_source__validation.jsonl__line0.json` (30 KB)
- sample: `samples/downloaded_domains_data__banking_knowledge__secondary_source__validation.jsonl__FULL_line0.json` (34 KB)

## downloaded_domains_data/banking_knowledge/tau2_env/db.json

Размер: 264.2 КБ
Тип: JSON dict (len=17)
Схема:
```
$: dict
$.users: dict
$.users.data: dict
$.users.data.123: dict
$.users.data.123.name: str
$.users.data.123.user_id: str
$.users.data.123.address: str
$.users.data.123.email: str
$.users.data.123.phone_number: str
$.users.data.123.date_of_birth: str
$.users.data.125: dict
$.users.data.125.name: str
$.users.data.125.user_id: str
$.users.data.125.address: str
$.users.data.125.email: str
$.users.data.125.phone_number: str
$.users.data.125.date_of_birth: str
$.users.data.6680a37184: dict
$.users.data.6680a37184.name: str
$.users.data.6680a37184.user_id: str
$.users.data.6680a37184.address: str
$.users.data.6680a37184.email: str
$.users.data.6680a37184.phone_number: str
$.users.data.6680a37184.date_of_birth: str
$.users.data.af0581dcbf: dict
$.users.data.af0581dcbf.name: str
$.users.data.af0581dcbf.user_id: str
$.users.data.af0581dcbf.address: str
$.users.data.af0581dcbf.email: str
$.users.data.af0581dcbf.phone_number: str
$.users.data.af0581dcbf.date_of_birth: str
$.users.data.86e92f639e: dict
$.users.data.86e92f639e.name: str
$.users.data.86e92f639e.user_id: str
$.users.data.86e92f639e.address: str
$.users.data.86e92f639e.email: str
$.users.data.86e92f639e.phone_number: str
$.users.data.86e92f639e.date_of_birth: str
$.users.data.d97fb90fe8: dict
$.users.data.d97fb90fe8.name: str
$.users.data.d97fb90fe8.user_id: str
$.users.data.d97fb90fe8.address: str
$.users.data.d97fb90fe8.email: str
$.users.data.d97fb90fe8.phone_number: str
$.users.data.d97fb90fe8.date_of_birth: str
$.users.data.76ad9cc60e: dict
$.users.data.76ad9cc60e.name: str
$.users.data.76ad9cc60e.user_id: str
$.users.data.76ad9cc60e.address: str
$.users.data.76ad9cc60e.email: str
$.users.data.76ad9cc60e.phone_number: str
$.users.data.76ad9cc60e.date_of_birth: str
$.users.data.890389b165: dict
$.users.data.890389b165.name: str
$.users.data.890389b165.user_id: str
$.users.data.890389b165.address: str
$.users.data.890389b165.email: str
$.users.data.890389b165.phone_number: str
$.users.data.890389b165.date_of_birth: str
$.users.data.d2e5bc4124: dict
$.users.data.d2e5bc4124.name: str
$.users.data.d2e5bc4124.user_id: str
$.users.data.d2e5bc4124.address: str
$.users.data.d2e5bc4124.email: str
$.users.data.d2e5bc4124.phone_number: str
$.users.data.d2e5bc4124.date_of_birth: str
$.users.data.755bcb4d5d: dict
$.users.data.755bcb4d5d.name: str
$.users.data.755bcb4d5d.user_id: str
$.users.data.755bcb4d5d.address: str
$.users.data.755bcb4d5d.email: str
$.users.data.755bcb4d5d.phone_number: str
$.users.data.755bcb4d5d.date_of_birth: str
$.users.data.584f9c5d00: dict
$.users.data.584f9c5d00.name: str
$.users.data.584f9c5d00.user_id: str
$.users.data.584f9c5d00.address: str
$.users.data.584f9c5d00.email: str
$.users.data.584f9c5d00.phone_number: str
$.users.data.584f9c5d00.date_of_birth: str
$.users.data.224959b99e: dict
$.users.data.224959b99e.name: str
$.users.data.224959b99e.user_id: str
$.users.data.224959b99e.address: str
$.users.data.224959b99e.email: str
$.users.data.224959b99e.phone_number: str
$.users.data.224959b99e.date_of_birth: str
$.users.data.f9bf8de0be: dict
$.users.data.f9bf8de0be.name: str
$.users.data.f9bf8de0be.user_id: str
$.users.data.f9bf8de0be.address: str
$.users.data.f9bf8de0be.email: str
$.users.data.f9bf8de0be.phone_number: str
$.users.data.f9bf8de0be.date_of_birth: str
$.users.data.01f21c9970: dict
$.users.data.01f21c9970.name: str
$.users.data.01f21c9970.user_id: str
$.users.data.01f21c9970.address: str
$.users.data.01f21c9970.email: str
$.users.data.01f21c9970.phone_number: str
$.users.data.01f21c9970.date_of_birth: str
$.users.data.4db6fc36e8: dict
$.users.data.4db6fc36e8.name: str
$.users.data.4db6fc36e8.user_id: str
$.users.data.4db6fc36e8.address: str
$.users.data.4db6fc36e8.email: str
$.users.data.4db6fc36e8.phone_number: str
$.users.data.4db6fc36e8.date_of_birth: str
$.users.data.a6a7d745b2: dict
$.users.data.a6a7d745b2.name: str
$.users.data.a6a7d745b2.user_id: str
$.users.data.a6a7d745b2.address: str
$.users.data.a6a7d745b2.email: str
$.users.data.a6a7d745b2.phone_number: str
$.users.data.a6a7d745b2.date_of_birth: str
$.users.data.601e851551: dict
$.users.data.601e851551.name: str
$.users.data.601e851551.user_id: str
$.users.data.601e851551.address: str
$.users.data.601e851551.email: str
$.users.data.601e851551.phone_number: str
$.users.data.601e851551.date_of_birth: str
$.users.data.3d91a520be: dict
$.users.data.3d91a520be.name: str
$.users.data.3d91a520be.user_id: str
$.users.data.3d91a520be.address: str
$.users.data.3d91a520be.email: str
$.users.data.3d91a520be.phone_number: str
$.users.data.3d91a520be.date_of_birth: str
$.users.data.5e4c1a83b0: dict
$.users.data.5e4c1a83b0.name: str
$.users.data.5e4c1a83b0.user_id: str
$.users.data.5e4c1a83b0.address: str
$.users.data.5e4c1a83b0.email: str
$.users.data.5e4c1a83b0.phone_number: str
$.users.data.5e4c1a83b0.date_of_birth: str
$.users.data.126: dict
$.users.data.126.name: str
$.users.data.126.user_id: str
$.users.data.126.address: str
$.users.data.126.email: str
$.users.data.126.phone_number: str
$.users.data.126.date_of_birth: str
$.users.data.c7d8e9f0a1: dict
$.users.data.c7d8e9f0a1.name: str
$.users.data.c7d8e9f0a1.user_id: str
$.users.data.c7d8e9f0a1.address: str
$.users.data.c7d8e9f0a1.email: str
$.users.data.c7d8e9f0a1.phone_number: str
$.users.data.c7d8e9f0a1.date_of_birth: str
$.users.data.e3f4a5b6c7: dict
$.users.data.e3f4a5b6c7.name: str
$.users.data.e3f4a5b6c7.user_id: str
$.users.data.e3f4a5b6c7.address: str
$.users.data.e3f4a5b6c7.email: str
$.users.data.e3f4a5b6c7.phone_number: str
$.users.data.e3f4a5b6c7.date_of_birth: str
$.users.data.h1i2j3k4l5: dict
$.users.data.h1i2j3k4l5.name: str
$.users.data.h1i2j3k4l5.user_id: str
$.users.data.h1i2j3k4l5.address: str
$.users.data.h1i2j3k4l5.email: str
$.users.data.h1i2j3k4l5.phone_number: str
$.users.data.h1i2j3k4l5.date_of_birth: str
$.users.data.e9d195fe8e: dict
$.users.data.e9d195fe8e.name: str
$.users.data.e9d195fe8e.user_id: str
$.users.data.e9d195fe8e.address: str
$.users.data.e9d195fe8e.email: str
$.users.data.e9d195fe8e.phone_number: str
$.users.data.e9d195fe8e.date_of_birth: str
$.users.data.b5e8f2a1c9: dict
$.users.data.b5e8f2a1c9.name: str
$.users.data.b5e8f2a1c9.user_id: str
$.users.data.b5e8f2a1c9.address: str
$.users.data.b5e8f2a1c9.email: str
$.users.data.b5e8f2a1c9.phone_number: str
$.users.data.b5e8f2a1c9.date_of_birth: str
$.users.data.a8c4e2f7b3: dict
$.users.data.a8c4e2f7b3.name: str
$.users.data.a8c4e2f7b3.user_id: str
$.users.data.a8c4e2f7b3.address: str
$.users.data.a8c4e2f7b3.email: str
$.users.data.a8c4e2f7b3.phone_number: str
$.users.data.a8c4e2f7b3.date_of_birth: str
$.users.data.jm60a8b9c2: dict
$.users.data.jm60a8b9c2.name: str
$.users.data.jm60a8b9c2.user_id: str
$.users.data.jm60a8b9c2.address: str
$.users.data.jm60a8b9c2.email: str
$.users.data.jm60a8b9c2.phone_number: str
$.users.data.jm60a8b9c2.date_of_birth: str
$.users.data.jc61f7a8d2: dict
$.users.data.jc61f7a8d2.name: str
$.users.data.jc61f7a8d2.user_id: str
$.users.data.jc61f7a8d2.address: str
$.users.data.jc61f7a8d2.email: str
$.users.data.jc61f7a8d2.phone_number: str
$.users.data.jc61f7a8d2.date_of_birth: str
$.users.data.mm61b4c8d3: dict
$.users.data.mm61b4c8d3.name: str
$.users.data.mm61b4c8d3.user_id: str
$.users.data.mm61b4c8d3.address: str
$.users.data.mm61b4c8d3.email: str
$.users.data.mm61b4c8d3.phone_number: str
$.users.data.mm61b4c8d3.date_of_birth: str
$.users.data.tb58a3c9d2: dict
$.users.data.tb58a3c9d2.name: str
$.users.data.tb58a3c9d2.user_id: str
$.users.data.tb58a3c9d2.address: str
$.users.data.tb58a3c9d2.email: str
$.users.data.tb58a3c9d2.phone_number: str
$.users.data.tb58a3c9d2.date_of_birth: str
$.users.data.cr59b4d8e3: dict
$.users.data.cr59b4d8e3.name: str
$.users.data.cr59b4d8e3.user_id: str
$.users.data.cr59b4d8e3.address: str
$.users.data.cr59b4d8e3.email: str
$.users.data.cr59b4d8e3.phone_number: str
$.users.data.cr59b4d8e3.date_of_birth: str
$.users.data.jl72b4e9d1: dict
$.users.data.jl72b4e9d1.name: str
$.users.data.jl72b4e9d1.user_id: str
$.users.data.jl72b4e9d1.address: str
$.users.data.jl72b4e9d1.email: str
$.users.data.jl72b4e9d1.phone_number: str
$.users.data.jl72b4e9d1.date_of_birth: str
$.users.data.jl72b4e9d1.rho_bank_plus_subscription: bool
$.users.data.rp65a7b3c4: dict
$.users.data.rp65a7b3c4.name: str
$.users.data.rp65a7b3c4.user_id: str
$.users.data.rp65a7b3c4.address: str
$.users.data.rp65a7b3c4.email: str
$.users.data.rp65a7b3c4.phone_number: str
$.users.data.rp65a7b3c4.date_of_birth: str
$.users.data.yt71c9e4f2: dict
$.users.data.yt71c9e4f2.name: str
$.users.data.yt71c9e4f2.user_id: str
$.users.data.yt71c9e4f2.address: str
$.users.data.yt71c9e4f2.email: str
$.users.data.yt71c9e4f2.phone_number: str
$.users.data.yt71c9e4f2.date_of_birth: str
$.users.data.lj82d4f1a9: dict
$.users.data.lj82d4f1a9.name: str
$.users.data.lj82d4f1a9.user_id: str
$.users.data.lj82d4f1a9.address: str
$.users.data.lj82d4f1a9.email: str
$.users.data.lj82d4f1a9.phone_number: str
$.users.data.lj82d4f1a9.date_of_birth: str
$.users.data.kj93a7b2e1: dict
$.users.data.kj93a7b2e1.name: str
$.users.data.kj93a7b2e1.user_id: str
$.users.data.kj93a7b2e1.address: str
$.users.data.kj93a7b2e1.email: str
$.users.data.kj93a7b2e1.phone_number: str
$.users.data.kj93a7b2e1.date_of_birth: str
$.users.data.ar72c5d8e3: dict
$.users.data.ar72c5d8e3.name: str
$.users.data.ar72c5d8e3.user_id: str
$.users.data.ar72c5d8e3.address: str
$.users.data.ar72c5d8e3.email: str
$.users.data.ar72c5d8e3.phone_number: str
$.users.data.ar72c5d8e3.date_of_birth: str
$.users.data.mv93f8a7b2: dict
$.users.data.mv93f8a7b2.name: str
$.users.data.mv93f8a7b2.user_id: str
$.users.data.mv93f8a7b2.address: str
$.users.data.mv93f8a7b2.email: str
$.users.data.mv93f8a7b2.phone_number: str
$.users.data.mv93f8a7b2.date_of_birth: str
$.users.data.av96d4e7f1: dict
$.users.data.av96d4e7f1.name: str
$.users.data.av96d4e7f1.user_id: str
$.users.data.av96d4e7f1.address: str
$.users.data.av96d4e7f1.email: str
$.users.data.av96d4e7f1.phone_number: str
$.users.data.av96d4e7f1.date_of_birth: str
$.users.notes: str
$.accounts: dict
$.accounts.data: dict
$.accounts.data.01: dict
$.accounts.data.01.account_id: str
$.accounts.data.01.user_id: str
$.accounts.data.01.class: str
$.accounts.data.01.level: str
$.accounts.data.01.date_opened: str
$.accounts.data.01.status: str
$.accounts.data.01.current_holdings: str
$.accounts.data.02: dict
$.accounts.data.02.account_id: str
$.accounts.data.02.user_id: str
$.accounts.data.02.class: str
$.accounts.data.02.level: str
$.accounts.data.02.date_opened: str
$.accounts.data.02.status: str
$.accounts.data.02.current_holdings: str
$.accounts.data.03: dict
$.accounts.data.03.account_id: str
$.accounts.data.03.user_id: str
$.accounts.data.03.class: str
$.accounts.data.03.level: str
$.accounts.data.03.date_opened: str
$.accounts.data.03.status: str
$.accounts.data.03.current_holdings: str
$.accounts.data.04: dict
$.accounts.data.04.account_id: str
$.accounts.data.04.user_id: str
$.accounts.data.04.class: str
$.accounts.data.04.level: str
$.accounts.data.04.date_opened: str
$.accounts.data.04.status: str
$.accounts.data.04.current_holdings: str
$.accounts.data.05: dict
$.accounts.data.05.account_id: str
$.accounts.data.05.user_id: str
$.accounts.data.05.class: str
$.accounts.data.05.level: str
$.accounts.data.05.date_opened: str
$.accounts.data.05.status: str
$.accounts.data.05.current_holdings: str
$.accounts.data.06: dict
$.accounts.data.06.account_id: str
$.accounts.data.06.user_id: str
$.accounts.data.06.class: str
$.accounts.data.06.level: str
$.accounts.data.06.date_opened: str
$.accounts.data.06.status: str
$.accounts.data.06.current_holdings: str
$.accounts.data.07: dict
$.accounts.data.07.account_id: str
$.accounts.data.07.user_id: str
$.accounts.data.07.class: str
$.accounts.data.07.level: str
$.accounts.data.07.date_opened: str
$.accounts.data.07.status: str
$.accounts.data.07.current_holdings: str
$.accounts.data.08: dict
$.accounts.data.08.account_id: str
$.accounts.data.08.user_id: str
$.accounts.data.08.class: str
$.accounts.data.08.level: str
$.accounts.data.08.date_opened: str
$.accounts.data.08.status: str
$.accounts.data.08.current_holdings: str
$.accounts.data.chk_e9d195fe8e: dict
$.accounts.data.chk_e9d195fe8e.account_id: str
$.accounts.data.chk_e9d195fe8e.user_id: str
$.accounts.data.chk_e9d195fe8e.class: str
$.accounts.data.chk_e9d195fe8e.level: str
$.accounts.data.chk_e9d195fe8e.date_opened: str
$.accounts.data.chk_e9d195fe8e.status: str
$.accounts.data.chk_e9d195fe8e.current_holdings: str
$.accounts.data.chk_b5e8f2a1c9: dict
$.accounts.data.chk_b5e8f2a1c9.account_id: str
$.accounts.data.chk_b5e8f2a1c9.user_id: str
$.accounts.data.chk_b5e8f2a1c9.class: str
$.accounts.data.chk_b5e8f2a1c9.level: str
$.accounts.data.chk_b5e8f2a1c9.date_opened: str
$.accounts.data.chk_b5e8f2a1c9.status: str
$.accounts.data.chk_b5e8f2a1c9.current_holdings: str
$.accounts.data.biz_chk_b5e8f2a1c9: dict
$.accounts.data.biz_chk_b5e8f2a1c9.account_id: str
$.accounts.data.biz_chk_b5e8f2a1c9.user_id: str
$.accounts.data.biz_chk_b5e8f2a1c9.class: str
$.accounts.data.biz_chk_b5e8f2a1c9.level: str
$.accounts.data.biz_chk_b5e8f2a1c9.date_opened: str
$.accounts.data.biz_chk_b5e8f2a1c9.status: str
$.accounts.data.biz_chk_b5e8f2a1c9.current_holdings: str
$.accounts.data.chk_yt71c9e4f2: dict
$.accounts.data.chk_yt71c9e4f2.account_id: str
$.accounts.data.chk_yt71c9e4f2.user_id: str
$.accounts.data.chk_yt71c9e4f2.class: str
$.accounts.data.chk_yt71c9e4f2.level: str
$.accounts.data.chk_yt71c9e4f2.date_opened: str
$.accounts.data.chk_yt71c9e4f2.status: str
$.accounts.data.chk_yt71c9e4f2.current_holdings: str
$.accounts.data.biz_chk_yt71c9e4f2: dict
$.accounts.data.biz_chk_yt71c9e4f2.account_id: str
$.accounts.data.biz_chk_yt71c9e4f2.user_id: str
$.accounts.data.biz_chk_yt71c9e4f2.class: str
$.accounts.data.biz_chk_yt71c9e4f2.level: str
$.accounts.data.biz_chk_yt71c9e4f2.date_opened: str
$.accounts.data.biz_chk_yt71c9e4f2.status: str
$.accounts.data.biz_chk_yt71c9e4f2.current_holdings: str
$.accounts.data.58d57780cc15e32d: dict
$.accounts.data.58d57780cc15e32d.account_id: str
$.accounts.data.58d57780cc15e32d.user_id: str
$.accounts.data.58d57780cc15e32d.class: str
$.accounts.data.58d57780cc15e32d.level: str
$.accounts.data.58d57780cc15e32d.date_opened: str
$.accounts.data.58d57780cc15e32d.status: str
$.accounts.data.58d57780cc15e32d.current_holdings: str
$.accounts.data.38a2c5f77504be6c: dict
$.accounts.data.38a2c5f77504be6c.account_id: str
$.accounts.data.38a2c5f77504be6c.user_id: str
$.accounts.data.38a2c5f77504be6c.class: str
$.accounts.data.38a2c5f77504be6c.level: str
$.accounts.data.38a2c5f77504be6c.date_opened: str
$.accounts.data.38a2c5f77504be6c.status: str
$.accounts.data.38a2c5f77504be6c.current_holdings: str
... (+893 lines)
```
- sample: `samples/downloaded_domains_data__banking_knowledge__tau2_env__db.json` (62 KB)

## downloaded_domains_data/banking_knowledge/tau2_env/documents/doc_bank_accounts_bank_accounts_(general)_001.json (в папке 698 файлов *.json; взяты первые 2)

Размер: 0.8 КБ
Тип: JSON dict (len=3)
Схема:
```
$: dict
$.id: str
$.title: str
$.content: str
```
- sample: `samples/downloaded_domains_data__banking_knowledge__tau2_env__documents__doc_bank_accounts_bank_accounts___general___001.json` (0 KB)

## downloaded_domains_data/banking_knowledge/tau2_env/documents/doc_bank_accounts_bank_accounts_(general)_002.json (в папке 698 файлов *.json; взяты первые 2)

Размер: 4.8 КБ
Тип: JSON dict (len=3)
Схема:
```
$: dict
$.id: str
$.title: str
$.content: str
```
- sample: `samples/downloaded_domains_data__banking_knowledge__tau2_env__documents__doc_bank_accounts_bank_accounts___general___002.json` (2 KB)

## downloaded_domains_data/banking_knowledge/tau2_env/prompts/agentic_search.md (в папке 14 файлов *.md; взяты первые 2)

Размер: 0.1 КБ
Тип: текст, 101 символов, 6 строк
- head: `samples/downloaded_domains_data__banking_knowledge__tau2_env__prompts__agentic_search.md.txt`

## downloaded_domains_data/banking_knowledge/tau2_env/prompts/agentic_search_write.md (в папке 14 файлов *.md; взяты первые 2)

Размер: 2.9 КБ
Тип: текст, 2930 символов, 74 строк
- head: `samples/downloaded_domains_data__banking_knowledge__tau2_env__prompts__agentic_search_write.md.txt`

## downloaded_domains_data/banking_knowledge/tau2_env/prompts/components/additional_instructions.md

Размер: 3.7 КБ
Тип: текст, 3816 символов, 44 строк
- head: `samples/downloaded_domains_data__banking_knowledge__tau2_env__prompts__components__additional_instructions.md.txt`

## downloaded_domains_data/banking_knowledge/tau2_env/prompts/components/policy_header.md

Размер: 1.7 КБ
Тип: текст, 1779 символов, 15 строк
- head: `samples/downloaded_domains_data__banking_knowledge__tau2_env__prompts__components__policy_header.md.txt`

## downloaded_domains_data/banking_knowledge/tau2_env/prompts/components/shell_instructions.md

Размер: 1.4 КБ
Тип: текст, 1468 символов, 44 строк
- head: `samples/downloaded_domains_data__banking_knowledge__tau2_env__prompts__components__shell_instructions.md.txt`

## downloaded_domains_data/banking_knowledge/tau2_env/tasks/task_001.json (в папке 97 файлов *.json; взяты первые 2)

Размер: 2.5 КБ
Тип: JSON dict (len=8)
Схема:
```
$: dict
$.id: str
$.description: dict
$.description.purpose: str
$.description.relevant_policies: NoneType
$.description.notes: NoneType
$.user_scenario: dict
$.user_scenario.persona: NoneType
$.user_scenario.instructions: str
$.initial_state: NoneType
$.evaluation_criteria: dict
$.evaluation_criteria.actions: len~1 | list
$.evaluation_criteria.actions[]: dict
$.evaluation_criteria.actions[].name: str
$.evaluation_criteria.actions[].arguments: dict
$.evaluation_criteria.actions[].arguments.card_type: str
$.evaluation_criteria.actions[].arguments.customer_name: str
$.evaluation_criteria.actions[].arguments.annual_income: int
$.evaluation_criteria.actions[].arguments.rho_bank_subscription: bool
$.evaluation_criteria.actions[].requestor: str
$.evaluation_criteria.actions[].action_id: str
$.evaluation_criteria.communicate_info: len~0 | list
$.evaluation_criteria.reward_basis: len~1 | list
$.evaluation_criteria.reward_basis[]: str
$.annotations: NoneType
$.user_tools: len~1 | list
$.user_tools[]: str
$.required_documents: len~4 | list
$.required_documents[]: str
```
- sample: `samples/downloaded_domains_data__banking_knowledge__tau2_env__tasks__task_001.json` (2 KB)

## downloaded_domains_data/banking_knowledge/tau2_env/tasks/task_002.json (в папке 97 файлов *.json; взяты первые 2)

Размер: 2.7 КБ
Тип: JSON dict (len=8)
Схема:
```
$: dict
$.id: str
$.description: dict
$.description.purpose: str
$.description.relevant_policies: NoneType
$.description.notes: NoneType
$.user_scenario: dict
$.user_scenario.persona: NoneType
$.user_scenario.instructions: str
$.initial_state: NoneType
$.evaluation_criteria: dict
$.evaluation_criteria.actions: len~1 | list
$.evaluation_criteria.actions[]: dict
$.evaluation_criteria.actions[].name: str
$.evaluation_criteria.actions[].arguments: dict
$.evaluation_criteria.actions[].arguments.card_type: str
$.evaluation_criteria.actions[].arguments.customer_name: str
$.evaluation_criteria.actions[].arguments.annual_income: int
$.evaluation_criteria.actions[].arguments.rho_bank_subscription: bool
$.evaluation_criteria.actions[].requestor: str
$.evaluation_criteria.actions[].action_id: str
$.evaluation_criteria.communicate_info: len~0 | list
$.evaluation_criteria.reward_basis: len~1 | list
$.evaluation_criteria.reward_basis[]: str
$.annotations: NoneType
$.user_tools: len~1 | list
$.user_tools[]: str
$.required_documents: len~6 | list
$.required_documents[]: str
```
- sample: `samples/downloaded_domains_data__banking_knowledge__tau2_env__tasks__task_002.json` (2 KB)

## downloaded_domains_data/banking_knowledge/tau2_env/tasks.json

Размер: 1111.5 КБ
Тип: JSON list (len=97)
Схема:
```
$: len~97 | list
$[]: dict
$[].id: str
$[].description: dict
$[].description.purpose: str
$[].description.relevant_policies: NoneType
$[].description.notes: NoneType | str
$[].user_scenario: dict
$[].user_scenario.persona: NoneType
$[].user_scenario.instructions: str
$[].initial_state: NoneType | dict
$[].evaluation_criteria: dict
$[].evaluation_criteria.actions: len~1 | len~10 | len~11 | len~12 | len~15 | len~16 | len~2 | len~25 | len~3 | len~4 | len~5 | len~6 | len~8 | len~9 | list
$[].evaluation_criteria.actions[]: dict
$[].evaluation_criteria.actions[].name: str
$[].evaluation_criteria.actions[].arguments: dict
$[].evaluation_criteria.actions[].arguments.card_type: str
$[].evaluation_criteria.actions[].arguments.customer_name: str
$[].evaluation_criteria.actions[].arguments.annual_income: int
$[].evaluation_criteria.actions[].arguments.rho_bank_subscription: bool
$[].evaluation_criteria.actions[].requestor: str
$[].evaluation_criteria.actions[].action_id: str
$[].evaluation_criteria.communicate_info: len~0 | list
$[].evaluation_criteria.reward_basis: len~1 | list
$[].evaluation_criteria.reward_basis[]: str
$[].annotations: NoneType
$[].user_tools: len~1 | len~2 | list
$[].user_tools[]: str
$[].required_documents: len~1 | len~10 | len~11 | len~13 | len~2 | len~3 | len~4 | len~5 | len~6 | len~7 | len~8 | list
$[].required_documents[]: str
$[].evaluation_criteria.actions[].arguments.reason: str
$[].evaluation_criteria.actions[].arguments.summary: str
$[].evaluation_criteria.actions[].compare_args: len~0 | len~1 | len~2 | len~6 | list
$[].evaluation_criteria.actions[].compare_args[]: str
$[].evaluation_criteria.actions[].arguments.name: str
$[].evaluation_criteria.actions[].arguments.user_id: str
$[].evaluation_criteria.actions[].arguments.address: str
$[].evaluation_criteria.actions[].arguments.email: str
$[].evaluation_criteria.actions[].arguments.phone_number: str
$[].evaluation_criteria.actions[].arguments.date_of_birth: str
$[].evaluation_criteria.actions[].arguments.time_verified: str
$[].evaluation_criteria.actions[].arguments.new_email: str
$[].evaluation_criteria.actions[].arguments.account_type: str
$[].evaluation_criteria.actions[].arguments.discoverable_tool_name: str
$[].evaluation_criteria.actions[].arguments.arguments: str
$[].evaluation_criteria.actions[].arguments.credit_card_type: str
$[].evaluation_criteria.actions[].arguments.merchant_name: str
$[].evaluation_criteria.actions[].arguments.amount: int
$[].evaluation_criteria.actions[].arguments.category: str
$[].initial_state.initialization_data: dict
$[].initial_state.initialization_data.agent_data: NoneType | dict
$[].initial_state.initialization_data.agent_data.task_config: dict
$[].initial_state.initialization_data.agent_data.task_config.data: dict
$[].initial_state.initialization_data.agent_data.task_config.data.dispute_settings: dict
$[].initial_state.initialization_data.agent_data.task_config.data.dispute_settings.auto_resolve_disputes: bool
$[].initial_state.initialization_data.user_data: NoneType
$[].initial_state.initialization_actions: NoneType
$[].initial_state.message_history: NoneType
$[].evaluation_criteria.actions[].arguments.agent_tool_name: str
$[].initial_state.initialization_data.agent_data.transaction_disputes: dict
$[].initial_state.initialization_data.agent_data.transaction_disputes.data: dict
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038: dict
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.dispute_id: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.transaction_id: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.user_id: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.card_action: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.card_last_4_digits: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.full_name: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.phone: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.email: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.address: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.contacted_merchant: bool
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.purchase_date: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.issue_noticed_date: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.dispute_reason: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.resolution_requested: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.partial_refund_amount: NoneType
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.eligible_for_provisional_credit: bool
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.provisional_credit_given: bool
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.submitted_at: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_ed3ab3dce038.status: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198: dict
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.dispute_id: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.transaction_id: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.user_id: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.card_action: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.card_last_4_digits: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.full_name: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.phone: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.email: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.address: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.contacted_merchant: bool
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.purchase_date: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.issue_noticed_date: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.dispute_reason: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.resolution_requested: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.partial_refund_amount: NoneType
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.eligible_for_provisional_credit: bool
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.provisional_credit_given: bool
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.submitted_at: str
$[].initial_state.initialization_data.agent_data.transaction_disputes.data.dsp_dfab0685d198.status: str
```
- sample: `samples/downloaded_domains_data__banking_knowledge__tau2_env__tasks.json` (5 KB)

## downloaded_domains_data/banking_knowledge/tau2_env/tools.py

Размер: 184.8 КБ
Тип: текст, 189255 символов, 4761 строк
Определения (87): _parse_balance, _get_account_balance, parse_discoverable_tool_docstring, format_discoverable_tool_for_agent, _validate_pin, _validate_activation_common, KnowledgeTools, __init__, set_read_log_allowlist, get_user_discoverable_tools_state, get_agent_discoverable_tools_state, transfer_to_human_agents, get_current_time, get_user_information_by_id, get_user_information_by_name, get_user_information_by_email, change_user_email, get_referrals_by_user, get_credit_card_transactions_by_user, get_credit_card_accounts_by_user, log_verification, give_discoverable_user_tool, unlock_discoverable_agent_tool, call_discoverable_agent_tool, list_discoverable_agent_tools, example_agent_tool_0000, update_transaction_rewards_3847, initial_transfer_to_human_agent_0218, initial_transfer_to_human_agent_1822, emergency_credit_bureau_incident_transfer_1114, file_credit_card_transaction_dispute_4829, file_debit_card_transaction_dispute_6281, set_debit_card_recurring_block_7382, get_debit_dispute_status_7483, get_atm_deposit_images_8473, order_replacement_credit_card_7291, get_user_dispute_history_7291, get_pending_replacement_orders_5765, log_credit_card_closure_reason_4521, get_closure_reason_history_8293, apply_statement_credit_8472, apply_credit_card_account_flag_6147, close_credit_card_account_7834, pay_credit_card_from_checking_9182, submit_credit_limit_increase_request_7392, get_credit_limit_increase_history_4829, get_payment_history_6183, approve_credit_limit_increase_5847, deny_credit_limit_increase_5848, open_bank_account_4821, get_account_age_days, close_bank_account_7392, get_all_user_accounts_by_user_id_3847, transfer_funds_between_bank_accounts_7291, apply_checking_account_credit_5829, apply_savings_account_credit_6831, submit_interest_discrepancy_report_7294, get_bank_account_transactions_9173, txn_sort_key, order_debit_card_5739, activate_debit_card_8291, activate_debit_card_8292, activate_debit_card_8293, close_debit_card_4721, freeze_debit_card_3892, unfreeze_debit_card_3893, clear_debit_card_fraud_alert_4892, reset_debit_card_pin_6284, change_debit_card_pin_6285, get_debit_cards_by_account_id_7823, request_temporary_debit_card_limit_increase_8374, KnowledgeUserTools, __init__, _check_tool_given, _log_user_tool_call, submit_cash_back_dispute_0589, get_referral_link, get_card_last_4_digits, deposit_check_3847, parse_balance
- head: `samples/downloaded_domains_data__banking_knowledge__tau2_env__tools.py.txt`

## downloaded_domains_data/downloaded_domains_data/airline/secondary_source/CLEANING_SUMMARY.md

Размер: 4.9 КБ
Тип: текст, 3577 символов, 129 строк
- head: `samples/downloaded_domains_data__downloaded_domains_data__airline__secondary_source__CLEANING_SUMMARY.md.txt`

## downloaded_domains_data/downloaded_domains_data/airline/secondary_source/README.md

Размер: 19.7 КБ
Тип: текст, 20139 символов, 427 строк
- head: `samples/downloaded_domains_data__downloaded_domains_data__airline__secondary_source__README.md.txt`

## downloaded_domains_data/downloaded_domains_data/airline/secondary_source/REAL_KEYS_ONLY_AUDIT.md

Размер: 10.7 КБ
Тип: текст, 10791 символов, 97 строк
- head: `samples/downloaded_domains_data__downloaded_domains_data__airline__secondary_source__REAL_KEYS_ONLY_AUDIT.md.txt`

## downloaded_domains_data/downloaded_domains_data/airline/secondary_source/removal_log.json (в папке 7 файлов *.json; взяты первые 2)

Размер: 0.9 КБ
Тип: JSON dict (len=6)
Схема:
```
$: dict
$.original_total: int
$.round1_removed: dict
$.round1_removed.count: int
$.round1_removed.criteria: len~3 | list
$.round1_removed.criteria[]: str
$.round1_removed.note: str
$.round2_removed: dict
$.round2_removed.count: int
$.round2_removed.criteria: len~1 | list
$.round2_removed.criteria[]: str
$.round2_removed.saved_to: str
$.final_total: int
$.breakdown: dict
$.breakdown.tau2bench: int
$.breakdown.swebench: int
$.breakdown.terminalbench: int
$.breakdown.mathhay: int
$.breakdown.search: int
$.breakdown.mcpbench: int
$.round3_removed: dict
$.round3_removed.count: int
$.round3_removed.criteria: str
$.round3_removed.saved_to: str
```
- sample: `samples/downloaded_domains_data__downloaded_domains_data__airline__secondary_source__removal_log.json` (0 KB)

## downloaded_domains_data/downloaded_domains_data/airline/secondary_source/tau2bench.jsonl

Размер: 65510.0 КБ
Тип: JSONL; прочитано строк: 984 (битых: 0, лимит 20000)
Схема (объединение по первым записям):
```
$: dict
$.id: str
$.benchmark: str
$.domain: str
$.task_id: str
$.source_model: str
$.pass: int
$.messages: len~10 | len~11 | len~12 | len~127 | len~13 | len~14 | len~15 | len~16 | len~17 | len~18 | len~19 | len~20 | len~21 | len~22 | len~23 | len~24 | len~25 | len~26 | len~27 | len~28 | len~29 | len~30 | len~31 | len~32 | len~33 | len~34 | len~35 | len~36 | len~37 | len~38 | len~39 | len~4 | len~40 | len~41 | len~42 | len~44 | len~45 | len~46 | len~47 | len~48 | len~49 | len~50 | len~52 | len~53 | len~55 | len~59 | len~6 | len~61 | len~67 | len~70 | len~72 | len~77 | len~8 | len~81 | list
$.messages[]: dict
$.messages[].role: str
$.messages[].content: str
$.messages[].tool_calls: len~1 | len~12 | len~2 | len~3 | len~4 | len~5 | len~6 | len~7 | list
$.messages[].tool_calls[]: dict
$.messages[].tool_calls[].id: str
$.messages[].tool_calls[].type: str
$.messages[].tool_calls[].function: dict
$.messages[].tool_calls[].function.name: str
$.messages[].tool_calls[].function.arguments: str
$.messages[].tool_call_id: str
$.messages[].name: str
$.num_turns: int
$.reward: float
$.eval_details: dict
$.eval_details.id: str
$.eval_details.task_id: str
$.eval_details.timestamp: str
$.eval_details.start_time: str
$.eval_details.end_time: str
$.eval_details.duration: float
$.eval_details.termination_reason: str
$.eval_details.agent_cost: float
$.eval_details.user_cost: float
$.eval_details.reward_info: dict
$.eval_details.reward_info.reward: float
$.eval_details.reward_info.db_check: dict
$.eval_details.reward_info.db_check.db_match: bool
$.eval_details.reward_info.db_check.db_reward: float
$.eval_details.reward_info.env_assertions: len~0 | len~1 | len~2 | len~3 | list
$.eval_details.reward_info.action_checks: NoneType | len~0 | len~1 | len~10 | len~11 | len~12 | len~13 | len~2 | len~3 | len~4 | len~5 | len~6 | len~7 | len~8 | len~9 | list
$.eval_details.reward_info.nl_assertions: len~0 | list
$.eval_details.reward_info.communicate_checks: NoneType | len~1 | len~2 | len~3 | list
$.eval_details.reward_info.reward_basis: len~0 | list
$.eval_details.reward_info.reward_breakdown: dict
$.eval_details.reward_info.reward_breakdown.DB: float
$.eval_details.reward_info.reward_breakdown.COMMUNICATE: float
$.eval_details.reward_info.info: dict
$.eval_details.trial: int
$.eval_details.seed: int
$.eval_details.model_name: str
$.eval_details.domain: str
$.trace_meta: dict
$.trace_meta.benchmark: str
$.trace_meta.domain: str
$.trace_meta.task_id: str
$.trace_meta.total_steps: int
$.trace_meta.error: NoneType
$.trace_meta.trace: dict
$.trace_meta.trace.task_id: str
$.trace_meta.trace.steps: len~10 | len~12 | len~128 | len~14 | len~16 | len~18 | len~20 | len~22 | len~24 | len~26 | len~28 | len~30 | len~32 | len~34 | len~36 | len~38 | len~4 | len~40 | len~42 | len~44 | len~48 | len~50 | len~52 | len~6 | len~60 | len~62 | len~64 | len~72 | len~8 | list
$.trace_meta.trace.steps[]: dict
$.trace_meta.trace.steps[].step: int
$.trace_meta.trace.steps[].timestamp: str
$.trace_meta.trace.steps[].message_type: str
$.trace_meta.trace.steps[].content: NoneType | str
$.trace_meta.trace.steps[].tool_name: NoneType | str
$.trace_meta.trace.steps[].tool_arguments: NoneType | dict
$.trace_meta.trace.steps[].tool_result: NoneType | str
$.trace_meta.trace.steps[].tool_error: bool
$.trace_meta.trace.steps[].tool_arguments.reservation_id: str
$.trace_meta.trace.steps[].tool_arguments.user_id: str
$.trace_meta.trace.rounds: len~1 | len~10 | len~11 | len~12 | len~13 | len~14 | len~15 | len~16 | len~17 | len~18 | len~19 | len~2 | len~20 | len~21 | len~23 | len~24 | len~25 | len~26 | len~29 | len~3 | len~30 | len~31 | len~4 | len~5 | len~6 | len~62 | len~7 | len~8 | len~9 | list
$.trace_meta.trace.rounds[]: dict
$.trace_meta.trace.rounds[].round_number: int
$.trace_meta.trace.rounds[].reasoning: str
$.trace_meta.trace.rounds[].should_continue: bool
$.trace_meta.trace.rounds[].prompt_tokens: int
$.trace_meta.trace.rounds[].output_tokens: int
$.trace_meta.trace.rounds[].round_total_tokens: int
$.trace_meta.trace.rounds[].cumulative_total_tokens: int
$.trace_meta.trace.rounds[].incremental_tokens: int
$.trace_meta.trace.rounds[].tools_executed: int
$.trace_meta.trace.rounds[].executions: len~0 | list
$.trace_meta.trace.final_response: str
$.trace_meta.trace.total_steps: int
$.trace_meta.trace.error: NoneType
$.trace_meta.trace.start_time: str
$.trace_meta.trace.end_time: str
$.trace_meta.trace.duration: float
$.trace_meta.trace.total_prompt_tokens: int
$.trace_meta.trace.total_output_tokens: int
$.trace_meta.trace.total_tokens: int
$.tool_registry: dict
$.tool_registry.scope: str
$.tool_registry.source_repo: str
$.tool_registry.construction_method: str
$.tool_registry.server_names: len~1 | list
$.tool_registry.server_names[]: str
$.tool_registry.tools: len~13 | len~14 | len~15 | list
$.tool_registry.tools[]: dict
$.tool_registry.tools[].name: str
$.tool_registry.tools[].source_server: str
$.tool_registry.tools[].description: str
$.tool_registry.tools[].parameters: dict
$.tool_registry.tools[].parameters.$defs: dict
$.tool_registry.tools[].parameters.$defs.FlightInfo: dict
$.tool_registry.tools[].parameters.$defs.FlightInfo.properties: dict
$.tool_registry.tools[].parameters.$defs.FlightInfo.properties.flight_number: dict
$.tool_registry.tools[].parameters.$defs.FlightInfo.properties.date: dict
$.tool_registry.tools[].parameters.$defs.FlightInfo.required: len~2 | list
$.tool_registry.tools[].parameters.$defs.FlightInfo.required[]: str
$.tool_registry.tools[].parameters.$defs.FlightInfo.title: str
$.tool_registry.tools[].parameters.$defs.FlightInfo.type: str
$.tool_registry.tools[].parameters.$defs.Passenger: dict
$.tool_registry.tools[].parameters.$defs.Passenger.properties: dict
$.tool_registry.tools[].parameters.$defs.Passenger.properties.first_name: dict
$.tool_registry.tools[].parameters.$defs.Passenger.properties.last_name: dict
$.tool_registry.tools[].parameters.$defs.Passenger.properties.dob: dict
$.tool_registry.tools[].parameters.$defs.Passenger.required: len~3 | list
$.tool_registry.tools[].parameters.$defs.Passenger.required[]: str
$.tool_registry.tools[].parameters.$defs.Passenger.title: str
$.tool_registry.tools[].parameters.$defs.Passenger.type: str
$.tool_registry.tools[].parameters.$defs.Payment: dict
$.tool_registry.tools[].parameters.$defs.Payment.properties: dict
$.tool_registry.tools[].parameters.$defs.Payment.properties.payment_id: dict
$.tool_registry.tools[].parameters.$defs.Payment.properties.amount: dict
$.tool_registry.tools[].parameters.$defs.Payment.required: len~2 | list
$.tool_registry.tools[].parameters.$defs.Payment.required[]: str
$.tool_registry.tools[].parameters.$defs.Payment.title: str
$.tool_registry.tools[].parameters.$defs.Payment.type: str
$.tool_registry.tools[].parameters.properties: dict
$.tool_registry.tools[].parameters.properties.user_id: dict
$.tool_registry.tools[].parameters.properties.user_id.description: str
$.tool_registry.tools[].parameters.properties.user_id.title: str
$.tool_registry.tools[].parameters.properties.user_id.type: str
$.tool_registry.tools[].parameters.properties.origin: dict
$.tool_registry.tools[].parameters.properties.origin.description: str
$.tool_registry.tools[].parameters.properties.origin.title: str
$.tool_registry.tools[].parameters.properties.origin.type: str
$.tool_registry.tools[].parameters.properties.destination: dict
$.tool_registry.tools[].parameters.properties.destination.description: str
$.tool_registry.tools[].parameters.properties.destination.title: str
$.tool_registry.tools[].parameters.properties.destination.type: str
$.tool_registry.tools[].parameters.properties.flight_type: dict
$.tool_registry.tools[].parameters.properties.flight_type.description: str
$.tool_registry.tools[].parameters.properties.flight_type.enum: len~2 | list
$.tool_registry.tools[].parameters.properties.flight_type.enum[]: str
$.tool_registry.tools[].parameters.properties.flight_type.title: str
$.tool_registry.tools[].parameters.properties.flight_type.type: str
$.tool_registry.tools[].parameters.properties.cabin: dict
$.tool_registry.tools[].parameters.properties.cabin.description: str
$.tool_registry.tools[].parameters.properties.cabin.enum: len~3 | list
$.tool_registry.tools[].parameters.properties.cabin.enum[]: str
$.tool_registry.tools[].parameters.properties.cabin.title: str
$.tool_registry.tools[].parameters.properties.cabin.type: str
$.tool_registry.tools[].parameters.properties.flights: dict
$.tool_registry.tools[].parameters.properties.flights.description: str
$.tool_registry.tools[].parameters.properties.flights.items: dict
$.tool_registry.tools[].parameters.properties.flights.items.anyOf: list
$.tool_registry.tools[].parameters.properties.flights.title: str
$.tool_registry.tools[].parameters.properties.flights.type: str
$.tool_registry.tools[].parameters.properties.passengers: dict
$.tool_registry.tools[].parameters.properties.passengers.description: str
$.tool_registry.tools[].parameters.properties.passengers.items: dict
$.tool_registry.tools[].parameters.properties.passengers.items.anyOf: list
$.tool_registry.tools[].parameters.properties.passengers.title: str
$.tool_registry.tools[].parameters.properties.passengers.type: str
$.tool_registry.tools[].parameters.properties.payment_methods: dict
$.tool_registry.tools[].parameters.properties.payment_methods.description: str
$.tool_registry.tools[].parameters.properties.payment_methods.items: dict
$.tool_registry.tools[].parameters.properties.payment_methods.items.anyOf: list
$.tool_registry.tools[].parameters.properties.payment_methods.title: str
$.tool_registry.tools[].parameters.properties.payment_methods.type: str
$.tool_registry.tools[].parameters.properties.total_baggages: dict
$.tool_registry.tools[].parameters.properties.total_baggages.description: str
$.tool_registry.tools[].parameters.properties.total_baggages.title: str
$.tool_registry.tools[].parameters.properties.total_baggages.type: str
$.tool_registry.tools[].parameters.properties.nonfree_baggages: dict
$.tool_registry.tools[].parameters.properties.nonfree_baggages.description: str
$.tool_registry.tools[].parameters.properties.nonfree_baggages.title: str
$.tool_registry.tools[].parameters.properties.nonfree_baggages.type: str
$.tool_registry.tools[].parameters.properties.insurance: dict
$.tool_registry.tools[].parameters.properties.insurance.description: str
$.tool_registry.tools[].parameters.properties.insurance.enum: len~2 | list
$.tool_registry.tools[].parameters.properties.insurance.enum[]: str
$.tool_registry.tools[].parameters.properties.insurance.title: str
$.tool_registry.tools[].parameters.properties.insurance.type: str
$.tool_registry.tools[].parameters.required: len~1 | len~11 | len~2 | len~3 | len~4 | len~7 | list
$.tool_registry.tools[].parameters.required[]: str
$.tool_registry.tools[].parameters.title: str
$.tool_registry.tools[].parameters.type: str
$.tool_registry.tools[].parameters.properties.expression: dict
$.tool_registry.tools[].parameters.properties.expression.description: str
$.tool_registry.tools[].parameters.properties.expression.title: str
$.tool_registry.tools[].parameters.properties.expression.type: str
$.tool_registry.tools[].parameters.properties.reservation_id: dict
$.tool_registry.tools[].parameters.properties.reservation_id.description: str
$.tool_registry.tools[].parameters.properties.reservation_id.title: str
$.tool_registry.tools[].parameters.properties.reservation_id.type: str
$.tool_registry.tools[].parameters.properties.flight_number: dict
$.tool_registry.tools[].parameters.properties.flight_number.description: str
$.tool_registry.tools[].parameters.properties.flight_number.title: str
$.tool_registry.tools[].parameters.properties.flight_number.type: str
$.tool_registry.tools[].parameters.properties.date: dict
$.tool_registry.tools[].parameters.properties.date.description: str
$.tool_registry.tools[].parameters.properties.date.title: str
$.tool_registry.tools[].parameters.properties.date.type: str
$.tool_registry.tools[].parameters.properties.amount: dict
$.tool_registry.tools[].parameters.properties.amount.description: str
$.tool_registry.tools[].parameters.properties.amount.title: str
$.tool_registry.tools[].parameters.properties.amount.type: str
$.tool_registry.tools[].parameters.properties.summary: dict
$.tool_registry.tools[].parameters.properties.summary.description: str
$.tool_registry.tools[].parameters.properties.summary.title: str
$.tool_registry.tools[].parameters.properties.summary.type: str
$.tool_registry.tools[].parameters.properties.payment_id: dict
$.tool_registry.tools[].parameters.properties.payment_id.description: str
$.tool_registry.tools[].parameters.properties.payment_id.title: str
$.tool_registry.tools[].parameters.properties.payment_id.type: str
$.cleaning_info: NoneType | len~1 | len~2 | len~3 | list
$.num_passes_available: int
$.has_all_4_passes: bool
$.eval_details.reward_info.action_checks[]: dict
$.eval_details.reward_info.action_checks[].action: dict
$.eval_details.reward_info.action_checks[].action.action_id: str
$.eval_details.reward_info.action_checks[].action.requestor: str
$.eval_details.reward_info.action_checks[].action.name: str
$.eval_details.reward_info.action_checks[].action.arguments: dict
$.eval_details.reward_info.action_checks[].action.arguments.summary: str
$.eval_details.reward_info.action_checks[].action.info: NoneType
$.eval_details.reward_info.action_checks[].action.compare_args: NoneType | len~0 | list
$.eval_details.reward_info.action_checks[].action_match: bool
$.eval_details.reward_info.action_checks[].action_reward: float
$.eval_details.reward_info.action_checks[].action.arguments.reservation_id: str
$.eval_details.reward_info.action_checks[].action.arguments.user_id: str
$.eval_details.reward_info.action_checks[].action.arguments.origin: str
$.eval_details.reward_info.action_checks[].action.arguments.destination: str
$.eval_details.reward_info.action_checks[].action.arguments.flight_type: str
$.eval_details.reward_info.action_checks[].action.arguments.cabin: str
$.eval_details.reward_info.action_checks[].action.arguments.flights: len~1 | len~2 | len~3 | len~4 | list
$.eval_details.reward_info.action_checks[].action.arguments.flights[]: dict
$.eval_details.reward_info.action_checks[].action.arguments.passengers: len~1 | len~2 | len~3 | list
$.eval_details.reward_info.action_checks[].action.arguments.passengers[]: dict
$.eval_details.reward_info.action_checks[].action.arguments.payment_methods: len~1 | len~2 | len~4 | list
$.eval_details.reward_info.action_checks[].action.arguments.payment_methods[]: dict
$.eval_details.reward_info.action_checks[].action.arguments.total_baggages: int
$.eval_details.reward_info.action_checks[].action.arguments.nonfree_baggages: int
$.eval_details.reward_info.action_checks[].action.arguments.insurance: str
$.eval_details.reward_info.communicate_checks[]: dict
$.eval_details.reward_info.communicate_checks[].info: str
$.eval_details.reward_info.communicate_checks[].met: bool
$.eval_details.reward_info.communicate_checks[].justification: str
$.trace_meta.trace.steps[].tool_arguments.amount: int
$.cleaning_info[]: dict
$.cleaning_info[].message_index: int
$.cleaning_info[].role: str
$.cleaning_info[].removals: len~1 | len~2 | len~3 | len~4 | len~9 | list
$.cleaning_info[].removals[]: dict
$.cleaning_info[].removals[].type: str
$.cleaning_info[].removals[].start: int
$.cleaning_info[].removals[].end: int
$.cleaning_info[].removals[].length: int
$.cleaning_info[].original_length: int
$.cleaning_info[].cleaned_length: int
$.eval_details.reward_info.action_checks[].action.arguments.date: str
$.trace_meta.trace.steps[].tool_arguments.origin: str
$.trace_meta.trace.steps[].tool_arguments.destination: str
$.trace_meta.trace.steps[].tool_arguments.date: str
$.trace_meta.trace.steps[].tool_arguments.flight_type: str
$.trace_meta.trace.steps[].tool_arguments.cabin: str
$.trace_meta.trace.steps[].tool_arguments.flights: len~1 | len~2 | len~3 | len~4 | list
$.trace_meta.trace.steps[].tool_arguments.flights[]: dict | str
$.trace_meta.trace.steps[].tool_arguments.flights[].flight_number: str
$.trace_meta.trace.steps[].tool_arguments.flights[].origin: str
$.trace_meta.trace.steps[].tool_arguments.flights[].destination: str
$.trace_meta.trace.steps[].tool_arguments.flights[].date: str
$.trace_meta.trace.steps[].tool_arguments.passengers: len~1 | len~2 | len~3 | list
$.trace_meta.trace.steps[].tool_arguments.passengers[]: dict
$.trace_meta.trace.steps[].tool_arguments.passengers[].first_name: str
$.trace_meta.trace.steps[].tool_arguments.passengers[].last_name: str
$.trace_meta.trace.steps[].tool_arguments.passengers[].dob: str
$.trace_meta.trace.steps[].tool_arguments.payment_methods: len~1 | len~2 | len~4 | len~5 | list
$.trace_meta.trace.steps[].tool_arguments.payment_methods[]: dict | str
$.trace_meta.trace.steps[].tool_arguments.payment_methods[].source: str
$.trace_meta.trace.steps[].tool_arguments.payment_methods[].id: str
$.trace_meta.trace.steps[].tool_arguments.payment_methods[].amount: float | int
$.trace_meta.trace.steps[].tool_arguments.total_baggages: int
$.trace_meta.trace.steps[].tool_arguments.nonfree_baggages: int
$.trace_meta.trace.steps[].tool_arguments.insurance: str
$.trace_meta.trace.steps[].tool_arguments.payment_methods[].payment_id: str
$.eval_details.reward_info.action_checks[].action.arguments.first_name: str
$.eval_details.reward_info.action_checks[].action.arguments.last_name: str
$.eval_details.reward_info.action_checks[].action.arguments.zip: str
$.eval_details.reward_info.action_checks[].action.arguments.order_id: str
$.eval_details.reward_info.action_checks[].action.arguments.product_id: str
$.eval_details.reward_info.action_checks[].action.arguments.item_ids: len~1 | len~2 | len~3 | len~4 | list
$.eval_details.reward_info.action_checks[].action.arguments.item_ids[]: str
$.eval_details.reward_info.action_checks[].action.arguments.new_item_ids: len~1 | len~2 | list
$.eval_details.reward_info.action_checks[].action.arguments.new_item_ids[]: str
$.eval_details.reward_info.action_checks[].action.arguments.payment_method_id: str
$.tool_registry.tools[].parameters.properties.order_id: dict
$.tool_registry.tools[].parameters.properties.order_id.description: str
$.tool_registry.tools[].parameters.properties.order_id.title: str
$.tool_registry.tools[].parameters.properties.order_id.type: str
$.tool_registry.tools[].parameters.properties.reason: dict
$.tool_registry.tools[].parameters.properties.reason.description: str
$.tool_registry.tools[].parameters.properties.reason.title: str
$.tool_registry.tools[].parameters.properties.reason.type: str
$.tool_registry.tools[].parameters.properties.item_ids: dict
$.tool_registry.tools[].parameters.properties.item_ids.description: str
$.tool_registry.tools[].parameters.properties.item_ids.items: dict
$.tool_registry.tools[].parameters.properties.item_ids.items.type: str
$.tool_registry.tools[].parameters.properties.item_ids.title: str
$.tool_registry.tools[].parameters.properties.item_ids.type: str
$.tool_registry.tools[].parameters.properties.new_item_ids: dict
$.tool_registry.tools[].parameters.properties.new_item_ids.description: str
$.tool_registry.tools[].parameters.properties.new_item_ids.items: dict
$.tool_registry.tools[].parameters.properties.new_item_ids.items.type: str
$.tool_registry.tools[].parameters.properties.new_item_ids.title: str
$.tool_registry.tools[].parameters.properties.new_item_ids.type: str
$.tool_registry.tools[].parameters.properties.payment_method_id: dict
$.tool_registry.tools[].parameters.properties.payment_method_id.description: str
$.tool_registry.tools[].parameters.properties.payment_method_id.title: str
$.tool_registry.tools[].parameters.properties.payment_method_id.type: str
$.tool_registry.tools[].parameters.properties.email: dict
$.tool_registry.tools[].parameters.properties.email.description: str
$.tool_registry.tools[].parameters.properties.email.title: str
$.tool_registry.tools[].parameters.properties.email.type: str
$.tool_registry.tools[].parameters.properties.first_name: dict
$.tool_registry.tools[].parameters.properties.first_name.description: str
$.tool_registry.tools[].parameters.properties.first_name.title: str
$.tool_registry.tools[].parameters.properties.first_name.type: str
$.tool_registry.tools[].parameters.properties.last_name: dict
$.tool_registry.tools[].parameters.properties.last_name.description: str
$.tool_registry.tools[].parameters.properties.last_name.title: str
$.tool_registry.tools[].parameters.properties.last_name.type: str
$.tool_registry.tools[].parameters.properties.zip: dict
$.tool_registry.tools[].parameters.properties.zip.description: str
$.tool_registry.tools[].parameters.properties.zip.title: str
$.tool_registry.tools[].parameters.properties.zip.type: str
$.tool_registry.tools[].parameters.properties.product_id: dict
$.tool_registry.tools[].parameters.properties.product_id.description: str
$.tool_registry.tools[].parameters.properties.product_id.title: str
$.tool_registry.tools[].parameters.properties.product_id.type: str
$.tool_registry.tools[].parameters.properties.address1: dict
$.tool_registry.tools[].parameters.properties.address1.description: str
$.tool_registry.tools[].parameters.properties.address1.title: str
$.tool_registry.tools[].parameters.properties.address1.type: str
$.tool_registry.tools[].parameters.properties.address2: dict
$.tool_registry.tools[].parameters.properties.address2.description: str
$.tool_registry.tools[].parameters.properties.address2.title: str
$.tool_registry.tools[].parameters.properties.address2.type: str
$.tool_registry.tools[].parameters.properties.city: dict
$.tool_registry.tools[].parameters.properties.city.description: str
$.tool_registry.tools[].parameters.properties.city.title: str
$.tool_registry.tools[].parameters.properties.city.type: str
$.tool_registry.tools[].parameters.properties.state: dict
$.tool_registry.tools[].parameters.properties.state.description: str
$.tool_registry.tools[].parameters.properties.state.title: str
$.tool_registry.tools[].parameters.properties.state.type: str
$.tool_registry.tools[].parameters.properties.country: dict
$.tool_registry.tools[].parameters.properties.country.description: str
$.tool_registry.tools[].parameters.properties.country.title: str
$.tool_registry.tools[].parameters.properties.country.type: str
$.eval_details.reward_info.action_checks[].action.arguments.email: str
$.trace_meta.trace.steps[].tool_arguments.first_name: str
$.trace_meta.trace.steps[].tool_arguments.last_name: str
$.trace_meta.trace.steps[].tool_arguments.zip: str
$.trace_meta.trace.steps[].tool_arguments.order_id: str
$.eval_details.reward_info.action_checks[].action.arguments.expression: str
$.eval_details.reward_info.action_checks[].action.arguments.reason: str
$.trace_meta.trace.steps[].tool_arguments.reason: str
$.eval_details.reward_info.env_assertions[]: dict
$.eval_details.reward_info.env_assertions[].env_assertion: dict
$.eval_details.reward_info.env_assertions[].env_assertion.env_type: str
$.eval_details.reward_info.env_assertions[].env_assertion.func_name: str
$.eval_details.reward_info.env_assertions[].env_assertion.arguments: dict
$.eval_details.reward_info.env_assertions[].env_assertion.arguments.expected_status: bool | str
$.eval_details.reward_info.env_assertions[].env_assertion.assert_value: bool
$.eval_details.reward_info.env_assertions[].env_assertion.message: NoneType | str
$.eval_details.reward_info.env_assertions[].met: bool
$.eval_details.reward_info.env_assertions[].reward: float
$.eval_details.reward_info.env_assertions[].env_assertion.arguments.expected_speed: int
$.eval_details.reward_info.env_assertions[].env_assertion.arguments.expected_desc: str
$.eval_details.reward_info.env_assertions[].env_assertion.arguments.customer_id: str
$.eval_details.reward_info.env_assertions[].env_assertion.arguments.line_id: str
$.eval_details.reward_info.env_assertions[].env_assertion.arguments.expected_amount: float
$.eval_details.reward_info.action_checks[].action.arguments.mode: str
$.eval_details.reward_info.action_checks[].action.arguments.customer_id: str
$.eval_details.reward_info.action_checks[].action.arguments.line_id: str
$.eval_details.reward_info.action_checks[].action.arguments.gb_amount: float
$.eval_details.reward_info.reward_breakdown.ENV_ASSERTION: float
$.tool_registry.tools[].parameters.properties.customer_id: dict
$.tool_registry.tools[].parameters.properties.customer_id.description: str
$.tool_registry.tools[].parameters.properties.customer_id.title: str
$.tool_registry.tools[].parameters.properties.customer_id.type: str
$.tool_registry.tools[].parameters.properties.line_id: dict
$.tool_registry.tools[].parameters.properties.line_id.description: str
$.tool_registry.tools[].parameters.properties.line_id.title: str
$.tool_registry.tools[].parameters.properties.line_id.type: str
$.tool_registry.tools[].parameters.properties.limit: dict
... (+57 lines)
```
- `domain`: {'"telecom"': 396, '"retail"': 395, '"airline"': 193}
- `benchmark`: {'"tau2bench"': 984}
- `reward`: {'0.0': 599, '1.0': 385}
- `source_model`: {'"Qwen3-Next"': 200, '"Qwen3-235B"': 199, '"DeepSeek-V3.2"': 198, '"Gemini-2.5-Flash"': 198, '"DeepSeek-R1"': 189}
- sample: `samples/downloaded_domains_data__downloaded_domains_data__airline__secondary_source__tau2bench.jsonl__line0.json` (53 KB)
- sample: `samples/downloaded_domains_data__downloaded_domains_data__airline__secondary_source__tau2bench.jsonl__line2.json` (59 KB)
- sample: `samples/downloaded_domains_data__downloaded_domains_data__airline__secondary_source__tau2bench.jsonl__line8.json` (58 KB)
- sample: `samples/downloaded_domains_data__downloaded_domains_data__airline__secondary_source__tau2bench.jsonl__line9.json` (36 KB)
- sample: `samples/downloaded_domains_data__downloaded_domains_data__airline__secondary_source__tau2bench.jsonl__FULL_line0.json` (60 KB)

## downloaded_domains_data/downloaded_domains_data/airline/secondary_source/tau2bench.parquet

Размер: 16349.5 КБ
parquet не прочитан: ModuleNotFoundError("No module named 'pyarrow'")

## downloaded_domains_data/downloaded_domains_data/airline/secondary_source/tau2bench_cleaning_report.json (в папке 7 файлов *.json; взяты первые 2)

Размер: 152.3 КБ
Тип: JSON list (len=189)
Схема:
```
$: len~189 | list
$[]: dict
$[].id: str
$[].benchmark: str
$[].source_model: str
$[].cleaning_info: len~1 | len~2 | list
$[].cleaning_info[]: dict
$[].cleaning_info[].message_index: int
$[].cleaning_info[].role: str
$[].cleaning_info[].removals: len~1 | len~2 | len~3 | len~4 | len~9 | list
$[].cleaning_info[].removals[]: dict
$[].cleaning_info[].removals[].type: str
$[].cleaning_info[].removals[].start: int
$[].cleaning_info[].removals[].end: int
$[].cleaning_info[].removals[].length: int
$[].cleaning_info[].original_length: int
$[].cleaning_info[].cleaned_length: int
```
- sample: `samples/downloaded_domains_data__downloaded_domains_data__airline__secondary_source__tau2bench_cleaning_report.json` (2 KB)

## downloaded_domains_data/downloaded_domains_data/airline/tau2_env/db.json

Размер: 6877.7 КБ
Тип: JSON dict (len=3)
Схема:
```
$: dict
$.flights: dict
$.flights.{*}: 300 keys | dict
$.flights.{*}.origin: str
$.flights.{*}.destination: str
$.flights.{*}.flight_number: str
$.flights.{*}.scheduled_departure_time_est: str
$.flights.{*}.scheduled_arrival_time_est: str
$.flights.{*}.dates: dict
$.flights.{*}.dates.2024-05-01: dict
$.flights.{*}.dates.2024-05-01.status: str
$.flights.{*}.dates.2024-05-01.actual_departure_time_est: str
$.flights.{*}.dates.2024-05-01.actual_arrival_time_est: str
$.flights.{*}.dates.2024-05-02: dict
$.flights.{*}.dates.2024-05-02.status: str
$.flights.{*}.dates.2024-05-02.actual_departure_time_est: str
$.flights.{*}.dates.2024-05-02.actual_arrival_time_est: str
$.flights.{*}.dates.2024-05-03: dict
$.flights.{*}.dates.2024-05-03.status: str
$.flights.{*}.dates.2024-05-04: dict
$.flights.{*}.dates.2024-05-04.status: str
$.flights.{*}.dates.2024-05-04.actual_departure_time_est: str
$.flights.{*}.dates.2024-05-04.actual_arrival_time_est: str
$.flights.{*}.dates.2024-05-05: dict
$.flights.{*}.dates.2024-05-05.status: str
$.flights.{*}.dates.2024-05-05.actual_departure_time_est: str
$.flights.{*}.dates.2024-05-05.actual_arrival_time_est: str
$.flights.{*}.dates.2024-05-06: dict
$.flights.{*}.dates.2024-05-06.status: str
$.flights.{*}.dates.2024-05-06.actual_departure_time_est: str
$.flights.{*}.dates.2024-05-06.actual_arrival_time_est: str
$.flights.{*}.dates.2024-05-07: dict
$.flights.{*}.dates.2024-05-07.status: str
$.flights.{*}.dates.2024-05-07.actual_departure_time_est: str
$.flights.{*}.dates.2024-05-07.actual_arrival_time_est: str
$.flights.{*}.dates.2024-05-08: dict
$.flights.{*}.dates.2024-05-08.status: str
$.flights.{*}.dates.2024-05-08.actual_departure_time_est: str
$.flights.{*}.dates.2024-05-08.actual_arrival_time_est: str
$.flights.{*}.dates.2024-05-09: dict
$.flights.{*}.dates.2024-05-09.status: str
$.flights.{*}.dates.2024-05-09.actual_departure_time_est: str
$.flights.{*}.dates.2024-05-09.actual_arrival_time_est: str
$.flights.{*}.dates.2024-05-10: dict
$.flights.{*}.dates.2024-05-10.status: str
$.flights.{*}.dates.2024-05-10.actual_departure_time_est: str
$.flights.{*}.dates.2024-05-10.actual_arrival_time_est: str
$.flights.{*}.dates.2024-05-11: dict
$.flights.{*}.dates.2024-05-11.status: str
$.flights.{*}.dates.2024-05-11.actual_departure_time_est: str
$.flights.{*}.dates.2024-05-11.actual_arrival_time_est: str
$.flights.{*}.dates.2024-05-12: dict
$.flights.{*}.dates.2024-05-12.status: str
$.flights.{*}.dates.2024-05-12.actual_departure_time_est: str
$.flights.{*}.dates.2024-05-12.actual_arrival_time_est: str
$.flights.{*}.dates.2024-05-13: dict
$.flights.{*}.dates.2024-05-13.status: str
$.flights.{*}.dates.2024-05-13.actual_departure_time_est: str
$.flights.{*}.dates.2024-05-13.actual_arrival_time_est: str
$.flights.{*}.dates.2024-05-14: dict
$.flights.{*}.dates.2024-05-14.status: str
$.flights.{*}.dates.2024-05-15: dict
$.flights.{*}.dates.2024-05-15.status: str
$.flights.{*}.dates.2024-05-15.actual_departure_time_est: str
$.flights.{*}.dates.2024-05-15.actual_arrival_time_est: str
$.flights.{*}.dates.2024-05-16: dict
$.flights.{*}.dates.2024-05-16.status: str
$.flights.{*}.dates.2024-05-16.available_seats: dict
$.flights.{*}.dates.2024-05-16.available_seats.basic_economy: int
$.flights.{*}.dates.2024-05-16.available_seats.economy: int
$.flights.{*}.dates.2024-05-16.available_seats.business: int
$.flights.{*}.dates.2024-05-16.prices: dict
$.flights.{*}.dates.2024-05-16.prices.basic_economy: int
$.flights.{*}.dates.2024-05-16.prices.economy: int
$.flights.{*}.dates.2024-05-16.prices.business: int
$.flights.{*}.dates.2024-05-17: dict
$.flights.{*}.dates.2024-05-17.status: str
$.flights.{*}.dates.2024-05-17.available_seats: dict
$.flights.{*}.dates.2024-05-17.available_seats.basic_economy: int
$.flights.{*}.dates.2024-05-17.available_seats.economy: int
$.flights.{*}.dates.2024-05-17.available_seats.business: int
$.flights.{*}.dates.2024-05-17.prices: dict
$.flights.{*}.dates.2024-05-17.prices.basic_economy: int
$.flights.{*}.dates.2024-05-17.prices.economy: int
$.flights.{*}.dates.2024-05-17.prices.business: int
$.flights.{*}.dates.2024-05-18: dict
$.flights.{*}.dates.2024-05-18.status: str
$.flights.{*}.dates.2024-05-18.available_seats: dict
$.flights.{*}.dates.2024-05-18.available_seats.basic_economy: int
$.flights.{*}.dates.2024-05-18.available_seats.economy: int
$.flights.{*}.dates.2024-05-18.available_seats.business: int
$.flights.{*}.dates.2024-05-18.prices: dict
$.flights.{*}.dates.2024-05-18.prices.basic_economy: int
$.flights.{*}.dates.2024-05-18.prices.economy: int
$.flights.{*}.dates.2024-05-18.prices.business: int
$.flights.{*}.dates.2024-05-19: dict
$.flights.{*}.dates.2024-05-19.status: str
$.flights.{*}.dates.2024-05-19.available_seats: dict
$.flights.{*}.dates.2024-05-19.available_seats.basic_economy: int
$.flights.{*}.dates.2024-05-19.available_seats.economy: int
$.flights.{*}.dates.2024-05-19.available_seats.business: int
$.flights.{*}.dates.2024-05-19.prices: dict
$.flights.{*}.dates.2024-05-19.prices.basic_economy: int
$.flights.{*}.dates.2024-05-19.prices.economy: int
$.flights.{*}.dates.2024-05-19.prices.business: int
$.flights.{*}.dates.2024-05-20: dict
$.flights.{*}.dates.2024-05-20.status: str
$.flights.{*}.dates.2024-05-20.available_seats: dict
$.flights.{*}.dates.2024-05-20.available_seats.basic_economy: int
$.flights.{*}.dates.2024-05-20.available_seats.economy: int
$.flights.{*}.dates.2024-05-20.available_seats.business: int
$.flights.{*}.dates.2024-05-20.prices: dict
$.flights.{*}.dates.2024-05-20.prices.basic_economy: int
$.flights.{*}.dates.2024-05-20.prices.economy: int
$.flights.{*}.dates.2024-05-20.prices.business: int
$.flights.{*}.dates.2024-05-21: dict
$.flights.{*}.dates.2024-05-21.status: str
$.flights.{*}.dates.2024-05-21.available_seats: dict
$.flights.{*}.dates.2024-05-21.available_seats.basic_economy: int
$.flights.{*}.dates.2024-05-21.available_seats.economy: int
$.flights.{*}.dates.2024-05-21.available_seats.business: int
$.flights.{*}.dates.2024-05-21.prices: dict
$.flights.{*}.dates.2024-05-21.prices.basic_economy: int
$.flights.{*}.dates.2024-05-21.prices.economy: int
$.flights.{*}.dates.2024-05-21.prices.business: int
$.flights.{*}.dates.2024-05-22: dict
$.flights.{*}.dates.2024-05-22.status: str
$.flights.{*}.dates.2024-05-22.available_seats: dict
$.flights.{*}.dates.2024-05-22.available_seats.basic_economy: int
$.flights.{*}.dates.2024-05-22.available_seats.economy: int
$.flights.{*}.dates.2024-05-22.available_seats.business: int
$.flights.{*}.dates.2024-05-22.prices: dict
$.flights.{*}.dates.2024-05-22.prices.basic_economy: int
$.flights.{*}.dates.2024-05-22.prices.economy: int
$.flights.{*}.dates.2024-05-22.prices.business: int
$.flights.{*}.dates.2024-05-23: dict
$.flights.{*}.dates.2024-05-23.status: str
$.flights.{*}.dates.2024-05-23.available_seats: dict
$.flights.{*}.dates.2024-05-23.available_seats.basic_economy: int
$.flights.{*}.dates.2024-05-23.available_seats.economy: int
$.flights.{*}.dates.2024-05-23.available_seats.business: int
$.flights.{*}.dates.2024-05-23.prices: dict
$.flights.{*}.dates.2024-05-23.prices.basic_economy: int
$.flights.{*}.dates.2024-05-23.prices.economy: int
$.flights.{*}.dates.2024-05-23.prices.business: int
$.flights.{*}.dates.2024-05-24: dict
$.flights.{*}.dates.2024-05-24.status: str
$.flights.{*}.dates.2024-05-24.available_seats: dict
$.flights.{*}.dates.2024-05-24.available_seats.basic_economy: int
$.flights.{*}.dates.2024-05-24.available_seats.economy: int
$.flights.{*}.dates.2024-05-24.available_seats.business: int
$.flights.{*}.dates.2024-05-24.prices: dict
$.flights.{*}.dates.2024-05-24.prices.basic_economy: int
$.flights.{*}.dates.2024-05-24.prices.economy: int
$.flights.{*}.dates.2024-05-24.prices.business: int
$.flights.{*}.dates.2024-05-25: dict
$.flights.{*}.dates.2024-05-25.status: str
$.flights.{*}.dates.2024-05-25.available_seats: dict
$.flights.{*}.dates.2024-05-25.available_seats.basic_economy: int
$.flights.{*}.dates.2024-05-25.available_seats.economy: int
$.flights.{*}.dates.2024-05-25.available_seats.business: int
$.flights.{*}.dates.2024-05-25.prices: dict
$.flights.{*}.dates.2024-05-25.prices.basic_economy: int
$.flights.{*}.dates.2024-05-25.prices.economy: int
$.flights.{*}.dates.2024-05-25.prices.business: int
$.flights.{*}.dates.2024-05-26: dict
$.flights.{*}.dates.2024-05-26.status: str
$.flights.{*}.dates.2024-05-26.available_seats: dict
$.flights.{*}.dates.2024-05-26.available_seats.basic_economy: int
$.flights.{*}.dates.2024-05-26.available_seats.economy: int
$.flights.{*}.dates.2024-05-26.available_seats.business: int
$.flights.{*}.dates.2024-05-26.prices: dict
$.flights.{*}.dates.2024-05-26.prices.basic_economy: int
$.flights.{*}.dates.2024-05-26.prices.economy: int
$.flights.{*}.dates.2024-05-26.prices.business: int
$.flights.{*}.dates.2024-05-27: dict
$.flights.{*}.dates.2024-05-27.status: str
$.flights.{*}.dates.2024-05-27.available_seats: dict
$.flights.{*}.dates.2024-05-27.available_seats.basic_economy: int
$.flights.{*}.dates.2024-05-27.available_seats.economy: int
$.flights.{*}.dates.2024-05-27.available_seats.business: int
$.flights.{*}.dates.2024-05-27.prices: dict
$.flights.{*}.dates.2024-05-27.prices.basic_economy: int
$.flights.{*}.dates.2024-05-27.prices.economy: int
$.flights.{*}.dates.2024-05-27.prices.business: int
$.flights.{*}.dates.2024-05-28: dict
$.flights.{*}.dates.2024-05-28.status: str
$.flights.{*}.dates.2024-05-28.available_seats: dict
$.flights.{*}.dates.2024-05-28.available_seats.basic_economy: int
$.flights.{*}.dates.2024-05-28.available_seats.economy: int
$.flights.{*}.dates.2024-05-28.available_seats.business: int
$.flights.{*}.dates.2024-05-28.prices: dict
$.flights.{*}.dates.2024-05-28.prices.basic_economy: int
$.flights.{*}.dates.2024-05-28.prices.economy: int
$.flights.{*}.dates.2024-05-28.prices.business: int
$.flights.{*}.dates.2024-05-29: dict
$.flights.{*}.dates.2024-05-29.status: str
$.flights.{*}.dates.2024-05-29.available_seats: dict
$.flights.{*}.dates.2024-05-29.available_seats.basic_economy: int
$.flights.{*}.dates.2024-05-29.available_seats.economy: int
$.flights.{*}.dates.2024-05-29.available_seats.business: int
$.flights.{*}.dates.2024-05-29.prices: dict
$.flights.{*}.dates.2024-05-29.prices.basic_economy: int
$.flights.{*}.dates.2024-05-29.prices.economy: int
$.flights.{*}.dates.2024-05-29.prices.business: int
$.flights.{*}.dates.2024-05-30: dict
$.flights.{*}.dates.2024-05-30.status: str
$.flights.{*}.dates.2024-05-30.available_seats: dict
$.flights.{*}.dates.2024-05-30.available_seats.basic_economy: int
$.flights.{*}.dates.2024-05-30.available_seats.economy: int
$.flights.{*}.dates.2024-05-30.available_seats.business: int
$.flights.{*}.dates.2024-05-30.prices: dict
$.flights.{*}.dates.2024-05-30.prices.basic_economy: int
$.flights.{*}.dates.2024-05-30.prices.economy: int
$.flights.{*}.dates.2024-05-30.prices.business: int
$.flights.{*}.dates.2024-05-03.actual_departure_time_est: str
$.flights.{*}.dates.2024-05-03.actual_arrival_time_est: str
$.flights.{*}.dates.2024-05-14.actual_departure_time_est: str
$.flights.{*}.dates.2024-05-14.actual_arrival_time_est: str
$.flights.{*}.dates.2024-05-15.estimated_departure_time_est: str
$.flights.{*}.dates.2024-05-15.estimated_arrival_time_est: str
$.users: dict
$.users.{*}: 500 keys | dict
$.users.{*}.user_id: str
$.users.{*}.name: dict
$.users.{*}.name.first_name: str
$.users.{*}.name.last_name: str
$.users.{*}.address: dict
$.users.{*}.address.address1: str
$.users.{*}.address.address2: str
$.users.{*}.address.city: str
$.users.{*}.address.country: str
$.users.{*}.address.state: str
$.users.{*}.address.zip: str
$.users.{*}.email: str
$.users.{*}.dob: str
$.users.{*}.payment_methods: dict
$.users.{*}.payment_methods.credit_card_4421486: dict
$.users.{*}.payment_methods.credit_card_4421486.source: str
$.users.{*}.payment_methods.credit_card_4421486.id: str
$.users.{*}.payment_methods.credit_card_4421486.brand: str
$.users.{*}.payment_methods.credit_card_4421486.last_four: str
$.users.{*}.payment_methods.certificate_4856383: dict
$.users.{*}.payment_methods.certificate_4856383.source: str
$.users.{*}.payment_methods.certificate_4856383.id: str
$.users.{*}.payment_methods.certificate_4856383.amount: float
$.users.{*}.payment_methods.certificate_7504069: dict
$.users.{*}.payment_methods.certificate_7504069.source: str
$.users.{*}.payment_methods.certificate_7504069.id: str
$.users.{*}.payment_methods.certificate_7504069.amount: float
$.users.{*}.payment_methods.credit_card_1955700: dict
$.users.{*}.payment_methods.credit_card_1955700.source: str
$.users.{*}.payment_methods.credit_card_1955700.id: str
$.users.{*}.payment_methods.credit_card_1955700.brand: str
$.users.{*}.payment_methods.credit_card_1955700.last_four: str
$.users.{*}.saved_passengers: len~1 | len~2 | list
$.users.{*}.saved_passengers[]: dict
$.users.{*}.saved_passengers[].first_name: str
$.users.{*}.saved_passengers[].last_name: str
$.users.{*}.saved_passengers[].dob: str
$.users.{*}.membership: str
$.users.{*}.reservations: len~3 | len~4 | list
$.users.{*}.reservations[]: str
$.users.{*}.payment_methods.gift_card_5309492: dict
$.users.{*}.payment_methods.gift_card_5309492.source: str
$.users.{*}.payment_methods.gift_card_5309492.id: str
$.users.{*}.payment_methods.gift_card_5309492.amount: float
$.users.{*}.payment_methods.credit_card_2140654: dict
$.users.{*}.payment_methods.credit_card_2140654.source: str
$.users.{*}.payment_methods.credit_card_2140654.id: str
$.users.{*}.payment_methods.credit_card_2140654.brand: str
$.users.{*}.payment_methods.credit_card_2140654.last_four: str
$.users.{*}.payment_methods.certificate_7502997: dict
$.users.{*}.payment_methods.certificate_7502997.source: str
$.users.{*}.payment_methods.certificate_7502997.id: str
$.users.{*}.payment_methods.certificate_7502997.amount: float
$.users.{*}.payment_methods.certificate_3321326: dict
$.users.{*}.payment_methods.certificate_3321326.source: str
$.users.{*}.payment_methods.certificate_3321326.id: str
$.users.{*}.payment_methods.certificate_3321326.amount: float
$.users.{*}.payment_methods.credit_card_6082923: dict
$.users.{*}.payment_methods.credit_card_6082923.source: str
$.users.{*}.payment_methods.credit_card_6082923.id: str
$.users.{*}.payment_methods.credit_card_6082923.brand: str
$.users.{*}.payment_methods.credit_card_6082923.last_four: str
$.users.{*}.payment_methods.certificate_1530821: dict
$.users.{*}.payment_methods.certificate_1530821.source: str
$.users.{*}.payment_methods.certificate_1530821.id: str
$.users.{*}.payment_methods.certificate_1530821.amount: float
$.users.{*}.payment_methods.certificate_3863871: dict
$.users.{*}.payment_methods.certificate_3863871.source: str
$.users.{*}.payment_methods.certificate_3863871.id: str
$.users.{*}.payment_methods.certificate_3863871.amount: float
$.users.{*}.payment_methods.credit_card_4319822: dict
$.users.{*}.payment_methods.credit_card_4319822.source: str
$.users.{*}.payment_methods.credit_card_4319822.id: str
$.users.{*}.payment_methods.credit_card_4319822.brand: str
$.users.{*}.payment_methods.credit_card_4319822.last_four: str
$.users.{*}.payment_methods.certificate_5569851: dict
$.users.{*}.payment_methods.certificate_5569851.source: str
$.users.{*}.payment_methods.certificate_5569851.id: str
$.users.{*}.payment_methods.certificate_5569851.amount: float
$.users.{*}.payment_methods.gift_card_9785014: dict
$.users.{*}.payment_methods.gift_card_9785014.source: str
$.users.{*}.payment_methods.gift_card_9785014.id: str
$.users.{*}.payment_methods.gift_card_9785014.amount: float
$.reservations: dict
$.reservations.{*}: 2000 keys | dict
$.reservations.{*}.reservation_id: str
$.reservations.{*}.user_id: str
$.reservations.{*}.origin: str
$.reservations.{*}.destination: str
$.reservations.{*}.flight_type: str
$.reservations.{*}.cabin: str
$.reservations.{*}.flights: len~2 | list
$.reservations.{*}.flights[]: dict
$.reservations.{*}.flights[].origin: str
$.reservations.{*}.flights[].destination: str
$.reservations.{*}.flights[].flight_number: str
$.reservations.{*}.flights[].date: str
$.reservations.{*}.flights[].price: int
$.reservations.{*}.passengers: len~1 | len~3 | list
$.reservations.{*}.passengers[]: dict
$.reservations.{*}.passengers[].first_name: str
$.reservations.{*}.passengers[].last_name: str
$.reservations.{*}.passengers[].dob: str
$.reservations.{*}.payment_history: len~1 | list
$.reservations.{*}.payment_history[]: dict
$.reservations.{*}.payment_history[].payment_id: str
$.reservations.{*}.payment_history[].amount: int
$.reservations.{*}.created_at: str
$.reservations.{*}.total_baggages: int
$.reservations.{*}.nonfree_baggages: int
$.reservations.{*}.insurance: str
```
- sample: `samples/downloaded_domains_data__downloaded_domains_data__airline__tau2_env__db.json` (206 KB)

## downloaded_domains_data/downloaded_domains_data/airline/tau2_env/policy.md

Размер: 7.5 КБ
Тип: текст, 7676 символов, 167 строк
- head: `samples/downloaded_domains_data__downloaded_domains_data__airline__tau2_env__policy.md.txt`

## downloaded_domains_data/downloaded_domains_data/airline/tau2_env/split_tasks.json

Размер: 1.4 КБ
Тип: JSON dict (len=3)
Схема:
```
$: dict
$.train: len~30 | list
$.train[]: str
$.test: len~20 | list
$.test[]: str
$.base: len~50 | list
$.base[]: str
```
- sample: `samples/downloaded_domains_data__downloaded_domains_data__airline__tau2_env__split_tasks.json` (0 KB)

## downloaded_domains_data/downloaded_domains_data/airline/tau2_env/tasks.json

Размер: 151.9 КБ
Тип: JSON list (len=50)
Схема:
```
$: len~50 | list
$[]: dict
$[].id: str
$[].description: dict
$[].description.purpose: str
$[].description.relevant_policies: NoneType
$[].description.notes: NoneType | str
$[].user_scenario: dict
$[].user_scenario.persona: NoneType
$[].user_scenario.instructions: dict
$[].user_scenario.instructions.task_instructions: str
$[].user_scenario.instructions.domain: str
$[].user_scenario.instructions.reason_for_call: str
$[].user_scenario.instructions.known_info: str
$[].user_scenario.instructions.unknown_info: NoneType | str
$[].initial_state: NoneType
$[].evaluation_criteria: dict
$[].evaluation_criteria.actions: len~0 | len~1 | len~11 | len~2 | len~3 | len~4 | len~5 | len~6 | list
$[].evaluation_criteria.communicate_info: len~0 | len~1 | len~3 | list
$[].evaluation_criteria.nl_assertions: len~1 | len~2 | len~3 | len~4 | len~5 | len~6 | len~8 | list
$[].evaluation_criteria.nl_assertions[]: str
$[].evaluation_criteria.reward_basis: len~2 | list
$[].evaluation_criteria.reward_basis[]: str
$[].annotations: NoneType
$[].evaluation_criteria.actions[]: dict
$[].evaluation_criteria.actions[].action_id: str
$[].evaluation_criteria.actions[].name: str
$[].evaluation_criteria.actions[].arguments: dict
$[].evaluation_criteria.actions[].arguments.user_id: str
$[].evaluation_criteria.actions[].info: NoneType
$[].evaluation_criteria.actions[].arguments.reservation_id: str
$[].evaluation_criteria.communicate_info[]: str
$[].evaluation_criteria.actions[].arguments.cabin: str
$[].evaluation_criteria.actions[].arguments.flights: len~1 | len~2 | len~3 | len~4 | list
$[].evaluation_criteria.actions[].arguments.flights[]: dict
$[].evaluation_criteria.actions[].arguments.flights[].flight_number: str
$[].evaluation_criteria.actions[].arguments.flights[].date: str
$[].evaluation_criteria.actions[].arguments.payment_id: str
$[].evaluation_criteria.actions[].arguments.origin: str
$[].evaluation_criteria.actions[].arguments.destination: str
$[].evaluation_criteria.actions[].arguments.date: str
$[].evaluation_criteria.actions[].arguments.flight_type: str
$[].evaluation_criteria.actions[].arguments.passengers: len~1 | len~2 | len~3 | list
$[].evaluation_criteria.actions[].arguments.passengers[]: dict
$[].evaluation_criteria.actions[].arguments.passengers[].first_name: str
$[].evaluation_criteria.actions[].arguments.passengers[].last_name: str
$[].evaluation_criteria.actions[].arguments.passengers[].dob: str
$[].evaluation_criteria.actions[].arguments.payment_methods: len~1 | len~2 | len~4 | list
$[].evaluation_criteria.actions[].arguments.payment_methods[]: dict
$[].evaluation_criteria.actions[].arguments.payment_methods[].payment_id: str
$[].evaluation_criteria.actions[].arguments.payment_methods[].amount: int
$[].evaluation_criteria.actions[].arguments.total_baggages: int
$[].evaluation_criteria.actions[].arguments.nonfree_baggages: int
$[].evaluation_criteria.actions[].arguments.insurance: str
$[].evaluation_criteria.actions[].arguments.expression: str
$[].evaluation_criteria.actions[].arguments.summary: str
$[].evaluation_criteria.actions[].compare_args: len~0 | list
```
- sample: `samples/downloaded_domains_data__downloaded_domains_data__airline__tau2_env__tasks.json` (2 KB)

## downloaded_domains_data/downloaded_domains_data/airline/tau2_env/tools.py

Размер: 27.5 КБ
Тип: текст, 28123 символов, 743 строк
Определения (26): AirlineTools, __init__, _get_user, _get_reservation, _get_flight, _get_flight_instance, _get_flights_from_flight_infos, _get_new_reservation_id, _get_new_payment_id, _get_datetime, _search_direct_flight, _payment_for_update, book_reservation, calculate, cancel_reservation, get_reservation_details, get_user_details, list_all_airports, search_direct_flight, search_onestop_flight, send_certificate, transfer_to_human_agents, update_reservation_baggages, update_reservation_flights, update_reservation_passengers, get_flight_status
- head: `samples/downloaded_domains_data__downloaded_domains_data__airline__tau2_env__tools.py.txt`

## downloaded_domains_data/retail/secondary_source/README.md

Размер: 2.0 КБ
Тип: текст, 2052 символов, 50 строк
- head: `samples/downloaded_domains_data__retail__secondary_source__README.md.txt`

## downloaded_domains_data/retail/secondary_source/bodies.json (в папке 7 файлов *.json; взяты первые 2)

Размер: 10.9 КБ
Тип: JSON dict (len=16)
Схема:
```
$: dict
$.calculate: str
$.cancel_pending_order: str
$.exchange_delivered_order_items: str
$.find_user_id_by_email: str
$.find_user_id_by_name_zip: str
$.get_item_details: str
$.get_order_details: str
$.get_product_details: str
$.get_user_details: str
$.list_all_product_types: str
$.modify_pending_order_address: str
$.modify_pending_order_items: str
$.modify_pending_order_payment: str
$.modify_user_address: str
$.return_delivered_order_items: str
$.transfer_to_human_agents: str
```
- sample: `samples/downloaded_domains_data__retail__secondary_source__bodies.json` (10 KB)

## downloaded_domains_data/retail/secondary_source/canon-rules.json (в папке 7 файлов *.json; взяты первые 2)

Размер: 1.2 КБ
Тип: JSON dict (len=18)
Схема:
```
$: dict
$.lowercase: bool
$.collapse_whitespace: bool
$.numbers: bool
$.number_precision: int
$.currency: bool
$.currency_symbols: len~4 | list
$.currency_symbols[]: str
$.currency_codes: len~4 | list
$.currency_codes[]: str
$.currency_symbol_codes: dict
$.currency_symbol_codes.$: str
$.currency_symbol_codes.€: str
$.currency_symbol_codes.£: str
$.currency_symbol_codes.¥: str
$.timestamps: bool
$.timestamp_formats: len~0 | list
$.assume_utc: bool
$.id_patterns: dict
$.id_patterns.items.item_id: str
$.id_patterns.orders.order_id: str
$.id_patterns.orders.user_id: str
$.id_patterns.products.product_id: str
$.id_patterns.users.user_id: str
$.id_upper: bool
$.id_strip_chars: str
$.unordered_lists: len~0 | list
$.unordered_all: bool
$.case_sensitive_paths: len~15 | list
$.case_sensitive_paths[]: str
$.default_class: str
```
- sample: `samples/downloaded_domains_data__retail__secondary_source__canon-rules.json` (1 KB)

## downloaded_domains_data/retail/secondary_source/env/calls/calculate.jsonl (в папке 16 файлов *.jsonl; взяты первые 2)

Размер: 18.3 КБ
Тип: JSONL; прочитано строк: 29 (битых: 0, лимит 20000)
Схема (объединение по первым записям):
```
$: dict
$.args: dict
$.args.expression: str
$.cut_marker: NoneType
$.error: NoneType
$.has_result: bool
$.id: str
$.latency_ms: float
$.name: str
$.raw_ptr: dict
$.raw_ptr.file_hash: str
$.raw_ptr.msg_index: int
$.raw_ptr.section: NoneType
$.raw_ptr.sim_index: int
$.requestor: str
$.resolved: bool
$.result: str
$.result_ptr: dict
$.result_ptr.file_hash: str
$.result_ptr.msg_index: int
$.result_ptr.section: NoneType
$.result_ptr.sim_index: int
$.trace_id: str
$.truncated: bool
$.visible_len: NoneType
```
- `resolved`: {'true': 29}
- sample: `samples/downloaded_domains_data__retail__secondary_source__env__calls__calculate.jsonl__line0.json` (0 KB)
- sample: `samples/downloaded_domains_data__retail__secondary_source__env__calls__calculate.jsonl__FULL_line0.json` (0 KB)

## downloaded_domains_data/retail/secondary_source/env/calls/cancel_pending_order.jsonl (в папке 16 файлов *.jsonl; взяты первые 2)

Размер: 110.8 КБ
Тип: JSONL; прочитано строк: 61 (битых: 0, лимит 20000)
Схема (объединение по первым записям):
```
$: dict
$.args: dict
$.args.order_id: str
$.args.reason: str
$.cut_marker: NoneType
$.error: NoneType
$.has_result: bool
$.id: str
$.latency_ms: float
$.name: str
$.raw_ptr: dict
$.raw_ptr.file_hash: str
$.raw_ptr.msg_index: int
$.raw_ptr.section: NoneType
$.raw_ptr.sim_index: int
$.requestor: str
$.resolved: bool
$.result: dict
$.result.address: dict
$.result.address.address1: str
$.result.address.address2: str
$.result.address.city: str
$.result.address.country: str
$.result.address.state: str
$.result.address.zip: str
$.result.cancel_reason: str
$.result.exchange_items: NoneType
$.result.exchange_new_items: NoneType
$.result.exchange_payment_method_id: NoneType
$.result.exchange_price_difference: NoneType
$.result.fulfillments: len~0 | list
$.result.items: len~1 | len~2 | len~3 | len~4 | len~5 | list
$.result.items[]: dict
$.result.items[].item_id: str
$.result.items[].name: str
$.result.items[].options: dict
$.result.items[].options.material: str
$.result.items[].options.size: str
$.result.items[].options.waterproof: str
$.result.items[].price: float
$.result.items[].product_id: str
$.result.items[].options.dial color: str
$.result.items[].options.strap material: str
$.result.items[].options.backlight: str
$.result.items[].options.switch type: str
$.result.order_id: str
$.result.payment_history: len~2 | list
$.result.payment_history[]: dict
$.result.payment_history[].amount: float
$.result.payment_history[].payment_method_id: str
$.result.payment_history[].transaction_type: str
$.result.return_items: NoneType
$.result.return_payment_method_id: NoneType
$.result.status: str
$.result.user_id: str
$.result_ptr: dict
$.result_ptr.file_hash: str
$.result_ptr.msg_index: int
$.result_ptr.section: NoneType
$.result_ptr.sim_index: int
$.trace_id: str
$.truncated: bool
$.visible_len: NoneType
$.result.items[].options.capacity: str
$.result.items[].options.color: str
$.result.items[].options.output: str
$.result.items[].options.piece count: str
$.result.items[].options.zipper: str
$.result.items[].options.sole: str
$.result.items[].options.RAM: str
$.result.items[].options.screen size: str
$.result.items[].options.storage: str
$.result.items[].options.battery type: str
$.result.items[].options.speed settings: str
$.result.items[].options.battery life: str
$.result.items[].options.water resistance: str
$.result.items[].options.set type: str
$.result.items[].options.weight range: str
$.result.items[].options.resolution: str
$.result.items[].options.tilt mechanism: str
$.result.items[].options.brightness: str
$.result.items[].options.power source: str
$.result.items[].options.style: str
$.result.items[].options.compartment: str
$.result.items[].options.ventilation: str
$.result.items[].options.band material: str
$.result.items[].options.display: str
$.result.items[].options.difficulty level: str
$.result.items[].options.pieces: str
$.result.items[].options.theme: str
$.result.items[].options.armrest: str
$.result.items[].options.backrest height: str
$.result.items[].options.deck material: str
$.result.items[].options.design: str
$.result.items[].options.length: str
$.result.items[].options.processor: str
$.result.items[].options.ram: str
$.result.items[].options.brand: str
$.result.items[].options.kit size: str
$.result.items[].options.skin tone: str
$.result.items[].options.pressure: str
$.result.items[].options.type: str
$.result.items[].options.features: str
$.result.items[].options.filter type: str
$.result.items[].options.room size: str
$.result.items[].options.thickness: str
$.result.items[].options.connectivity: str
$.result.items[].options.sensor type: str
$.result.items[].options.height: str
$.result.items[].options.zoom: str
```
- `resolved`: {'true': 61}
- sample: `samples/downloaded_domains_data__retail__secondary_source__env__calls__cancel_pending_order.jsonl__line0.json` (2 KB)
- sample: `samples/downloaded_domains_data__retail__secondary_source__env__calls__cancel_pending_order.jsonl__FULL_line0.json` (2 KB)

## downloaded_domains_data/retail/secondary_source/env/canon-rules.json

Размер: 1.2 КБ
Тип: JSON dict (len=18)
Схема:
```
$: dict
$.lowercase: bool
$.collapse_whitespace: bool
$.numbers: bool
$.number_precision: int
$.currency: bool
$.currency_symbols: len~4 | list
$.currency_symbols[]: str
$.currency_codes: len~4 | list
$.currency_codes[]: str
$.currency_symbol_codes: dict
$.currency_symbol_codes.$: str
$.currency_symbol_codes.€: str
$.currency_symbol_codes.£: str
$.currency_symbol_codes.¥: str
$.timestamps: bool
$.timestamp_formats: len~0 | list
$.assume_utc: bool
$.id_patterns: dict
$.id_patterns.items.item_id: str
$.id_patterns.orders.order_id: str
$.id_patterns.orders.user_id: str
$.id_patterns.products.product_id: str
$.id_patterns.users.user_id: str
$.id_upper: bool
$.id_strip_chars: str
$.unordered_lists: len~0 | list
$.unordered_all: bool
$.case_sensitive_paths: len~15 | list
$.case_sensitive_paths[]: str
$.default_class: str
```
- sample: `samples/downloaded_domains_data__retail__secondary_source__env__canon-rules.json` (1 KB)

## downloaded_domains_data/retail/secondary_source/env/data_model.py

Размер: 3.1 КБ
Тип: текст, 3161 символов, 86 строк
Определения (8): Action, Constant, Item, Order, Product, User, DomainDB, load
- head: `samples/downloaded_domains_data__retail__secondary_source__env__data_model.py.txt`

## downloaded_domains_data/retail/secondary_source/env/db.json

Размер: 464.7 КБ
Тип: JSON dict (len=6)
Схема:
```
$: dict
$.actions: dict
$.constants: dict
$.constants.world: dict
$.constants.world.list_all_product_types: dict
$.constants.world.list_all_product_types.Action Camera: str
$.constants.world.list_all_product_types.Air Purifier: str
$.constants.world.list_all_product_types.Backpack: str
$.constants.world.list_all_product_types.Bicycle: str
$.constants.world.list_all_product_types.Bluetooth Speaker: str
$.constants.world.list_all_product_types.Bookshelf: str
$.constants.world.list_all_product_types.Coffee Maker: str
$.constants.world.list_all_product_types.Cycling Helmet: str
$.constants.world.list_all_product_types.Desk Lamp: str
$.constants.world.list_all_product_types.Digital Camera: str
$.constants.world.list_all_product_types.Dumbbell Set: str
$.constants.world.list_all_product_types.E-Reader: str
$.constants.world.list_all_product_types.Electric Kettle: str
$.constants.world.list_all_product_types.Electric Toothbrush: str
$.constants.world.list_all_product_types.Espresso Machine: str
$.constants.world.list_all_product_types.Fleece Jacket: str
$.constants.world.list_all_product_types.Gaming Mouse: str
$.constants.world.list_all_product_types.Garden Hose: str
$.constants.world.list_all_product_types.Grill: str
$.constants.world.list_all_product_types.Headphones: str
$.constants.world.list_all_product_types.Hiking Boots: str
$.constants.world.list_all_product_types.Indoor Security Camera: str
$.constants.world.list_all_product_types.Jigsaw Puzzle: str
$.constants.world.list_all_product_types.LED Light Bulb: str
$.constants.world.list_all_product_types.Laptop: str
$.constants.world.list_all_product_types.Luggage Set: str
$.constants.world.list_all_product_types.Makeup Kit: str
$.constants.world.list_all_product_types.Mechanical Keyboard: str
$.constants.world.list_all_product_types.Notebook: str
$.constants.world.list_all_product_types.Office Chair: str
$.constants.world.list_all_product_types.Patio Umbrella: str
$.constants.world.list_all_product_types.Perfume: str
$.constants.world.list_all_product_types.Pet Bed: str
$.constants.world.list_all_product_types.Portable Charger: str
$.constants.world.list_all_product_types.Running Shoes: str
$.constants.world.list_all_product_types.Skateboard: str
$.constants.world.list_all_product_types.Smart Thermostat: str
$.constants.world.list_all_product_types.Smart Watch: str
$.constants.world.list_all_product_types.Smartphone: str
$.constants.world.list_all_product_types.Sneakers: str
$.constants.world.list_all_product_types.Sunglasses: str
$.constants.world.list_all_product_types.T-Shirt: str
$.constants.world.list_all_product_types.Tablet: str
$.constants.world.list_all_product_types.Tea Kettle: str
$.constants.world.list_all_product_types.Vacuum Cleaner: str
$.constants.world.list_all_product_types.Wall Clock: str
$.constants.world.list_all_product_types.Water Bottle: str
$.constants.world.list_all_product_types.Wireless Earbuds: str
$.constants.world.list_all_product_types.Wristwatch: str
$.constants.world.list_all_product_types.Yoga Mat: str
$.items: dict
$.items.{*}: 72 keys | dict
$.items.{*}.available: bool
$.items.{*}.item_id: str
$.items.{*}.name: str
$.items.{*}.options: dict
$.items.{*}.options.color: str
$.items.{*}.options.connectivity: str
$.items.{*}.options.type: str
$.items.{*}.price: float
$.items.{*}.product_id: str
$.items.{*}.options.RAM: str
$.items.{*}.options.screen size: str
$.items.{*}.options.storage: str
$.orders: dict
$.orders.{*}: 158 keys | dict
$.orders.{*}.address: dict
$.orders.{*}.address.address1: str
$.orders.{*}.address.address2: str
$.orders.{*}.address.city: str
$.orders.{*}.address.country: str
$.orders.{*}.address.state: str
$.orders.{*}.address.zip: str
$.orders.{*}.cancel_reason: NoneType
$.orders.{*}.exchange_items: NoneType
$.orders.{*}.exchange_new_items: NoneType
$.orders.{*}.exchange_payment_method_id: NoneType
$.orders.{*}.exchange_price_difference: NoneType
$.orders.{*}.fulfillments: len~0 | len~1 | list
$.orders.{*}.items: len~1 | len~5 | list
$.orders.{*}.items[]: dict
$.orders.{*}.items[].item_id: str
$.orders.{*}.items[].name: str
$.orders.{*}.items[].options: dict
$.orders.{*}.items[].options.color: str
$.orders.{*}.items[].options.material: str
$.orders.{*}.items[].options.piece count: str
$.orders.{*}.items[].price: float
$.orders.{*}.items[].product_id: str
$.orders.{*}.order_id: str
$.orders.{*}.payment_history: len~1 | len~2 | list
$.orders.{*}.payment_history[]: dict
$.orders.{*}.payment_history[].amount: float
$.orders.{*}.payment_history[].payment_method_id: str
$.orders.{*}.payment_history[].transaction_type: str
$.orders.{*}.return_items: NoneType
$.orders.{*}.return_payment_method_id: NoneType
$.orders.{*}.status: str
$.orders.{*}.user_id: str
$.orders.{*}.fulfillments[]: dict
$.orders.{*}.fulfillments[].item_ids: len~5 | list
$.orders.{*}.fulfillments[].item_ids[]: str
$.orders.{*}.fulfillments[].tracking_id: len~1 | list
$.orders.{*}.fulfillments[].tracking_id[]: str
$.orders.{*}.items[].options.capacity: str
$.orders.{*}.items[].options.stovetop compatibility: str
$.orders.{*}.items[].options.battery life: str
$.orders.{*}.items[].options.water resistance: str
$.orders.{*}.items[].options.connectivity: str
$.orders.{*}.items[].options.type: str
$.orders.{*}.items[].options.RAM: str
$.orders.{*}.items[].options.screen size: str
$.orders.{*}.items[].options.storage: str
$.orders.{*}.items[].options.difficulty level: str
$.orders.{*}.items[].options.pieces: str
$.orders.{*}.items[].options.theme: str
$.orders.{*}.items[].options.deck material: str
$.orders.{*}.items[].options.design: str
$.orders.{*}.items[].options.length: str
$.products: dict
$.products.1656367028: dict
$.products.1656367028.name: str
$.products.1656367028.product_id: str
$.products.1656367028.variants: dict
$.products.1656367028.variants.1151293680: dict
$.products.1656367028.variants.1151293680.available: bool
$.products.1656367028.variants.1151293680.item_id: str
$.products.1656367028.variants.1151293680.options: dict
$.products.1656367028.variants.1151293680.options.backlight: str
$.products.1656367028.variants.1151293680.options.size: str
$.products.1656367028.variants.1151293680.options.switch type: str
$.products.1656367028.variants.1151293680.price: float
$.products.1656367028.variants.1340995114: dict
$.products.1656367028.variants.1340995114.available: bool
$.products.1656367028.variants.1340995114.item_id: str
$.products.1656367028.variants.1340995114.options: dict
$.products.1656367028.variants.1340995114.options.backlight: str
$.products.1656367028.variants.1340995114.options.size: str
$.products.1656367028.variants.1340995114.options.switch type: str
$.products.1656367028.variants.1340995114.price: float
$.products.1656367028.variants.1421289881: dict
$.products.1656367028.variants.1421289881.available: bool
$.products.1656367028.variants.1421289881.item_id: str
$.products.1656367028.variants.1421289881.options: dict
$.products.1656367028.variants.1421289881.options.backlight: str
$.products.1656367028.variants.1421289881.options.size: str
$.products.1656367028.variants.1421289881.options.switch type: str
$.products.1656367028.variants.1421289881.price: float
$.products.1656367028.variants.2299424241: dict
$.products.1656367028.variants.2299424241.available: bool
$.products.1656367028.variants.2299424241.item_id: str
$.products.1656367028.variants.2299424241.options: dict
$.products.1656367028.variants.2299424241.options.backlight: str
$.products.1656367028.variants.2299424241.options.size: str
$.products.1656367028.variants.2299424241.options.switch type: str
$.products.1656367028.variants.2299424241.price: float
$.products.1656367028.variants.3616838507: dict
$.products.1656367028.variants.3616838507.available: bool
$.products.1656367028.variants.3616838507.item_id: str
$.products.1656367028.variants.3616838507.options: dict
$.products.1656367028.variants.3616838507.options.backlight: str
$.products.1656367028.variants.3616838507.options.size: str
$.products.1656367028.variants.3616838507.options.switch type: str
$.products.1656367028.variants.3616838507.price: float
$.products.1656367028.variants.4402162122: dict
$.products.1656367028.variants.4402162122.available: bool
$.products.1656367028.variants.4402162122.item_id: str
$.products.1656367028.variants.4402162122.options: dict
$.products.1656367028.variants.4402162122.options.backlight: str
$.products.1656367028.variants.4402162122.options.size: str
$.products.1656367028.variants.4402162122.options.switch type: str
$.products.1656367028.variants.4402162122.price: float
$.products.1656367028.variants.4648814700: dict
$.products.1656367028.variants.4648814700.available: bool
$.products.1656367028.variants.4648814700.item_id: str
$.products.1656367028.variants.4648814700.options: dict
$.products.1656367028.variants.4648814700.options.backlight: str
$.products.1656367028.variants.4648814700.options.size: str
$.products.1656367028.variants.4648814700.options.switch type: str
$.products.1656367028.variants.4648814700.price: float
$.products.1656367028.variants.4843487907: dict
$.products.1656367028.variants.4843487907.available: bool
$.products.1656367028.variants.4843487907.item_id: str
$.products.1656367028.variants.4843487907.options: dict
$.products.1656367028.variants.4843487907.options.backlight: str
$.products.1656367028.variants.4843487907.options.size: str
$.products.1656367028.variants.4843487907.options.switch type: str
$.products.1656367028.variants.4843487907.price: float
$.products.1656367028.variants.5222576926: dict
$.products.1656367028.variants.5222576926.available: bool
$.products.1656367028.variants.5222576926.item_id: str
$.products.1656367028.variants.5222576926.options: dict
$.products.1656367028.variants.5222576926.options.backlight: str
$.products.1656367028.variants.5222576926.options.size: str
$.products.1656367028.variants.5222576926.options.switch type: str
$.products.1656367028.variants.5222576926.price: float
$.products.1656367028.variants.6342039236: dict
$.products.1656367028.variants.6342039236.available: bool
$.products.1656367028.variants.6342039236.item_id: str
$.products.1656367028.variants.6342039236.options: dict
$.products.1656367028.variants.6342039236.options.backlight: str
$.products.1656367028.variants.6342039236.options.size: str
$.products.1656367028.variants.6342039236.options.switch type: str
$.products.1656367028.variants.6342039236.price: float
$.products.1656367028.variants.6439196450: dict
$.products.1656367028.variants.6439196450.available: bool
$.products.1656367028.variants.6439196450.item_id: str
$.products.1656367028.variants.6439196450.options: dict
$.products.1656367028.variants.6439196450.options.backlight: str
$.products.1656367028.variants.6439196450.options.size: str
$.products.1656367028.variants.6439196450.options.switch type: str
$.products.1656367028.variants.6439196450.price: float
$.products.1656367028.variants.7658724607: dict
$.products.1656367028.variants.7658724607.available: bool
$.products.1656367028.variants.7658724607.item_id: str
$.products.1656367028.variants.7658724607.options: dict
$.products.1656367028.variants.7658724607.options.backlight: str
$.products.1656367028.variants.7658724607.options.size: str
$.products.1656367028.variants.7658724607.options.switch type: str
$.products.1656367028.variants.7658724607.price: float
$.products.1656367028.variants.7706410293: dict
$.products.1656367028.variants.7706410293.available: bool
$.products.1656367028.variants.7706410293.item_id: str
$.products.1656367028.variants.7706410293.options: dict
$.products.1656367028.variants.7706410293.options.backlight: str
$.products.1656367028.variants.7706410293.options.size: str
$.products.1656367028.variants.7706410293.options.switch type: str
$.products.1656367028.variants.7706410293.price: float
$.products.1656367028.variants.7867398203: dict
$.products.1656367028.variants.7867398203.available: bool
$.products.1656367028.variants.7867398203.item_id: str
$.products.1656367028.variants.7867398203.options: dict
$.products.1656367028.variants.7867398203.options.backlight: str
$.products.1656367028.variants.7867398203.options.size: str
$.products.1656367028.variants.7867398203.options.switch type: str
$.products.1656367028.variants.7867398203.price: float
$.products.1656367028.variants.8484921793: dict
$.products.1656367028.variants.8484921793.available: bool
$.products.1656367028.variants.8484921793.item_id: str
$.products.1656367028.variants.8484921793.options: dict
$.products.1656367028.variants.8484921793.options.backlight: str
$.products.1656367028.variants.8484921793.options.size: str
$.products.1656367028.variants.8484921793.options.switch type: str
$.products.1656367028.variants.8484921793.price: float
$.products.1656367028.variants.9025753381: dict
$.products.1656367028.variants.9025753381.available: bool
$.products.1656367028.variants.9025753381.item_id: str
$.products.1656367028.variants.9025753381.options: dict
$.products.1656367028.variants.9025753381.options.backlight: str
$.products.1656367028.variants.9025753381.options.size: str
$.products.1656367028.variants.9025753381.options.switch type: str
$.products.1656367028.variants.9025753381.price: float
$.products.1656367028.variants.9570044148: dict
$.products.1656367028.variants.9570044148.available: bool
$.products.1656367028.variants.9570044148.item_id: str
$.products.1656367028.variants.9570044148.options: dict
$.products.1656367028.variants.9570044148.options.backlight: str
$.products.1656367028.variants.9570044148.options.size: str
$.products.1656367028.variants.9570044148.options.switch type: str
$.products.1656367028.variants.9570044148.price: float
$.products.1656367028.variants.9665000388: dict
$.products.1656367028.variants.9665000388.available: bool
$.products.1656367028.variants.9665000388.item_id: str
$.products.1656367028.variants.9665000388.options: dict
$.products.1656367028.variants.9665000388.options.backlight: str
$.products.1656367028.variants.9665000388.options.size: str
$.products.1656367028.variants.9665000388.options.switch type: str
$.products.1656367028.variants.9665000388.price: float
$.products.1656367028.variants.9690244451: dict
$.products.1656367028.variants.9690244451.available: bool
$.products.1656367028.variants.9690244451.item_id: str
$.products.1656367028.variants.9690244451.name: str
$.products.1656367028.variants.9690244451.options: dict
$.products.1656367028.variants.9690244451.options.backlight: str
$.products.1656367028.variants.9690244451.options.size: str
$.products.1656367028.variants.9690244451.options.switch type: str
$.products.1656367028.variants.9690244451.price: float
$.products.1656367028.variants.9690244451.product_id: str
$.products.1656367028.variants.9991484137: dict
$.products.1656367028.variants.9991484137.available: bool
$.products.1656367028.variants.9991484137.item_id: str
$.products.1656367028.variants.9991484137.options: dict
$.products.1656367028.variants.9991484137.options.backlight: str
$.products.1656367028.variants.9991484137.options.size: str
$.products.1656367028.variants.9991484137.options.switch type: str
$.products.1656367028.variants.9991484137.price: float
$.products.1762337868: dict
$.products.1762337868.name: str
$.products.1762337868.product_id: str
$.products.1762337868.variants: dict
$.products.1762337868.variants.1304426904: dict
$.products.1762337868.variants.1304426904.available: bool
$.products.1762337868.variants.1304426904.item_id: str
$.products.1762337868.variants.1304426904.name: str
$.products.1762337868.variants.1304426904.options: dict
$.products.1762337868.variants.1304426904.options.bagged/bagless: str
$.products.1762337868.variants.1304426904.options.features: str
$.products.1762337868.variants.1304426904.options.type: str
$.products.1762337868.variants.1304426904.price: float
$.products.1762337868.variants.1304426904.product_id: str
$.products.1762337868.variants.1345513440: dict
$.products.1762337868.variants.1345513440.available: bool
$.products.1762337868.variants.1345513440.item_id: str
$.products.1762337868.variants.1345513440.name: str
$.products.1762337868.variants.1345513440.options: dict
$.products.1762337868.variants.1345513440.options.bagged/bagless: str
$.products.1762337868.variants.1345513440.options.features: str
$.products.1762337868.variants.1345513440.options.type: str
$.products.1762337868.variants.1345513440.price: float
$.products.1762337868.variants.1345513440.product_id: str
$.products.1762337868.variants.2872451762: dict
$.products.1762337868.variants.2872451762.available: bool
$.products.1762337868.variants.2872451762.item_id: str
$.products.1762337868.variants.2872451762.name: str
$.products.1762337868.variants.2872451762.options: dict
$.products.1762337868.variants.2872451762.options.bagged/bagless: str
$.products.1762337868.variants.2872451762.options.features: str
$.products.1762337868.variants.2872451762.options.type: str
$.products.1762337868.variants.2872451762.price: float
$.products.1762337868.variants.2872451762.product_id: str
$.products.1762337868.variants.3019027053: dict
$.products.1762337868.variants.3019027053.available: bool
$.products.1762337868.variants.3019027053.item_id: str
$.products.1762337868.variants.3019027053.options: dict
$.products.1762337868.variants.3019027053.options.bagged/bagless: str
$.products.1762337868.variants.3019027053.options.features: str
$.products.1762337868.variants.3019027053.options.type: str
$.products.1762337868.variants.3019027053.price: float
$.products.1762337868.variants.3526747930: dict
$.products.1762337868.variants.3526747930.available: bool
$.products.1762337868.variants.3526747930.item_id: str
$.products.1762337868.variants.3526747930.name: str
$.products.1762337868.variants.3526747930.options: dict
$.products.1762337868.variants.3526747930.options.bagged/bagless: str
$.products.1762337868.variants.3526747930.options.features: str
$.products.1762337868.variants.3526747930.options.type: str
$.products.1762337868.variants.3526747930.price: float
$.products.1762337868.variants.3526747930.product_id: str
$.products.1762337868.variants.4602305039: dict
$.products.1762337868.variants.4602305039.available: bool
$.products.1762337868.variants.4602305039.item_id: str
$.products.1762337868.variants.4602305039.name: str
$.products.1762337868.variants.4602305039.options: dict
$.products.1762337868.variants.4602305039.options.bagged/bagless: str
$.products.1762337868.variants.4602305039.options.features: str
$.products.1762337868.variants.4602305039.options.type: str
$.products.1762337868.variants.4602305039.price: float
$.products.1762337868.variants.4602305039.product_id: str
$.products.1762337868.variants.4725166838: dict
$.products.1762337868.variants.4725166838.available: bool
$.products.1762337868.variants.4725166838.item_id: str
$.products.1762337868.variants.4725166838.options: dict
$.products.1762337868.variants.4725166838.options.bagged/bagless: str
$.products.1762337868.variants.4725166838.options.features: str
$.products.1762337868.variants.4725166838.options.type: str
$.products.1762337868.variants.4725166838.price: float
$.products.1762337868.variants.4806644905: dict
$.products.1762337868.variants.4806644905.available: bool
$.products.1762337868.variants.4806644905.item_id: str
$.products.1762337868.variants.4806644905.name: str
$.products.1762337868.variants.4806644905.options: dict
$.products.1762337868.variants.4806644905.options.bagged/bagless: str
$.products.1762337868.variants.4806644905.options.features: str
$.products.1762337868.variants.4806644905.options.type: str
$.products.1762337868.variants.4806644905.price: float
$.products.1762337868.variants.4806644905.product_id: str
$.products.1762337868.variants.4965355367: dict
$.products.1762337868.variants.4965355367.available: bool
$.products.1762337868.variants.4965355367.item_id: str
$.products.1762337868.variants.4965355367.options: dict
$.products.1762337868.variants.4965355367.options.bagged/bagless: str
$.products.1762337868.variants.4965355367.options.features: str
$.products.1762337868.variants.4965355367.options.type: str
$.products.1762337868.variants.4965355367.price: float
$.products.1762337868.variants.6259501109: dict
$.products.1762337868.variants.6259501109.available: bool
$.products.1762337868.variants.6259501109.item_id: str
$.products.1762337868.variants.6259501109.name: str
$.products.1762337868.variants.6259501109.options: dict
$.products.1762337868.variants.6259501109.options.bagged/bagless: str
$.products.1762337868.variants.6259501109.options.features: str
$.products.1762337868.variants.6259501109.options.type: str
$.products.1762337868.variants.6259501109.price: float
$.products.1762337868.variants.6259501109.product_id: str
$.products.1762337868.variants.7407609582: dict
$.products.1762337868.variants.7407609582.available: bool
$.products.1762337868.variants.7407609582.item_id: str
$.products.1762337868.variants.7407609582.name: str
$.products.1762337868.variants.7407609582.options: dict
$.products.1762337868.variants.7407609582.options.bagged/bagless: str
$.products.1762337868.variants.7407609582.options.features: str
$.products.1762337868.variants.7407609582.options.type: str
$.products.1762337868.variants.7407609582.price: float
$.products.1762337868.variants.7407609582.product_id: str
$.products.1762337868.variants.7958300294: dict
... (+3721 lines)
```
- sample: `samples/downloaded_domains_data__retail__secondary_source__env__db.json` (153 KB)

## downloaded_domains_data/retail/secondary_source/env/policy.md

Размер: 6.5 КБ
Тип: текст, 6699 символов, 137 строк
- head: `samples/downloaded_domains_data__retail__secondary_source__env__policy.md.txt`

## downloaded_domains_data/retail/secondary_source/env/schema.json

Размер: 41.6 КБ
Тип: JSON dict (len=7)
Схема:
```
$: dict
$.columns: len~32 | list
$.columns[]: dict
$.columns[].class: str
$.columns[].class_confidence: str
$.columns[].class_reason: str
$.columns[].class_rule: str
$.columns[].classified_by: str
$.columns[].evidence: dict
$.columns[].evidence.actions_of: len~1 | list
$.columns[].evidence.actions_of[]: str
$.columns[].name: str
$.columns[].samples: len~0 | len~1 | len~5 | list
$.columns[].table: str
$.columns[].vocabulary: len~0 | len~2 | len~7 | list
$.columns[].evidence.constant_of: str
$.columns[].evidence.constant_value: dict
$.columns[].evidence.constant_value.Action Camera: str
$.columns[].evidence.constant_value.Air Purifier: str
$.columns[].evidence.constant_value.Backpack: str
$.columns[].evidence.constant_value.Bicycle: str
$.columns[].evidence.constant_value.Bluetooth Speaker: str
$.columns[].evidence.constant_value.Bookshelf: str
$.columns[].evidence.constant_value.Coffee Maker: str
$.columns[].evidence.constant_value.Cycling Helmet: str
$.columns[].evidence.constant_value.Desk Lamp: str
$.columns[].evidence.constant_value.Digital Camera: str
$.columns[].evidence.constant_value.Dumbbell Set: str
$.columns[].evidence.constant_value.E-Reader: str
$.columns[].evidence.constant_value.Electric Kettle: str
$.columns[].evidence.constant_value.Electric Toothbrush: str
$.columns[].evidence.constant_value.Espresso Machine: str
$.columns[].evidence.constant_value.Fleece Jacket: str
$.columns[].evidence.constant_value.Gaming Mouse: str
$.columns[].evidence.constant_value.Garden Hose: str
$.columns[].evidence.constant_value.Grill: str
$.columns[].evidence.constant_value.Headphones: str
$.columns[].evidence.constant_value.Hiking Boots: str
$.columns[].evidence.constant_value.Indoor Security Camera: str
$.columns[].evidence.constant_value.Jigsaw Puzzle: str
$.columns[].evidence.constant_value.LED Light Bulb: str
$.columns[].evidence.constant_value.Laptop: str
$.columns[].evidence.constant_value.Luggage Set: str
$.columns[].evidence.constant_value.Makeup Kit: str
$.columns[].evidence.constant_value.Mechanical Keyboard: str
$.columns[].evidence.constant_value.Notebook: str
$.columns[].evidence.constant_value.Office Chair: str
$.columns[].evidence.constant_value.Patio Umbrella: str
$.columns[].evidence.constant_value.Perfume: str
$.columns[].evidence.constant_value.Pet Bed: str
$.columns[].evidence.constant_value.Portable Charger: str
$.columns[].evidence.constant_value.Running Shoes: str
$.columns[].evidence.constant_value.Skateboard: str
$.columns[].evidence.constant_value.Smart Thermostat: str
$.columns[].evidence.constant_value.Smart Watch: str
$.columns[].evidence.constant_value.Smartphone: str
$.columns[].evidence.constant_value.Sneakers: str
$.columns[].evidence.constant_value.Sunglasses: str
$.columns[].evidence.constant_value.T-Shirt: str
$.columns[].evidence.constant_value.Tablet: str
$.columns[].evidence.constant_value.Tea Kettle: str
$.columns[].evidence.constant_value.Vacuum Cleaner: str
$.columns[].evidence.constant_value.Wall Clock: str
$.columns[].evidence.constant_value.Water Bottle: str
$.columns[].evidence.constant_value.Wireless Earbuds: str
$.columns[].evidence.constant_value.Wristwatch: str
$.columns[].evidence.constant_value.Yoga Mat: str
$.columns[].samples[]: NoneType | bool | dict | float | str
$.columns[].samples[].Action Camera: str
$.columns[].samples[].Air Purifier: str
$.columns[].samples[].Backpack: str
$.columns[].samples[].Bicycle: str
$.columns[].samples[].Bluetooth Speaker: str
$.columns[].samples[].Bookshelf: str
$.columns[].samples[].Coffee Maker: str
$.columns[].samples[].Cycling Helmet: str
$.columns[].samples[].Desk Lamp: str
$.columns[].samples[].Digital Camera: str
$.columns[].samples[].Dumbbell Set: str
$.columns[].samples[].E-Reader: str
$.columns[].samples[].Electric Kettle: str
$.columns[].samples[].Electric Toothbrush: str
$.columns[].samples[].Espresso Machine: str
$.columns[].samples[].Fleece Jacket: str
$.columns[].samples[].Gaming Mouse: str
$.columns[].samples[].Garden Hose: str
$.columns[].samples[].Grill: str
$.columns[].samples[].Headphones: str
$.columns[].samples[].Hiking Boots: str
$.columns[].samples[].Indoor Security Camera: str
$.columns[].samples[].Jigsaw Puzzle: str
$.columns[].samples[].LED Light Bulb: str
$.columns[].samples[].Laptop: str
$.columns[].samples[].Luggage Set: str
$.columns[].samples[].Makeup Kit: str
$.columns[].samples[].Mechanical Keyboard: str
$.columns[].samples[].Notebook: str
$.columns[].samples[].Office Chair: str
$.columns[].samples[].Patio Umbrella: str
$.columns[].samples[].Perfume: str
$.columns[].samples[].Pet Bed: str
$.columns[].samples[].Portable Charger: str
$.columns[].samples[].Running Shoes: str
$.columns[].samples[].Skateboard: str
$.columns[].samples[].Smart Thermostat: str
$.columns[].samples[].Smart Watch: str
$.columns[].samples[].Smartphone: str
$.columns[].samples[].Sneakers: str
$.columns[].samples[].Sunglasses: str
$.columns[].samples[].T-Shirt: str
$.columns[].samples[].Tablet: str
$.columns[].samples[].Tea Kettle: str
$.columns[].samples[].Vacuum Cleaner: str
$.columns[].samples[].Wall Clock: str
$.columns[].samples[].Water Bottle: str
$.columns[].samples[].Wireless Earbuds: str
$.columns[].samples[].Wristwatch: str
$.columns[].samples[].Yoga Mat: str
$.columns[].evidence.class_basis: str
$.columns[].evidence.class_contradicts_name: bool
$.columns[].evidence.class_support: len~0 | len~5 | list
$.columns[].evidence.class_support_count: int
$.columns[].evidence.count: int
$.columns[].evidence.distinct: int
$.columns[].evidence.max_len: int
$.columns[].evidence.monotonic: bool
$.columns[].evidence.sampled: int
$.columns[].evidence.types: len~1 | len~2 | list
$.columns[].evidence.types[]: str
$.columns[].evidence.class_support[]: len~2 | list
$.columns[].evidence.class_support[][]: int | str
$.columns[].evidence.id_basis: str
$.columns[].evidence.id_contradicts_name: bool
$.columns[].evidence.id_fact: bool
$.columns[].evidence.id_support: len~0 | len~5 | list
$.columns[].evidence.id_support[]: len~2 | list
$.columns[].evidence.id_support[][]: int | str
$.columns[].evidence.id_support_count: int
$.columns[].evidence.table_basis: str
$.columns[].vocabulary[]: str
$.composite_keys: dict
$.homes: dict
$.homes.items: str
$.id_patterns: dict
$.id_patterns.items.item_id: str
$.id_patterns.orders.order_id: str
$.id_patterns.orders.user_id: str
$.id_patterns.products.product_id: str
$.id_patterns.users.user_id: str
$.key_separator: str
$.synthetic_rows: len~160 | list
$.synthetic_rows[]: str
$.tables: len~6 | list
$.tables[]: str
```
- sample: `samples/downloaded_domains_data__retail__secondary_source__env__schema.json` (37 KB)

## downloaded_domains_data/retail/secondary_source/env/sidecar.json

Размер: 1434.2 КБ
Тип: JSON dict (len=11)
Схема:
```
$: dict
$.env_id: str
$.schema_version: str
$.tools_version: str
$.policy_version: str
$.files: dict
$.files.data_model.py: str
$.files.tools.py: str
$.files.db.json: str
$.files.policy.md: str
$.files.tasks.json: str
$.assisted_tools: len~4 | list
$.assisted_tools[]: str
$.assumptions: len~634 | list
$.assumptions[]: str
$.synthetic_rows: len~186 | list
$.synthetic_rows[]: str
$.overlays: len~209 | list
$.overlays[]: dict
$.overlays[].task_id: str
$.overlays[].rows: len~12 | len~13 | len~14 | len~15 | len~16 | len~17 | len~18 | len~19 | len~20 | len~22 | len~24 | len~26 | len~27 | len~28 | len~30 | len~31 | len~36 | len~37 | len~39 | len~41 | len~44 | len~5 | len~53 | len~6 | len~7 | len~9 | list
$.overlays[].rows[]: dict
$.overlays[].rows[].table: str
$.overlays[].rows[].id: str
$.overlays[].rows[].version_hash: str
$.overlays[].rows[].trace_id: str
$.overlays[].rows[].after_write: bool
$.atoms: dict
$.revealed_by: dict
```
- sample: `samples/downloaded_domains_data__retail__secondary_source__env__sidecar.json` (230 KB)

## downloaded_domains_data/retail/secondary_source/env/tasks/task_018a626ff6c9.json (в папке 245 файлов *.json; взяты первые 2)

Размер: 0.2 КБ
Тип: JSON dict (len=7)
Схема:
```
$: dict
$.anchor_run_ids: len~0 | list
$.category_id: str
$.id: str
$.intent: NoneType
$.name: NoneType
$.run_ids: len~1 | list
$.run_ids[]: str
$.unguarded: bool
```
- sample: `samples/downloaded_domains_data__retail__secondary_source__env__tasks__task_018a626ff6c9.json` (0 KB)

## downloaded_domains_data/retail/secondary_source/env/tasks/task_01d506ce7c9e.json (в папке 245 файлов *.json; взяты первые 2)

Размер: 0.3 КБ
Тип: JSON dict (len=7)
Схема:
```
$: dict
$.anchor_run_ids: len~0 | list
$.category_id: str
$.id: str
$.intent: NoneType
$.name: NoneType
$.run_ids: len~4 | list
$.run_ids[]: str
$.unguarded: bool
```
- sample: `samples/downloaded_domains_data__retail__secondary_source__env__tasks__task_01d506ce7c9e.json` (0 KB)

## downloaded_domains_data/retail/secondary_source/env/tasks.json

Размер: 94.7 КБ
Тип: JSON list (len=209)
Схема:
```
$: len~209 | list
$[]: dict
$[].id: str
$[].description: dict
$[].description.purpose: NoneType
$[].description.relevant_policies: NoneType
$[].description.notes: NoneType
$[].user_scenario: dict
$[].user_scenario.persona: NoneType
$[].user_scenario.instructions: dict
$[].user_scenario.instructions.task_instructions: NoneType
$[].user_scenario.instructions.domain: str
$[].user_scenario.instructions.reason_for_call: NoneType
$[].user_scenario.instructions.known_info: NoneType
$[].user_scenario.instructions.unknown_info: NoneType
$[].initial_state: NoneType
$[].evaluation_criteria: dict
$[].evaluation_criteria.actions: len~0 | list
```
- sample: `samples/downloaded_domains_data__retail__secondary_source__env__tasks.json` (0 KB)

## downloaded_domains_data/retail/secondary_source/env/tool_sigs.json

Размер: 178.0 КБ
Тип: JSON list (len=16)
Схема:
```
$: len~16 | list
$[]: dict
$[].args_fields: len~0 | len~1 | len~2 | len~3 | len~4 | len~7 | list
$[].args_fields[]: dict
$[].args_fields[].count: int
$[].args_fields[].declared: bool
$[].args_fields[].first_seen: str
$[].args_fields[].last_seen: str
$[].args_fields[].name: str
$[].args_fields[].optional: bool
$[].args_fields[].types: len~1 | list
$[].args_fields[].types[]: str
$[].args_schema: dict
$[].args_schema.properties: dict
$[].args_schema.properties.expression: dict
$[].args_schema.properties.expression.type: len~1 | list
$[].args_schema.properties.expression.type[]: str
$[].args_schema.required: len~0 | len~1 | len~2 | len~3 | len~4 | len~7 | list
$[].args_schema.required[]: str
$[].args_schema.type: str
$[].callers: len~1 | list
$[].callers[]: str
$[].classified_by: str
$[].description: NoneType
$[].effects_observed: len~0 | len~20 | list
$[].error_shapes: len~0 | len~1 | list
$[].evidence: len~105 | len~107 | len~123 | len~19 | len~20 | len~27 | len~276 | len~31 | len~349 | len~38 | len~4 | len~423 | len~446 | len~56 | len~66 | len~81 | list
$[].evidence[]: str
$[].evidence_strength: dict
$[].evidence_strength.call_count: int
$[].evidence_strength.error_count: int
$[].evidence_strength.trace_count: int
$[].kind: str
$[].kind_confidence: str
$[].kind_reason: str
$[].name: str
$[].refused_callers: len~0 | list
$[].result_schema: len~1 | len~14 | len~3 | len~4 | len~50 | len~6 | list
$[].result_schema[]: dict
$[].result_schema[].count: int
$[].result_schema[].declared: bool
$[].result_schema[].first_seen: str
$[].result_schema[].last_seen: str
$[].result_schema[].name: str
$[].result_schema[].optional: bool
$[].result_schema[].types: len~1 | list
$[].result_schema[].types[]: str
$[].source: str
$[].unclassified: bool
$[].args_schema.properties.order_id: dict
$[].args_schema.properties.order_id.type: len~1 | list
$[].args_schema.properties.order_id.type[]: str
$[].args_schema.properties.reason: dict
$[].args_schema.properties.reason.type: len~1 | list
$[].args_schema.properties.reason.type[]: str
$[].args_schema.properties.item_ids: dict
$[].args_schema.properties.item_ids.type: len~1 | list
$[].args_schema.properties.item_ids.type[]: str
$[].args_schema.properties.new_item_ids: dict
$[].args_schema.properties.new_item_ids.type: len~1 | list
$[].args_schema.properties.new_item_ids.type[]: str
$[].args_schema.properties.payment_method_id: dict
$[].args_schema.properties.payment_method_id.type: len~1 | list
$[].args_schema.properties.payment_method_id.type[]: str
$[].error_shapes[]: dict
$[].error_shapes[].class: str
$[].error_shapes[].count: int
$[].error_shapes[].encoding: str
$[].error_shapes[].sample_payload: str
$[].args_schema.properties.email: dict
$[].args_schema.properties.email.type: len~1 | list
$[].args_schema.properties.email.type[]: str
$[].args_schema.properties.first_name: dict
$[].args_schema.properties.first_name.type: len~1 | list
$[].args_schema.properties.first_name.type[]: str
$[].args_schema.properties.last_name: dict
$[].args_schema.properties.last_name.type: len~1 | list
$[].args_schema.properties.last_name.type[]: str
$[].args_schema.properties.zip: dict
$[].args_schema.properties.zip.type: len~1 | list
$[].args_schema.properties.zip.type[]: str
$[].args_schema.properties.item_id: dict
$[].args_schema.properties.item_id.type: len~1 | list
$[].args_schema.properties.item_id.type[]: str
$[].args_schema.properties.product_id: dict
$[].args_schema.properties.product_id.type: len~1 | list
$[].args_schema.properties.product_id.type[]: str
$[].args_schema.properties.user_id: dict
$[].args_schema.properties.user_id.type: len~1 | list
$[].args_schema.properties.user_id.type[]: str
$[].args_schema.properties.address1: dict
$[].args_schema.properties.address1.type: len~1 | list
$[].args_schema.properties.address1.type[]: str
$[].args_schema.properties.address2: dict
$[].args_schema.properties.address2.type: len~1 | list
$[].args_schema.properties.address2.type[]: str
$[].args_schema.properties.city: dict
$[].args_schema.properties.city.type: len~1 | list
$[].args_schema.properties.city.type[]: str
$[].args_schema.properties.country: dict
$[].args_schema.properties.country.type: len~1 | list
$[].args_schema.properties.country.type[]: str
$[].args_schema.properties.state: dict
$[].args_schema.properties.state.type: len~1 | list
$[].args_schema.properties.state.type[]: str
$[].effects_observed[]: dict
$[].effects_observed[].field: str
$[].effects_observed[].note: str
$[].effects_observed[].trace_id: str
$[].args_schema.properties.summary: dict
$[].args_schema.properties.summary.type: len~1 | list
$[].args_schema.properties.summary.type[]: str
```
- sample: `samples/downloaded_domains_data__retail__secondary_source__env__tool_sigs.json` (9 KB)

## downloaded_domains_data/retail/secondary_source/env/tools/calculate.py (в папке 16 файлов *.py; взяты первые 2)

Размер: 0.9 КБ
Тип: текст, 939 символов, 13 строк
Определения (1): calculate
- head: `samples/downloaded_domains_data__retail__secondary_source__env__tools__calculate.py.txt`

## downloaded_domains_data/retail/secondary_source/env/tools/cancel_pending_order.py (в папке 16 файлов *.py; взяты первые 2)

Размер: 1.0 КБ
Тип: текст, 1034 символов, 23 строк
Определения (1): cancel_pending_order
- head: `samples/downloaded_domains_data__retail__secondary_source__env__tools__cancel_pending_order.py.txt`

## downloaded_domains_data/retail/secondary_source/env/tools.py

Размер: 35.7 КБ
Тип: текст, 36524 символов, 812 строк
Определения (45): _ToolKitBase, __init__, ToolType, is_tool, decorate, ToolContext, __init__, set_clock, begin_call, turn, _snapshot_starting_ids, _table_keys, _snapshot_starting_times, feed_call, _created_exempt, attach_recorded, reseed, usage, now, random, new_id, _draw, _seeded_now, _mint, _shape_of, _broaden, _draw_id, DomainTools, __init__, calculate, cancel_pending_order, exchange_delivered_order_items, find_user_id_by_email, find_user_id_by_name_zip, get_item_details, get_order_details, get_product_details, get_user_details, list_all_product_types, modify_pending_order_address, modify_pending_order_items, modify_pending_order_payment, modify_user_address, return_delivered_order_items, transfer_to_human_agents
- head: `samples/downloaded_domains_data__retail__secondary_source__env__tools.py.txt`

## downloaded_domains_data/retail/secondary_source/overlays/task_000ffeb205cd.json (в папке 458 файлов *.json; взяты первые 2)

Размер: 5.8 КБ
Тип: JSON dict (len=2)
Схема:
```
$: dict
$.overlay: dict
$.overlay.rows: len~6 | list
$.overlay.rows[]: dict
$.overlay.rows[].after_write: bool
$.overlay.rows[].id: str
$.overlay.rows[].table: str
$.overlay.rows[].trace_id: str
$.overlay.rows[].version_hash: str
$.overlay.task_id: str
$.values: dict
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d: dict
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.address: dict
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.address.address1: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.address.address2: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.address.city: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.address.country: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.address.state: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.address.zip: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.cancel_reason: NoneType
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.exchange_items: NoneType
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.exchange_new_items: NoneType
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.exchange_payment_method_id: NoneType
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.exchange_price_difference: NoneType
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.fulfillments: len~1 | list
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.fulfillments[]: dict
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.fulfillments[].item_ids: len~5 | list
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.fulfillments[].item_ids[]: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.fulfillments[].tracking_id: len~1 | list
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.fulfillments[].tracking_id[]: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.items: len~5 | list
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.items[]: dict
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.items[].item_id: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.items[].name: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.items[].options: dict
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.items[].options.bagged/bagless: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.items[].options.features: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.items[].options.type: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.items[].price: float
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.items[].product_id: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.items[].options.filter type: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.items[].options.room size: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.items[].options.color: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.items[].options.material: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.items[].options.size: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.items[].options.tilt mechanism: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.items[].options.set type: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.items[].options.weight range: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.order_id: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.payment_history: len~1 | list
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.payment_history[]: dict
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.payment_history[].amount: float
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.payment_history[].payment_method_id: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.payment_history[].transaction_type: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.return_items: NoneType
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.return_payment_method_id: NoneType
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.status: str
$.values.19758b0e248b2582757f80314bb7aca036ad2bf96450a4e10d57a47b3f28490d.user_id: str
$.values.bfd0d222adaf5adb40ade2071dc635a06331b0a3536dcdb2401c4d3504881257: dict
$.values.bfd0d222adaf5adb40ade2071dc635a06331b0a3536dcdb2401c4d3504881257.item_id: str
$.values.bfd0d222adaf5adb40ade2071dc635a06331b0a3536dcdb2401c4d3504881257.name: str
$.values.bfd0d222adaf5adb40ade2071dc635a06331b0a3536dcdb2401c4d3504881257.options: dict
$.values.bfd0d222adaf5adb40ade2071dc635a06331b0a3536dcdb2401c4d3504881257.options.bagged/bagless: str
$.values.bfd0d222adaf5adb40ade2071dc635a06331b0a3536dcdb2401c4d3504881257.options.features: str
$.values.bfd0d222adaf5adb40ade2071dc635a06331b0a3536dcdb2401c4d3504881257.options.type: str
$.values.bfd0d222adaf5adb40ade2071dc635a06331b0a3536dcdb2401c4d3504881257.price: float
$.values.bfd0d222adaf5adb40ade2071dc635a06331b0a3536dcdb2401c4d3504881257.product_id: str
$.values.c1be2182666bb49dbb73a09be74c8df2bf187d5c73fc5acdfc523bf474bae99e: dict
$.values.c1be2182666bb49dbb73a09be74c8df2bf187d5c73fc5acdfc523bf474bae99e.item_id: str
$.values.c1be2182666bb49dbb73a09be74c8df2bf187d5c73fc5acdfc523bf474bae99e.name: str
$.values.c1be2182666bb49dbb73a09be74c8df2bf187d5c73fc5acdfc523bf474bae99e.options: dict
$.values.c1be2182666bb49dbb73a09be74c8df2bf187d5c73fc5acdfc523bf474bae99e.options.features: str
$.values.c1be2182666bb49dbb73a09be74c8df2bf187d5c73fc5acdfc523bf474bae99e.options.filter type: str
$.values.c1be2182666bb49dbb73a09be74c8df2bf187d5c73fc5acdfc523bf474bae99e.options.room size: str
$.values.c1be2182666bb49dbb73a09be74c8df2bf187d5c73fc5acdfc523bf474bae99e.price: float
$.values.c1be2182666bb49dbb73a09be74c8df2bf187d5c73fc5acdfc523bf474bae99e.product_id: str
$.values.c25fb3163f00fb9783c1dd5fe1fd72dca522ae5f3176aa32610c96dff5992c20: dict
$.values.c25fb3163f00fb9783c1dd5fe1fd72dca522ae5f3176aa32610c96dff5992c20.item_id: str
$.values.c25fb3163f00fb9783c1dd5fe1fd72dca522ae5f3176aa32610c96dff5992c20.name: str
$.values.c25fb3163f00fb9783c1dd5fe1fd72dca522ae5f3176aa32610c96dff5992c20.options: dict
$.values.c25fb3163f00fb9783c1dd5fe1fd72dca522ae5f3176aa32610c96dff5992c20.options.bagged/bagless: str
$.values.c25fb3163f00fb9783c1dd5fe1fd72dca522ae5f3176aa32610c96dff5992c20.options.features: str
$.values.c25fb3163f00fb9783c1dd5fe1fd72dca522ae5f3176aa32610c96dff5992c20.options.type: str
$.values.c25fb3163f00fb9783c1dd5fe1fd72dca522ae5f3176aa32610c96dff5992c20.price: float
$.values.c25fb3163f00fb9783c1dd5fe1fd72dca522ae5f3176aa32610c96dff5992c20.product_id: str
$.values.db2a57f801b464677998c0fa79f9d45438f9606105bb9f835f3e78d7b7efc2b6: dict
$.values.db2a57f801b464677998c0fa79f9d45438f9606105bb9f835f3e78d7b7efc2b6.item_id: str
$.values.db2a57f801b464677998c0fa79f9d45438f9606105bb9f835f3e78d7b7efc2b6.name: str
$.values.db2a57f801b464677998c0fa79f9d45438f9606105bb9f835f3e78d7b7efc2b6.options: dict
$.values.db2a57f801b464677998c0fa79f9d45438f9606105bb9f835f3e78d7b7efc2b6.options.color: str
$.values.db2a57f801b464677998c0fa79f9d45438f9606105bb9f835f3e78d7b7efc2b6.options.material: str
$.values.db2a57f801b464677998c0fa79f9d45438f9606105bb9f835f3e78d7b7efc2b6.options.size: str
$.values.db2a57f801b464677998c0fa79f9d45438f9606105bb9f835f3e78d7b7efc2b6.options.tilt mechanism: str
$.values.db2a57f801b464677998c0fa79f9d45438f9606105bb9f835f3e78d7b7efc2b6.price: float
$.values.db2a57f801b464677998c0fa79f9d45438f9606105bb9f835f3e78d7b7efc2b6.product_id: str
$.values.ff6f97b869791de3fd60406850d153f996a0f7999fa1c6a22cfb004f96d3439b: dict
$.values.ff6f97b869791de3fd60406850d153f996a0f7999fa1c6a22cfb004f96d3439b.item_id: str
$.values.ff6f97b869791de3fd60406850d153f996a0f7999fa1c6a22cfb004f96d3439b.name: str
$.values.ff6f97b869791de3fd60406850d153f996a0f7999fa1c6a22cfb004f96d3439b.options: dict
$.values.ff6f97b869791de3fd60406850d153f996a0f7999fa1c6a22cfb004f96d3439b.options.material: str
$.values.ff6f97b869791de3fd60406850d153f996a0f7999fa1c6a22cfb004f96d3439b.options.set type: str
$.values.ff6f97b869791de3fd60406850d153f996a0f7999fa1c6a22cfb004f96d3439b.options.weight range: str
$.values.ff6f97b869791de3fd60406850d153f996a0f7999fa1c6a22cfb004f96d3439b.price: float
$.values.ff6f97b869791de3fd60406850d153f996a0f7999fa1c6a22cfb004f96d3439b.product_id: str
```
- sample: `samples/downloaded_domains_data__retail__secondary_source__overlays__task_000ffeb205cd.json` (5 KB)

## downloaded_domains_data/retail/secondary_source/overlays/task_018a626ff6c9.json (в папке 458 файлов *.json; взяты первые 2)

Размер: 11.4 КБ
Тип: JSON dict (len=4)
Схема:
```
$: dict
$.overlay: dict
$.overlay.rows: len~12 | list
$.overlay.rows[]: dict
$.overlay.rows[].after_write: bool
$.overlay.rows[].id: str
$.overlay.rows[].table: str
$.overlay.rows[].trace_id: str
$.overlay.rows[].version_hash: str
$.overlay.steps: len~0 | list
$.overlay.task_id: str
$.reference_run_id: str
$.runs: dict
$.values: dict
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef: dict
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef.address: dict
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef.address.address1: str
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef.address.address2: str
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef.address.city: str
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef.address.country: str
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef.address.state: str
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef.address.zip: str
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef.email: str
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef.name: dict
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef.name.first_name: str
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef.name.last_name: str
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef.orders: len~2 | list
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef.orders[]: str
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef.payment_methods: dict
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef.payment_methods.paypal_3820631: dict
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef.payment_methods.paypal_3820631.id: str
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef.payment_methods.paypal_3820631.source: str
$.values.1cbdbfd6c141bfbdc38c34890d048797ccf95d26edfc1c160a6fccc2dab7b8ef.user_id: str
$.values.52fe2ffebfc1f66b6fb1e686ba1c4ec3c5743be29af85daf7228ab6b849a95eb: dict
$.values.52fe2ffebfc1f66b6fb1e686ba1c4ec3c5743be29af85daf7228ab6b849a95eb.item_id: str
$.values.52fe2ffebfc1f66b6fb1e686ba1c4ec3c5743be29af85daf7228ab6b849a95eb.name: str
$.values.52fe2ffebfc1f66b6fb1e686ba1c4ec3c5743be29af85daf7228ab6b849a95eb.options: dict
$.values.52fe2ffebfc1f66b6fb1e686ba1c4ec3c5743be29af85daf7228ab6b849a95eb.options.capacity: str
$.values.52fe2ffebfc1f66b6fb1e686ba1c4ec3c5743be29af85daf7228ab6b849a95eb.options.color: str
$.values.52fe2ffebfc1f66b6fb1e686ba1c4ec3c5743be29af85daf7228ab6b849a95eb.options.material: str
$.values.52fe2ffebfc1f66b6fb1e686ba1c4ec3c5743be29af85daf7228ab6b849a95eb.price: float
$.values.52fe2ffebfc1f66b6fb1e686ba1c4ec3c5743be29af85daf7228ab6b849a95eb.product_id: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af: dict
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.address: dict
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.address.address1: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.address.address2: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.address.city: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.address.country: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.address.state: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.address.zip: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.cancel_reason: NoneType
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.exchange_items: NoneType
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.exchange_new_items: NoneType
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.exchange_payment_method_id: NoneType
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.exchange_price_difference: NoneType
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.fulfillments: len~1 | list
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.fulfillments[]: dict
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.fulfillments[].item_ids: len~4 | list
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.fulfillments[].item_ids[]: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.fulfillments[].tracking_id: len~1 | list
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.fulfillments[].tracking_id[]: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.items: len~4 | list
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.items[]: dict
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.items[].item_id: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.items[].name: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.items[].options: dict
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.items[].options.color: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.items[].options.size: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.items[].options.ventilation: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.items[].price: float
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.items[].product_id: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.items[].options.capacity: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.items[].options.material: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.items[].options.battery life: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.items[].options.water resistance: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.items[].options.battery type: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.items[].options.speed settings: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.order_id: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.payment_history: len~2 | list
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.payment_history[]: dict
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.payment_history[].amount: float
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.payment_history[].payment_method_id: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.payment_history[].transaction_type: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.return_items: NoneType
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.return_payment_method_id: NoneType
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.status: str
$.values.56d7a7ad3b08cfa754375104eaaa803d7cf9eb080cf3c750c5faab4e5a2bb4af.user_id: str
$.values.6dafe90d42bbce4dd5c52a919c423ce0097829513257cc257bc9427e0d3e6e53: dict
$.values.6dafe90d42bbce4dd5c52a919c423ce0097829513257cc257bc9427e0d3e6e53.item_id: str
$.values.6dafe90d42bbce4dd5c52a919c423ce0097829513257cc257bc9427e0d3e6e53.name: str
$.values.6dafe90d42bbce4dd5c52a919c423ce0097829513257cc257bc9427e0d3e6e53.options: dict
$.values.6dafe90d42bbce4dd5c52a919c423ce0097829513257cc257bc9427e0d3e6e53.options.color: str
$.values.6dafe90d42bbce4dd5c52a919c423ce0097829513257cc257bc9427e0d3e6e53.options.resolution: str
$.values.6dafe90d42bbce4dd5c52a919c423ce0097829513257cc257bc9427e0d3e6e53.options.waterproof: str
$.values.6dafe90d42bbce4dd5c52a919c423ce0097829513257cc257bc9427e0d3e6e53.price: float
$.values.6dafe90d42bbce4dd5c52a919c423ce0097829513257cc257bc9427e0d3e6e53.product_id: str
$.values.7922aecb5cc9c75ad1f450e78380369cee4fb619a6df09520c97f97e71ccbfcd: dict
$.values.7922aecb5cc9c75ad1f450e78380369cee4fb619a6df09520c97f97e71ccbfcd.item_id: str
$.values.7922aecb5cc9c75ad1f450e78380369cee4fb619a6df09520c97f97e71ccbfcd.name: str
$.values.7922aecb5cc9c75ad1f450e78380369cee4fb619a6df09520c97f97e71ccbfcd.options: dict
$.values.7922aecb5cc9c75ad1f450e78380369cee4fb619a6df09520c97f97e71ccbfcd.options.bagged/bagless: str
$.values.7922aecb5cc9c75ad1f450e78380369cee4fb619a6df09520c97f97e71ccbfcd.options.features: str
$.values.7922aecb5cc9c75ad1f450e78380369cee4fb619a6df09520c97f97e71ccbfcd.options.type: str
$.values.7922aecb5cc9c75ad1f450e78380369cee4fb619a6df09520c97f97e71ccbfcd.price: float
$.values.7922aecb5cc9c75ad1f450e78380369cee4fb619a6df09520c97f97e71ccbfcd.product_id: str
$.values.956893114d4ea47e35194d57483497bb703e58776ed9f7798ed95ad7ad320588: dict
$.values.956893114d4ea47e35194d57483497bb703e58776ed9f7798ed95ad7ad320588.item_id: str
$.values.956893114d4ea47e35194d57483497bb703e58776ed9f7798ed95ad7ad320588.name: str
$.values.956893114d4ea47e35194d57483497bb703e58776ed9f7798ed95ad7ad320588.options: dict
$.values.956893114d4ea47e35194d57483497bb703e58776ed9f7798ed95ad7ad320588.options.battery life: str
$.values.956893114d4ea47e35194d57483497bb703e58776ed9f7798ed95ad7ad320588.options.color: str
$.values.956893114d4ea47e35194d57483497bb703e58776ed9f7798ed95ad7ad320588.options.water resistance: str
$.values.956893114d4ea47e35194d57483497bb703e58776ed9f7798ed95ad7ad320588.price: float
$.values.956893114d4ea47e35194d57483497bb703e58776ed9f7798ed95ad7ad320588.product_id: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25: dict
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.address: dict
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.address.address1: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.address.address2: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.address.city: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.address.country: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.address.state: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.address.zip: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.cancel_reason: NoneType
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.exchange_items: NoneType
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.exchange_new_items: NoneType
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.exchange_payment_method_id: NoneType
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.exchange_price_difference: NoneType
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.fulfillments: len~1 | list
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.fulfillments[]: dict
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.fulfillments[].item_ids: len~5 | list
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.fulfillments[].item_ids[]: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.fulfillments[].tracking_id: len~1 | list
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.fulfillments[].tracking_id[]: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items: len~5 | list
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items[]: dict
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items[].item_id: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items[].name: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items[].options: dict
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items[].options.color: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items[].options.screen size: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items[].options.storage: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items[].price: float
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items[].product_id: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items[].options.resolution: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items[].options.waterproof: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items[].options.backlight: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items[].options.size: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items[].options.switch type: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items[].options.bagged/bagless: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items[].options.features: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items[].options.type: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.items[].options.compatibility: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.order_id: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.payment_history: len~1 | list
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.payment_history[]: dict
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.payment_history[].amount: float
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.payment_history[].payment_method_id: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.payment_history[].transaction_type: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.return_items: NoneType
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.return_payment_method_id: NoneType
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.status: str
$.values.a1e5c9d44e60a21359737236f6dd2f04cf20429df88f7916cad95f47b42bfa25.user_id: str
$.values.bfde1168c0c4517bdcebb6f385d8ef1f39df72e9ccf539802112deefaef8270e: dict
$.values.bfde1168c0c4517bdcebb6f385d8ef1f39df72e9ccf539802112deefaef8270e.item_id: str
$.values.bfde1168c0c4517bdcebb6f385d8ef1f39df72e9ccf539802112deefaef8270e.name: str
$.values.bfde1168c0c4517bdcebb6f385d8ef1f39df72e9ccf539802112deefaef8270e.options: dict
$.values.bfde1168c0c4517bdcebb6f385d8ef1f39df72e9ccf539802112deefaef8270e.options.color: str
$.values.bfde1168c0c4517bdcebb6f385d8ef1f39df72e9ccf539802112deefaef8270e.options.size: str
$.values.bfde1168c0c4517bdcebb6f385d8ef1f39df72e9ccf539802112deefaef8270e.options.ventilation: str
$.values.bfde1168c0c4517bdcebb6f385d8ef1f39df72e9ccf539802112deefaef8270e.price: float
$.values.bfde1168c0c4517bdcebb6f385d8ef1f39df72e9ccf539802112deefaef8270e.product_id: str
$.values.e766b08dd73bbf7561b63dada113337466d6a71fe1f0e5975581903ac296514d: dict
$.values.e766b08dd73bbf7561b63dada113337466d6a71fe1f0e5975581903ac296514d.item_id: str
$.values.e766b08dd73bbf7561b63dada113337466d6a71fe1f0e5975581903ac296514d.name: str
$.values.e766b08dd73bbf7561b63dada113337466d6a71fe1f0e5975581903ac296514d.options: dict
$.values.e766b08dd73bbf7561b63dada113337466d6a71fe1f0e5975581903ac296514d.options.color: str
$.values.e766b08dd73bbf7561b63dada113337466d6a71fe1f0e5975581903ac296514d.options.screen size: str
$.values.e766b08dd73bbf7561b63dada113337466d6a71fe1f0e5975581903ac296514d.options.storage: str
$.values.e766b08dd73bbf7561b63dada113337466d6a71fe1f0e5975581903ac296514d.price: float
$.values.e766b08dd73bbf7561b63dada113337466d6a71fe1f0e5975581903ac296514d.product_id: str
$.values.ee201cc4f3a007ddfd30fff80dfb0263cfdecf83a35f7f59758fb3aa0e776d3c: dict
$.values.ee201cc4f3a007ddfd30fff80dfb0263cfdecf83a35f7f59758fb3aa0e776d3c.item_id: str
$.values.ee201cc4f3a007ddfd30fff80dfb0263cfdecf83a35f7f59758fb3aa0e776d3c.name: str
$.values.ee201cc4f3a007ddfd30fff80dfb0263cfdecf83a35f7f59758fb3aa0e776d3c.options: dict
$.values.ee201cc4f3a007ddfd30fff80dfb0263cfdecf83a35f7f59758fb3aa0e776d3c.options.backlight: str
$.values.ee201cc4f3a007ddfd30fff80dfb0263cfdecf83a35f7f59758fb3aa0e776d3c.options.size: str
$.values.ee201cc4f3a007ddfd30fff80dfb0263cfdecf83a35f7f59758fb3aa0e776d3c.options.switch type: str
$.values.ee201cc4f3a007ddfd30fff80dfb0263cfdecf83a35f7f59758fb3aa0e776d3c.price: float
$.values.ee201cc4f3a007ddfd30fff80dfb0263cfdecf83a35f7f59758fb3aa0e776d3c.product_id: str
$.values.f0f535e843dcfcb5d759cbc557731312fdae67b5d8e25ae1d35140e8fbe4c5a3: dict
$.values.f0f535e843dcfcb5d759cbc557731312fdae67b5d8e25ae1d35140e8fbe4c5a3.item_id: str
$.values.f0f535e843dcfcb5d759cbc557731312fdae67b5d8e25ae1d35140e8fbe4c5a3.name: str
$.values.f0f535e843dcfcb5d759cbc557731312fdae67b5d8e25ae1d35140e8fbe4c5a3.options: dict
$.values.f0f535e843dcfcb5d759cbc557731312fdae67b5d8e25ae1d35140e8fbe4c5a3.options.color: str
$.values.f0f535e843dcfcb5d759cbc557731312fdae67b5d8e25ae1d35140e8fbe4c5a3.options.compatibility: str
$.values.f0f535e843dcfcb5d759cbc557731312fdae67b5d8e25ae1d35140e8fbe4c5a3.price: float
$.values.f0f535e843dcfcb5d759cbc557731312fdae67b5d8e25ae1d35140e8fbe4c5a3.product_id: str
$.values.faca434ac850956d0838c6c25af8d26c09806c53449874395059441ebb2a84ec: dict
$.values.faca434ac850956d0838c6c25af8d26c09806c53449874395059441ebb2a84ec.item_id: str
$.values.faca434ac850956d0838c6c25af8d26c09806c53449874395059441ebb2a84ec.name: str
$.values.faca434ac850956d0838c6c25af8d26c09806c53449874395059441ebb2a84ec.options: dict
$.values.faca434ac850956d0838c6c25af8d26c09806c53449874395059441ebb2a84ec.options.battery type: str
$.values.faca434ac850956d0838c6c25af8d26c09806c53449874395059441ebb2a84ec.options.color: str
$.values.faca434ac850956d0838c6c25af8d26c09806c53449874395059441ebb2a84ec.options.speed settings: str
$.values.faca434ac850956d0838c6c25af8d26c09806c53449874395059441ebb2a84ec.price: float
$.values.faca434ac850956d0838c6c25af8d26c09806c53449874395059441ebb2a84ec.product_id: str
```
- sample: `samples/downloaded_domains_data__retail__secondary_source__overlays__task_018a626ff6c9.json` (11 KB)

## downloaded_domains_data/retail/secondary_source/tasks/task_000ffeb205cd.json (в папке 450 файлов *.json; взяты первые 2)

Размер: 0.2 КБ
Тип: JSON dict (len=7)
Схема:
```
$: dict
$.anchor_run_ids: len~0 | list
$.category_id: str
$.id: str
$.intent: str
$.name: NoneType
$.run_ids: len~0 | list
$.unguarded: bool
```
- sample: `samples/downloaded_domains_data__retail__secondary_source__tasks__task_000ffeb205cd.json` (0 KB)

## downloaded_domains_data/retail/secondary_source/tasks/task_018a626ff6c9.json (в папке 450 файлов *.json; взяты первые 2)

Размер: 0.2 КБ
Тип: JSON dict (len=7)
Схема:
```
$: dict
$.anchor_run_ids: len~0 | list
$.category_id: str
$.id: str
$.intent: NoneType
$.name: NoneType
$.run_ids: len~0 | list
$.unguarded: bool
```
- sample: `samples/downloaded_domains_data__retail__secondary_source__tasks__task_018a626ff6c9.json` (0 KB)

## downloaded_domains_data/retail/secondary_source/tasks.jsonl

Размер: 44.9 КБ
Тип: JSONL; прочитано строк: 223 (битых: 0, лимит 20000)
Схема (объединение по первым записям):
```
$: dict
$.bucket: NoneType | str
$.instruction: str
$.recordings: int
$.refused: bool
$.replay_confirmed: bool
$.stage: str
$.stopped_because: NoneType | str
$.task_id: str
$.trusted: bool
```
- sample: `samples/downloaded_domains_data__retail__secondary_source__tasks.jsonl__line0.json` (0 KB)
- sample: `samples/downloaded_domains_data__retail__secondary_source__tasks.jsonl__FULL_line0.json` (0 KB)

## downloaded_domains_data/retail/secondary_source/verifiers/task_000ffeb205cd.json (в папке 444 файлов *.json; взяты первые 2)

Размер: 298.8 КБ
Тип: JSON dict (len=4)
Схема:
```
$: dict
$.atoms: len~46 | list
$.atoms[]: dict
$.atoms[].description: str
$.atoms[].id: str
$.atoms[].judge: bool
$.atoms[].kind: str
$.atoms[].predicate_src: str
$.atoms[].provenance: NoneType
$.atoms[].spans: len~0 | len~1 | list
$.atoms[].spans[]: dict
$.atoms[].spans[].file_hash: str
$.atoms[].spans[].msg_index: int
$.atoms[].spans[].section: NoneType
$.atoms[].spans[].sim_index: NoneType
$.atoms[].target: dict
$.atoms[].target.at: int
$.atoms[].target.entity: str
$.atoms[].target.entity_raw: str
$.atoms[].target.id_field: str
$.atoms[].target.kind: str
$.atoms[].target.tool: str
$.atoms[].target.constraint_id: str
$.atoms[].target.derived_as: str
$.atoms[].target.judge: bool
$.atoms[].target.predicate_src: NoneType | str
$.atoms[].target.read_tools: len~0 | len~4 | list
$.atoms[].target.write_tools: len~7 | list
$.atoms[].target.write_tools[]: str
$.atoms[].target.text: str
$.atoms[].target.value: str
$.atoms[].target.count: int
$.atoms[].target.read_tools[]: str
$.seed_run_ids: len~2 | list
$.seed_run_ids[]: str
$.task_id: str
$.verifier_version: str
```
- sample: `samples/downloaded_domains_data__retail__secondary_source__verifiers__task_000ffeb205cd.json` (147 KB)

## downloaded_domains_data/retail/secondary_source/verifiers/task_018a626ff6c9.json (в папке 444 файлов *.json; взяты первые 2)

Размер: 40.0 КБ
Тип: JSON dict (len=4)
Схема:
```
$: dict
$.atoms: len~21 | list
$.atoms[]: dict
$.atoms[].description: str
$.atoms[].id: str
$.atoms[].judge: bool
$.atoms[].kind: str
$.atoms[].predicate_src: str
$.atoms[].provenance: NoneType | str
$.atoms[].spans: len~0 | len~1 | list
$.atoms[].spans[]: dict
$.atoms[].spans[].file_hash: str
$.atoms[].spans[].msg_index: int
$.atoms[].spans[].section: NoneType
$.atoms[].spans[].sim_index: NoneType
$.atoms[].target: dict
$.atoms[].target.at: int
$.atoms[].target.entity: str
$.atoms[].target.entity_raw: str
$.atoms[].target.id_field: str
$.atoms[].target.kind: str
$.atoms[].target.tool: str
$.atoms[].target.field: NoneType | str
$.atoms[].target.raw: str
$.atoms[].target.value: str
$.atoms[].target.constraint_id: str
$.atoms[].target.derived_as: str
$.atoms[].target.judge: bool
$.atoms[].target.predicate_src: str
$.atoms[].target.read_tools: len~0 | list
$.atoms[].target.shape_source: str
$.atoms[].target.write_tools: len~8 | list
$.atoms[].target.write_tools[]: str
$.atoms[].target.generic: str
$.atoms[].target.source_tool: str
$.atoms[].target.text: str
$.atoms[].target.count: int
$.seed_run_ids: len~3 | list
$.seed_run_ids[]: str
$.task_id: str
$.verifier_version: str
```
- sample: `samples/downloaded_domains_data__retail__secondary_source__verifiers__task_018a626ff6c9.json` (25 KB)

## downloaded_domains_data/retail/tau2_env/db.json

Размер: 2745.7 КБ
Тип: JSON dict (len=3)
Схема:
```
$: dict
$.products: dict
$.products.9523456873: dict
$.products.9523456873.name: str
$.products.9523456873.product_id: str
$.products.9523456873.variants: dict
$.products.9523456873.variants.9612497925: dict
$.products.9523456873.variants.9612497925.item_id: str
$.products.9523456873.variants.9612497925.options: dict
$.products.9523456873.variants.9612497925.options.color: str
$.products.9523456873.variants.9612497925.options.size: str
$.products.9523456873.variants.9612497925.options.material: str
$.products.9523456873.variants.9612497925.options.style: str
$.products.9523456873.variants.9612497925.available: bool
$.products.9523456873.variants.9612497925.price: float
$.products.9523456873.variants.8124970213: dict
$.products.9523456873.variants.8124970213.item_id: str
$.products.9523456873.variants.8124970213.options: dict
$.products.9523456873.variants.8124970213.options.color: str
$.products.9523456873.variants.8124970213.options.size: str
$.products.9523456873.variants.8124970213.options.material: str
$.products.9523456873.variants.8124970213.options.style: str
$.products.9523456873.variants.8124970213.available: bool
$.products.9523456873.variants.8124970213.price: float
$.products.9523456873.variants.9354168549: dict
$.products.9523456873.variants.9354168549.item_id: str
$.products.9523456873.variants.9354168549.options: dict
$.products.9523456873.variants.9354168549.options.color: str
$.products.9523456873.variants.9354168549.options.size: str
$.products.9523456873.variants.9354168549.options.material: str
$.products.9523456873.variants.9354168549.options.style: str
$.products.9523456873.variants.9354168549.available: bool
$.products.9523456873.variants.9354168549.price: float
$.products.9523456873.variants.5253880258: dict
$.products.9523456873.variants.5253880258.item_id: str
$.products.9523456873.variants.5253880258.options: dict
$.products.9523456873.variants.5253880258.options.color: str
$.products.9523456873.variants.5253880258.options.size: str
$.products.9523456873.variants.5253880258.options.material: str
$.products.9523456873.variants.5253880258.options.style: str
$.products.9523456873.variants.5253880258.available: bool
$.products.9523456873.variants.5253880258.price: float
$.products.9523456873.variants.1176194968: dict
$.products.9523456873.variants.1176194968.item_id: str
$.products.9523456873.variants.1176194968.options: dict
$.products.9523456873.variants.1176194968.options.color: str
$.products.9523456873.variants.1176194968.options.size: str
$.products.9523456873.variants.1176194968.options.material: str
$.products.9523456873.variants.1176194968.options.style: str
$.products.9523456873.variants.1176194968.available: bool
$.products.9523456873.variants.1176194968.price: float
$.products.9523456873.variants.9647292434: dict
$.products.9523456873.variants.9647292434.item_id: str
$.products.9523456873.variants.9647292434.options: dict
$.products.9523456873.variants.9647292434.options.color: str
$.products.9523456873.variants.9647292434.options.size: str
$.products.9523456873.variants.9647292434.options.material: str
$.products.9523456873.variants.9647292434.options.style: str
$.products.9523456873.variants.9647292434.available: bool
$.products.9523456873.variants.9647292434.price: float
$.products.9523456873.variants.8349118980: dict
$.products.9523456873.variants.8349118980.item_id: str
$.products.9523456873.variants.8349118980.options: dict
$.products.9523456873.variants.8349118980.options.color: str
$.products.9523456873.variants.8349118980.options.size: str
$.products.9523456873.variants.8349118980.options.material: str
$.products.9523456873.variants.8349118980.options.style: str
$.products.9523456873.variants.8349118980.available: bool
$.products.9523456873.variants.8349118980.price: float
$.products.9523456873.variants.5047954489: dict
$.products.9523456873.variants.5047954489.item_id: str
$.products.9523456873.variants.5047954489.options: dict
$.products.9523456873.variants.5047954489.options.color: str
$.products.9523456873.variants.5047954489.options.size: str
$.products.9523456873.variants.5047954489.options.material: str
$.products.9523456873.variants.5047954489.options.style: str
$.products.9523456873.variants.5047954489.available: bool
$.products.9523456873.variants.5047954489.price: float
$.products.9523456873.variants.3799046073: dict
$.products.9523456873.variants.3799046073.item_id: str
$.products.9523456873.variants.3799046073.options: dict
$.products.9523456873.variants.3799046073.options.color: str
$.products.9523456873.variants.3799046073.options.size: str
$.products.9523456873.variants.3799046073.options.material: str
$.products.9523456873.variants.3799046073.options.style: str
$.products.9523456873.variants.3799046073.available: bool
$.products.9523456873.variants.3799046073.price: float
$.products.9523456873.variants.3234800602: dict
$.products.9523456873.variants.3234800602.item_id: str
$.products.9523456873.variants.3234800602.options: dict
$.products.9523456873.variants.3234800602.options.color: str
$.products.9523456873.variants.3234800602.options.size: str
$.products.9523456873.variants.3234800602.options.material: str
$.products.9523456873.variants.3234800602.options.style: str
$.products.9523456873.variants.3234800602.available: bool
$.products.9523456873.variants.3234800602.price: float
$.products.9523456873.variants.3542102174: dict
$.products.9523456873.variants.3542102174.item_id: str
$.products.9523456873.variants.3542102174.options: dict
$.products.9523456873.variants.3542102174.options.color: str
$.products.9523456873.variants.3542102174.options.size: str
$.products.9523456873.variants.3542102174.options.material: str
$.products.9523456873.variants.3542102174.options.style: str
$.products.9523456873.variants.3542102174.available: bool
$.products.9523456873.variants.3542102174.price: float
$.products.9523456873.variants.2060066974: dict
$.products.9523456873.variants.2060066974.item_id: str
$.products.9523456873.variants.2060066974.options: dict
$.products.9523456873.variants.2060066974.options.color: str
$.products.9523456873.variants.2060066974.options.size: str
$.products.9523456873.variants.2060066974.options.material: str
$.products.9523456873.variants.2060066974.options.style: str
$.products.9523456873.variants.2060066974.available: bool
$.products.9523456873.variants.2060066974.price: float
$.products.4760268021: dict
$.products.4760268021.name: str
$.products.4760268021.product_id: str
$.products.4760268021.variants: dict
$.products.4760268021.variants.8997785118: dict
$.products.4760268021.variants.8997785118.item_id: str
$.products.4760268021.variants.8997785118.options: dict
$.products.4760268021.variants.8997785118.options.screen size: str
$.products.4760268021.variants.8997785118.options.processor: str
$.products.4760268021.variants.8997785118.options.ram: str
$.products.4760268021.variants.8997785118.options.storage: str
$.products.4760268021.variants.8997785118.options.color: str
$.products.4760268021.variants.8997785118.available: bool
$.products.4760268021.variants.8997785118.price: float
$.products.4760268021.variants.2216662955: dict
$.products.4760268021.variants.2216662955.item_id: str
$.products.4760268021.variants.2216662955.options: dict
$.products.4760268021.variants.2216662955.options.screen size: str
$.products.4760268021.variants.2216662955.options.processor: str
$.products.4760268021.variants.2216662955.options.ram: str
$.products.4760268021.variants.2216662955.options.storage: str
$.products.4760268021.variants.2216662955.options.color: str
$.products.4760268021.variants.2216662955.available: bool
$.products.4760268021.variants.2216662955.price: float
$.products.4760268021.variants.2768401027: dict
$.products.4760268021.variants.2768401027.item_id: str
$.products.4760268021.variants.2768401027.options: dict
$.products.4760268021.variants.2768401027.options.screen size: str
$.products.4760268021.variants.2768401027.options.processor: str
$.products.4760268021.variants.2768401027.options.ram: str
$.products.4760268021.variants.2768401027.options.storage: str
$.products.4760268021.variants.2768401027.options.color: str
$.products.4760268021.variants.2768401027.available: bool
$.products.4760268021.variants.2768401027.price: float
$.products.4760268021.variants.1684786391: dict
$.products.4760268021.variants.1684786391.item_id: str
$.products.4760268021.variants.1684786391.options: dict
$.products.4760268021.variants.1684786391.options.screen size: str
$.products.4760268021.variants.1684786391.options.processor: str
$.products.4760268021.variants.1684786391.options.ram: str
$.products.4760268021.variants.1684786391.options.storage: str
$.products.4760268021.variants.1684786391.options.color: str
$.products.4760268021.variants.1684786391.available: bool
$.products.4760268021.variants.1684786391.price: float
$.products.4760268021.variants.3778566150: dict
$.products.4760268021.variants.3778566150.item_id: str
$.products.4760268021.variants.3778566150.options: dict
$.products.4760268021.variants.3778566150.options.screen size: str
$.products.4760268021.variants.3778566150.options.processor: str
$.products.4760268021.variants.3778566150.options.ram: str
$.products.4760268021.variants.3778566150.options.storage: str
$.products.4760268021.variants.3778566150.options.color: str
$.products.4760268021.variants.3778566150.available: bool
$.products.4760268021.variants.3778566150.price: float
$.products.4760268021.variants.8193934556: dict
$.products.4760268021.variants.8193934556.item_id: str
$.products.4760268021.variants.8193934556.options: dict
$.products.4760268021.variants.8193934556.options.screen size: str
$.products.4760268021.variants.8193934556.options.processor: str
$.products.4760268021.variants.8193934556.options.ram: str
$.products.4760268021.variants.8193934556.options.storage: str
$.products.4760268021.variants.8193934556.options.color: str
$.products.4760268021.variants.8193934556.available: bool
$.products.4760268021.variants.8193934556.price: float
$.products.4760268021.variants.2913673670: dict
$.products.4760268021.variants.2913673670.item_id: str
$.products.4760268021.variants.2913673670.options: dict
$.products.4760268021.variants.2913673670.options.screen size: str
$.products.4760268021.variants.2913673670.options.processor: str
$.products.4760268021.variants.2913673670.options.ram: str
$.products.4760268021.variants.2913673670.options.storage: str
$.products.4760268021.variants.2913673670.options.color: str
$.products.4760268021.variants.2913673670.available: bool
$.products.4760268021.variants.2913673670.price: float
$.products.4760268021.variants.3478699712: dict
$.products.4760268021.variants.3478699712.item_id: str
$.products.4760268021.variants.3478699712.options: dict
$.products.4760268021.variants.3478699712.options.screen size: str
$.products.4760268021.variants.3478699712.options.processor: str
$.products.4760268021.variants.3478699712.options.ram: str
$.products.4760268021.variants.3478699712.options.storage: str
$.products.4760268021.variants.3478699712.options.color: str
$.products.4760268021.variants.3478699712.available: bool
$.products.4760268021.variants.3478699712.price: float
$.products.4760268021.variants.6056040996: dict
$.products.4760268021.variants.6056040996.item_id: str
$.products.4760268021.variants.6056040996.options: dict
$.products.4760268021.variants.6056040996.options.screen size: str
$.products.4760268021.variants.6056040996.options.processor: str
$.products.4760268021.variants.6056040996.options.ram: str
$.products.4760268021.variants.6056040996.options.storage: str
$.products.4760268021.variants.6056040996.options.color: str
$.products.4760268021.variants.6056040996.available: bool
$.products.4760268021.variants.6056040996.price: float
$.products.4760268021.variants.6017636844: dict
$.products.4760268021.variants.6017636844.item_id: str
$.products.4760268021.variants.6017636844.options: dict
$.products.4760268021.variants.6017636844.options.screen size: str
$.products.4760268021.variants.6017636844.options.processor: str
$.products.4760268021.variants.6017636844.options.ram: str
$.products.4760268021.variants.6017636844.options.storage: str
$.products.4760268021.variants.6017636844.options.color: str
$.products.4760268021.variants.6017636844.available: bool
$.products.4760268021.variants.6017636844.price: float
$.products.4760268021.variants.1657832319: dict
$.products.4760268021.variants.1657832319.item_id: str
$.products.4760268021.variants.1657832319.options: dict
$.products.4760268021.variants.1657832319.options.screen size: str
$.products.4760268021.variants.1657832319.options.processor: str
$.products.4760268021.variants.1657832319.options.ram: str
$.products.4760268021.variants.1657832319.options.storage: str
$.products.4760268021.variants.1657832319.options.color: str
$.products.4760268021.variants.1657832319.available: bool
$.products.4760268021.variants.1657832319.price: float
$.products.4760268021.variants.5052031638: dict
$.products.4760268021.variants.5052031638.item_id: str
$.products.4760268021.variants.5052031638.options: dict
$.products.4760268021.variants.5052031638.options.screen size: str
$.products.4760268021.variants.5052031638.options.processor: str
$.products.4760268021.variants.5052031638.options.ram: str
$.products.4760268021.variants.5052031638.options.storage: str
$.products.4760268021.variants.5052031638.options.color: str
$.products.4760268021.variants.5052031638.available: bool
$.products.4760268021.variants.5052031638.price: float
$.products.4760268021.variants.3265035808: dict
$.products.4760268021.variants.3265035808.item_id: str
$.products.4760268021.variants.3265035808.options: dict
$.products.4760268021.variants.3265035808.options.screen size: str
$.products.4760268021.variants.3265035808.options.processor: str
$.products.4760268021.variants.3265035808.options.ram: str
$.products.4760268021.variants.3265035808.options.storage: str
$.products.4760268021.variants.3265035808.options.color: str
$.products.4760268021.variants.3265035808.available: bool
$.products.4760268021.variants.3265035808.price: float
$.products.4760268021.variants.3334537816: dict
$.products.4760268021.variants.3334537816.item_id: str
$.products.4760268021.variants.3334537816.options: dict
$.products.4760268021.variants.3334537816.options.screen size: str
$.products.4760268021.variants.3334537816.options.processor: str
$.products.4760268021.variants.3334537816.options.ram: str
$.products.4760268021.variants.3334537816.options.storage: str
$.products.4760268021.variants.3334537816.options.color: str
$.products.4760268021.variants.3334537816.available: bool
$.products.4760268021.variants.3334537816.price: float
$.products.4760268021.variants.9844888101: dict
$.products.4760268021.variants.9844888101.item_id: str
$.products.4760268021.variants.9844888101.options: dict
$.products.4760268021.variants.9844888101.options.screen size: str
$.products.4760268021.variants.9844888101.options.processor: str
$.products.4760268021.variants.9844888101.options.ram: str
$.products.4760268021.variants.9844888101.options.storage: str
$.products.4760268021.variants.9844888101.options.color: str
$.products.4760268021.variants.9844888101.available: bool
$.products.4760268021.variants.9844888101.price: float
$.products.4760268021.variants.4241599783: dict
$.products.4760268021.variants.4241599783.item_id: str
$.products.4760268021.variants.4241599783.options: dict
$.products.4760268021.variants.4241599783.options.screen size: str
$.products.4760268021.variants.4241599783.options.processor: str
$.products.4760268021.variants.4241599783.options.ram: str
$.products.4760268021.variants.4241599783.options.storage: str
$.products.4760268021.variants.4241599783.options.color: str
$.products.4760268021.variants.4241599783.available: bool
$.products.4760268021.variants.4241599783.price: float
$.products.4760268021.variants.2611676054: dict
$.products.4760268021.variants.2611676054.item_id: str
$.products.4760268021.variants.2611676054.options: dict
$.products.4760268021.variants.2611676054.options.screen size: str
$.products.4760268021.variants.2611676054.options.processor: str
$.products.4760268021.variants.2611676054.options.ram: str
$.products.4760268021.variants.2611676054.options.storage: str
$.products.4760268021.variants.2611676054.options.color: str
$.products.4760268021.variants.2611676054.available: bool
$.products.4760268021.variants.2611676054.price: float
$.products.6938111410: dict
$.products.6938111410.name: str
$.products.6938111410.product_id: str
$.products.6938111410.variants: dict
$.products.6938111410.variants.4153505238: dict
$.products.6938111410.variants.4153505238.item_id: str
$.products.6938111410.variants.4153505238.options: dict
$.products.6938111410.variants.4153505238.options.size: str
$.products.6938111410.variants.4153505238.options.color: str
$.products.6938111410.variants.4153505238.options.material: str
$.products.6938111410.variants.4153505238.options.sole: str
$.products.6938111410.variants.4153505238.available: bool
$.products.6938111410.variants.4153505238.price: float
$.products.6938111410.variants.1775591963: dict
$.products.6938111410.variants.1775591963.item_id: str
$.products.6938111410.variants.1775591963.options: dict
$.products.6938111410.variants.1775591963.options.size: str
$.products.6938111410.variants.1775591963.options.color: str
$.products.6938111410.variants.1775591963.options.material: str
$.products.6938111410.variants.1775591963.options.sole: str
$.products.6938111410.variants.1775591963.available: bool
$.products.6938111410.variants.1775591963.price: float
$.products.6938111410.variants.9635758562: dict
$.products.6938111410.variants.9635758562.item_id: str
$.products.6938111410.variants.9635758562.options: dict
$.products.6938111410.variants.9635758562.options.size: str
$.products.6938111410.variants.9635758562.options.color: str
$.products.6938111410.variants.9635758562.options.material: str
$.products.6938111410.variants.9635758562.options.sole: str
$.products.6938111410.variants.9635758562.available: bool
$.products.6938111410.variants.9635758562.price: float
$.products.6938111410.variants.9791469541: dict
$.products.6938111410.variants.9791469541.item_id: str
$.products.6938111410.variants.9791469541.options: dict
$.products.6938111410.variants.9791469541.options.size: str
$.products.6938111410.variants.9791469541.options.color: str
$.products.6938111410.variants.9791469541.options.material: str
$.products.6938111410.variants.9791469541.options.sole: str
$.products.6938111410.variants.9791469541.available: bool
$.products.6938111410.variants.9791469541.price: float
$.products.6938111410.variants.4107812777: dict
$.products.6938111410.variants.4107812777.item_id: str
$.products.6938111410.variants.4107812777.options: dict
$.products.6938111410.variants.4107812777.options.size: str
$.products.6938111410.variants.4107812777.options.color: str
$.products.6938111410.variants.4107812777.options.material: str
$.products.6938111410.variants.4107812777.options.sole: str
$.products.6938111410.variants.4107812777.available: bool
$.products.6938111410.variants.4107812777.price: float
$.products.1801728040: dict
$.products.1801728040.name: str
$.products.1801728040.product_id: str
$.products.1801728040.variants: dict
$.products.1801728040.variants.1631373418: dict
$.products.1801728040.variants.1631373418.item_id: str
$.products.1801728040.variants.1631373418.options: dict
$.products.1801728040.variants.1631373418.options.color: str
$.products.1801728040.variants.1631373418.options.storage: str
$.products.1801728040.variants.1631373418.options.RAM: str
$.products.1801728040.variants.1631373418.options.screen size: str
$.products.1801728040.variants.1631373418.available: bool
$.products.1801728040.variants.1631373418.price: float
$.products.1801728040.variants.5490694069: dict
$.products.1801728040.variants.5490694069.item_id: str
$.products.1801728040.variants.5490694069.options: dict
$.products.1801728040.variants.5490694069.options.color: str
$.products.1801728040.variants.5490694069.options.storage: str
$.products.1801728040.variants.5490694069.options.RAM: str
$.products.1801728040.variants.5490694069.options.screen size: str
$.products.1801728040.variants.5490694069.available: bool
$.products.1801728040.variants.5490694069.price: float
$.products.1801728040.variants.3187628796: dict
$.products.1801728040.variants.3187628796.item_id: str
$.products.1801728040.variants.3187628796.options: dict
$.products.1801728040.variants.3187628796.options.color: str
$.products.1801728040.variants.3187628796.options.storage: str
$.products.1801728040.variants.3187628796.options.RAM: str
$.products.1801728040.variants.3187628796.options.screen size: str
$.products.1801728040.variants.3187628796.available: bool
$.products.1801728040.variants.3187628796.price: float
$.products.1801728040.variants.5339029584: dict
$.products.1801728040.variants.5339029584.item_id: str
$.products.1801728040.variants.5339029584.options: dict
$.products.1801728040.variants.5339029584.options.color: str
$.products.1801728040.variants.5339029584.options.storage: str
$.products.1801728040.variants.5339029584.options.RAM: str
$.products.1801728040.variants.5339029584.options.screen size: str
$.products.1801728040.variants.5339029584.available: bool
$.products.1801728040.variants.5339029584.price: float
$.products.1801728040.variants.3952176596: dict
$.products.1801728040.variants.3952176596.item_id: str
$.products.1801728040.variants.3952176596.options: dict
$.products.1801728040.variants.3952176596.options.color: str
$.products.1801728040.variants.3952176596.options.storage: str
$.products.1801728040.variants.3952176596.options.RAM: str
$.products.1801728040.variants.3952176596.options.screen size: str
$.products.1801728040.variants.3952176596.available: bool
$.products.1801728040.variants.3952176596.price: float
$.products.1801728040.variants.9929635042: dict
$.products.1801728040.variants.9929635042.item_id: str
$.products.1801728040.variants.9929635042.options: dict
$.products.1801728040.variants.9929635042.options.color: str
$.products.1801728040.variants.9929635042.options.storage: str
$.products.1801728040.variants.9929635042.options.RAM: str
$.products.1801728040.variants.9929635042.options.screen size: str
$.products.1801728040.variants.9929635042.available: bool
$.products.1801728040.variants.9929635042.price: float
$.products.1801728040.variants.1507389580: dict
$.products.1801728040.variants.1507389580.item_id: str
$.products.1801728040.variants.1507389580.options: dict
$.products.1801728040.variants.1507389580.options.color: str
$.products.1801728040.variants.1507389580.options.storage: str
... (+4704 lines)
```
- sample: `samples/downloaded_domains_data__retail__tau2_env__db.json` (124 KB)

## downloaded_domains_data/retail/tau2_env/policy.md

Размер: 6.5 КБ
Тип: текст, 6699 символов, 137 строк
- head: `samples/downloaded_domains_data__retail__tau2_env__policy.md.txt`

## downloaded_domains_data/retail/tau2_env/split_tasks.json

Размер: 3.2 КБ
Тип: JSON dict (len=3)
Схема:
```
$: dict
$.train: len~74 | list
$.train[]: str
$.test: len~40 | list
$.test[]: str
$.base: len~114 | list
$.base[]: str
```
- sample: `samples/downloaded_domains_data__retail__tau2_env__split_tasks.json` (1 KB)

## downloaded_domains_data/retail/tau2_env/tasks.json

Размер: 337.9 КБ
Тип: JSON list (len=114)
Схема:
```
$: len~114 | list
$[]: dict
$[].id: str
$[].description: dict
$[].description.purpose: NoneType
$[].description.relevant_policies: NoneType
$[].description.notes: NoneType
$[].user_scenario: dict
$[].user_scenario.persona: NoneType
$[].user_scenario.instructions: dict
$[].user_scenario.instructions.task_instructions: str
$[].user_scenario.instructions.domain: str
$[].user_scenario.instructions.reason_for_call: str
$[].user_scenario.instructions.known_info: str
$[].user_scenario.instructions.unknown_info: NoneType | str
$[].initial_state: NoneType
$[].evaluation_criteria: dict
$[].evaluation_criteria.actions: len~0 | len~1 | len~10 | len~11 | len~12 | len~13 | len~4 | len~5 | len~6 | len~7 | len~8 | len~9 | list
$[].evaluation_criteria.actions[]: dict
$[].evaluation_criteria.actions[].action_id: str
$[].evaluation_criteria.actions[].name: str
$[].evaluation_criteria.actions[].arguments: dict
$[].evaluation_criteria.actions[].arguments.first_name: str
$[].evaluation_criteria.actions[].arguments.last_name: str
$[].evaluation_criteria.actions[].arguments.zip: str
$[].evaluation_criteria.actions[].info: NoneType
$[].evaluation_criteria.actions[].arguments.order_id: str
$[].evaluation_criteria.actions[].arguments.product_id: str
$[].evaluation_criteria.actions[].arguments.item_ids: len~1 | len~2 | len~3 | len~4 | list
$[].evaluation_criteria.actions[].arguments.item_ids[]: str
$[].evaluation_criteria.actions[].arguments.new_item_ids: len~1 | len~2 | len~3 | len~4 | list
$[].evaluation_criteria.actions[].arguments.new_item_ids[]: str
$[].evaluation_criteria.actions[].arguments.payment_method_id: str
$[].evaluation_criteria.communicate_info: len~0 | len~1 | len~2 | len~3 | list
$[].evaluation_criteria.nl_assertions: NoneType | len~0 | len~1 | len~2 | list
$[].evaluation_criteria.reward_basis: len~1 | len~2 | list
$[].evaluation_criteria.reward_basis[]: str
$[].evaluation_criteria.actions[].arguments.user_id: str
$[].evaluation_criteria.communicate_info[]: str
$[].evaluation_criteria.nl_assertions[]: str
$[].issues: len~1 | list
$[].issues[]: dict
$[].issues[].id: str
$[].issues[].title: str
$[].issues[].status: str
$[].issues[].created_at: str
$[].issues[].author_email: str
$[].issues[].simulation_file: str
$[].issues[].description: str
$[].evaluation_criteria.actions[].arguments.email: str
$[].evaluation_criteria.actions[].arguments.summary: str
$[].evaluation_criteria.actions[].compare_args: len~0 | list
$[].evaluation_criteria.actions[].arguments.expression: str
$[].evaluation_criteria.actions[].arguments.reason: str
$[].evaluation_criteria.actions[].arguments.address1: str
$[].evaluation_criteria.actions[].arguments.address2: str
$[].evaluation_criteria.actions[].arguments.city: str
$[].evaluation_criteria.actions[].arguments.state: str
$[].evaluation_criteria.actions[].arguments.country: str
$[].evaluation_criteria.actions[].arguments.item_id: str
```
- sample: `samples/downloaded_domains_data__retail__tau2_env__tasks.json` (4 KB)

## downloaded_domains_data/retail/tau2_env/tools.py

Размер: 28.5 КБ
Тип: текст, 29202 символов, 753 строк
Определения (25): RetailTools, __init__, _get_order, _get_user, _get_product, _get_item, _get_variant, _get_payment_method, _is_pending_order, calculate, cancel_pending_order, exchange_delivered_order_items, find_user_id_by_name_zip, find_user_id_by_email, get_order_details, get_product_details, get_item_details, get_user_details, list_all_product_types, modify_pending_order_address, modify_pending_order_items, modify_pending_order_payment, modify_user_address, return_delivered_order_items, transfer_to_human_agents
- head: `samples/downloaded_domains_data__retail__tau2_env__tools.py.txt`

## downloaded_domains_data/telecom/secondary_source/README.md

Размер: 5.4 КБ
Тип: текст, 5344 символов, 160 строк
- head: `samples/downloaded_domains_data__telecom__secondary_source__README.md.txt`

## downloaded_domains_data/telecom/secondary_source/dataset_stats.json

Размер: 0.4 КБ
Тип: JSON dict (len=6)
Схема:
```
$: dict
$.total_samples: int
$.rfcs_processed: int
$.agent_types: int
$.model_used: str
$.domains: len~14 | list
$.domains[]: str
$.generated_at: str
```
- sample: `samples/downloaded_domains_data__telecom__secondary_source__dataset_stats.json` (0 KB)

## downloaded_domains_data/telecom/secondary_source/telecom_agentic_dataset.jsonl

Размер: 12543.7 КБ
Тип: JSONL; прочитано строк: 2000 (битых: 0, лимит 20000)
Схема (объединение по первым записям):
```
$: dict
$.id: str
$.conversations: len~3 | len~5 | list
$.conversations[]: dict
$.conversations[].role: str
$.conversations[].content: str
$.metadata: dict
$.metadata.domain: str
$.metadata.topic: str
$.metadata.scenario: str
$.metadata.complexity: str
$.metadata.turns: int
$.metadata.generated_at: str
$.metadata.generator: str
```
- sample: `samples/downloaded_domains_data__telecom__secondary_source__telecom_agentic_dataset.jsonl__line0.json` (3 KB)
- sample: `samples/downloaded_domains_data__telecom__secondary_source__telecom_agentic_dataset.jsonl__FULL_line0.json` (3 KB)

## downloaded_domains_data/telecom/tau2_env/db.toml

Размер: 9.4 КБ
Тип: текст, 9628 символов, 451 строк
- head: `samples/downloaded_domains_data__telecom__tau2_env__db.toml.txt`

## downloaded_domains_data/telecom/tau2_env/main_policy.md

Размер: 5.6 КБ
Тип: текст, 5699 символов, 159 строк
- head: `samples/downloaded_domains_data__telecom__tau2_env__main_policy.md.txt`

## downloaded_domains_data/telecom/tau2_env/main_policy_solo.md

Размер: 5.1 КБ
Тип: текст, 5200 символов, 155 строк
- head: `samples/downloaded_domains_data__telecom__tau2_env__main_policy_solo.md.txt`

## downloaded_domains_data/telecom/tau2_env/split_tasks.json

Размер: 347.8 КБ
Тип: JSON dict (len=5)
Схема:
```
$: dict
$.small: len~20 | list
$.small[]: str
$.train: len~74 | list
$.train[]: str
$.test: len~40 | list
$.test[]: str
$.full: len~2285 | list
$.full[]: str
$.base: len~114 | list
$.base[]: str
```
- sample: `samples/downloaded_domains_data__telecom__tau2_env__split_tasks.json` (20 KB)

## downloaded_domains_data/telecom/tau2_env/tasks.json

Размер: 13649.5 КБ
Тип: JSON list (len=2285)
Схема:
```
$: len~2285 | list
$[]: dict
$[].id: str
$[].description: dict
$[].description.purpose: str
$[].description.relevant_policies: NoneType
$[].description.notes: NoneType
$[].user_scenario: dict
$[].user_scenario.persona: NoneType | str
$[].user_scenario.instructions: dict
$[].user_scenario.instructions.domain: str
$[].user_scenario.instructions.reason_for_call: str
$[].user_scenario.instructions.known_info: str
$[].user_scenario.instructions.unknown_info: NoneType
$[].user_scenario.instructions.task_instructions: str
$[].ticket: str
$[].initial_state: dict
$[].initial_state.initialization_data: NoneType
$[].initial_state.initialization_actions: len~2 | len~3 | len~4 | len~5 | len~6 | list
$[].initial_state.initialization_actions[]: dict
$[].initial_state.initialization_actions[].env_type: str
$[].initial_state.initialization_actions[].func_name: str
$[].initial_state.initialization_actions[].arguments: dict
$[].initial_state.initialization_actions[].arguments.name: str
$[].initial_state.initialization_actions[].arguments.phone_number: str
$[].initial_state.initialization_actions[].arguments.abroad: bool
$[].initial_state.initialization_actions[].arguments.customer_id: str
$[].initial_state.initialization_actions[].arguments.line_id: str
$[].initial_state.message_history: NoneType
$[].evaluation_criteria: dict
$[].evaluation_criteria.actions: len~1 | len~2 | len~3 | list
$[].evaluation_criteria.actions[]: dict
$[].evaluation_criteria.actions[].action_id: str
$[].evaluation_criteria.actions[].requestor: str
$[].evaluation_criteria.actions[].name: str
$[].evaluation_criteria.actions[].arguments: dict
$[].evaluation_criteria.actions[].info: NoneType
$[].evaluation_criteria.actions[].compare_args: NoneType
$[].evaluation_criteria.env_assertions: len~2 | len~3 | list
$[].evaluation_criteria.env_assertions[]: dict
$[].evaluation_criteria.env_assertions[].env_type: str
$[].evaluation_criteria.env_assertions[].func_name: str
$[].evaluation_criteria.env_assertions[].arguments: dict
$[].evaluation_criteria.env_assertions[].arguments.expected_status: bool
$[].evaluation_criteria.env_assertions[].assert_value: bool
$[].evaluation_criteria.env_assertions[].message: NoneType
$[].evaluation_criteria.env_assertions[].arguments.expected_speed: int
$[].evaluation_criteria.env_assertions[].arguments.expected_desc: str
$[].evaluation_criteria.communicate_info: NoneType
$[].evaluation_criteria.nl_assertions: NoneType
$[].evaluation_criteria.reward_basis: len~1 | list
$[].evaluation_criteria.reward_basis[]: str
$[].evaluation_criteria.actions[].arguments.customer_id: str
$[].evaluation_criteria.actions[].arguments.line_id: str
$[].initial_state.initialization_actions[].arguments.mode: str
$[].evaluation_criteria.actions[].arguments.mode: str
$[].initial_state.initialization_actions[].arguments.data_used_gb: float
$[].evaluation_criteria.actions[].arguments.gb_amount: float
$[].evaluation_criteria.env_assertions[].arguments.customer_id: str
$[].evaluation_criteria.env_assertions[].arguments.line_id: str
$[].evaluation_criteria.env_assertions[].arguments.expected_amount: float
```
- sample: `samples/downloaded_domains_data__telecom__tau2_env__tasks.json` (9 KB)

## downloaded_domains_data/telecom/tau2_env/tasks_full.json

Размер: 13649.5 КБ
Тип: JSON list (len=2285)
Схема:
```
$: len~2285 | list
$[]: dict
$[].id: str
$[].description: dict
$[].description.purpose: str
$[].description.relevant_policies: NoneType
$[].description.notes: NoneType
$[].user_scenario: dict
$[].user_scenario.persona: NoneType | str
$[].user_scenario.instructions: dict
$[].user_scenario.instructions.domain: str
$[].user_scenario.instructions.reason_for_call: str
$[].user_scenario.instructions.known_info: str
$[].user_scenario.instructions.unknown_info: NoneType
$[].user_scenario.instructions.task_instructions: str
$[].ticket: str
$[].initial_state: dict
$[].initial_state.initialization_data: NoneType
$[].initial_state.initialization_actions: len~2 | len~3 | len~4 | len~5 | len~6 | list
$[].initial_state.initialization_actions[]: dict
$[].initial_state.initialization_actions[].env_type: str
$[].initial_state.initialization_actions[].func_name: str
$[].initial_state.initialization_actions[].arguments: dict
$[].initial_state.initialization_actions[].arguments.name: str
$[].initial_state.initialization_actions[].arguments.phone_number: str
$[].initial_state.initialization_actions[].arguments.abroad: bool
$[].initial_state.initialization_actions[].arguments.customer_id: str
$[].initial_state.initialization_actions[].arguments.line_id: str
$[].initial_state.message_history: NoneType
$[].evaluation_criteria: dict
$[].evaluation_criteria.actions: len~1 | len~2 | len~3 | list
$[].evaluation_criteria.actions[]: dict
$[].evaluation_criteria.actions[].action_id: str
$[].evaluation_criteria.actions[].requestor: str
$[].evaluation_criteria.actions[].name: str
$[].evaluation_criteria.actions[].arguments: dict
$[].evaluation_criteria.actions[].info: NoneType
$[].evaluation_criteria.actions[].compare_args: NoneType
$[].evaluation_criteria.env_assertions: len~2 | len~3 | list
$[].evaluation_criteria.env_assertions[]: dict
$[].evaluation_criteria.env_assertions[].env_type: str
$[].evaluation_criteria.env_assertions[].func_name: str
$[].evaluation_criteria.env_assertions[].arguments: dict
$[].evaluation_criteria.env_assertions[].arguments.expected_status: bool
$[].evaluation_criteria.env_assertions[].assert_value: bool
$[].evaluation_criteria.env_assertions[].message: NoneType
$[].evaluation_criteria.env_assertions[].arguments.expected_speed: int
$[].evaluation_criteria.env_assertions[].arguments.expected_desc: str
$[].evaluation_criteria.communicate_info: NoneType
$[].evaluation_criteria.nl_assertions: NoneType
$[].evaluation_criteria.reward_basis: len~1 | list
$[].evaluation_criteria.reward_basis[]: str
$[].evaluation_criteria.actions[].arguments.customer_id: str
$[].evaluation_criteria.actions[].arguments.line_id: str
$[].initial_state.initialization_actions[].arguments.mode: str
$[].evaluation_criteria.actions[].arguments.mode: str
$[].initial_state.initialization_actions[].arguments.data_used_gb: float
$[].evaluation_criteria.actions[].arguments.gb_amount: float
$[].evaluation_criteria.env_assertions[].arguments.customer_id: str
$[].evaluation_criteria.env_assertions[].arguments.line_id: str
$[].evaluation_criteria.env_assertions[].arguments.expected_amount: float
```
- sample: `samples/downloaded_domains_data__telecom__tau2_env__tasks_full.json` (9 KB)

## downloaded_domains_data/telecom/tau2_env/tasks_small.json

Размер: 81.9 КБ
Тип: JSON list (len=20)
Схема:
```
$: len~20 | list
$[]: dict
$[].id: str
$[].description: dict
$[].description.purpose: str
$[].description.relevant_policies: NoneType
$[].description.notes: NoneType
$[].user_scenario: dict
$[].user_scenario.persona: NoneType | str
$[].user_scenario.instructions: dict
$[].user_scenario.instructions.domain: str
$[].user_scenario.instructions.reason_for_call: str
$[].user_scenario.instructions.known_info: str
$[].user_scenario.instructions.unknown_info: NoneType
$[].user_scenario.instructions.task_instructions: str
$[].ticket: str
$[].initial_state: dict
$[].initial_state.initialization_data: NoneType
$[].initial_state.initialization_actions: len~2 | len~3 | len~4 | len~5 | list
$[].initial_state.initialization_actions[]: dict
$[].initial_state.initialization_actions[].env_type: str
$[].initial_state.initialization_actions[].func_name: str
$[].initial_state.initialization_actions[].arguments: dict
$[].initial_state.initialization_actions[].arguments.name: str
$[].initial_state.initialization_actions[].arguments.phone_number: str
$[].initial_state.initialization_actions[].arguments.abroad: bool
$[].initial_state.initialization_actions[].arguments.customer_id: str
$[].initial_state.initialization_actions[].arguments.line_id: str
$[].initial_state.message_history: NoneType
$[].evaluation_criteria: dict
$[].evaluation_criteria.actions: len~1 | len~2 | len~4 | list
$[].evaluation_criteria.actions[]: dict
$[].evaluation_criteria.actions[].action_id: str
$[].evaluation_criteria.actions[].requestor: str
$[].evaluation_criteria.actions[].name: str
$[].evaluation_criteria.actions[].arguments: dict
$[].evaluation_criteria.actions[].info: NoneType
$[].evaluation_criteria.actions[].compare_args: NoneType | len~0 | list
$[].evaluation_criteria.env_assertions: len~1 | len~2 | len~3 | list
$[].evaluation_criteria.env_assertions[]: dict
$[].evaluation_criteria.env_assertions[].env_type: str
$[].evaluation_criteria.env_assertions[].func_name: str
$[].evaluation_criteria.env_assertions[].arguments: dict
$[].evaluation_criteria.env_assertions[].arguments.expected_status: bool | str
$[].evaluation_criteria.env_assertions[].assert_value: bool
$[].evaluation_criteria.env_assertions[].message: NoneType | str
$[].evaluation_criteria.env_assertions[].arguments.expected_speed: int
$[].evaluation_criteria.env_assertions[].arguments.expected_desc: str
$[].evaluation_criteria.communicate_info: NoneType
$[].evaluation_criteria.nl_assertions: NoneType
$[].evaluation_criteria.reward_basis: len~1 | len~2 | list
$[].evaluation_criteria.reward_basis[]: str
$[].evaluation_criteria.actions[].arguments.customer_id: str
$[].evaluation_criteria.actions[].arguments.line_id: str
$[].initial_state.initialization_actions[].arguments.mode: str
$[].evaluation_criteria.actions[].arguments.mode: str
$[].initial_state.initialization_actions[].arguments.data_used_gb: float
$[].evaluation_criteria.actions[].arguments.gb_amount: float
$[].evaluation_criteria.env_assertions[].arguments.customer_id: str
$[].evaluation_criteria.env_assertions[].arguments.line_id: str
$[].evaluation_criteria.env_assertions[].arguments.expected_amount: float
$[].evaluation_criteria.env_assertions[].arguments.overdue_bill_id: str
$[].evaluation_criteria.actions[].arguments.summary: str
$[].initial_state.initialization_actions[].arguments.new_bill_id: str
$[].initial_state.initialization_actions[].arguments.contract_ended: bool
$[].evaluation_criteria.actions[].arguments.bill_id: str
$[].initial_state.initialization_actions[].arguments.enabled: bool
$[].initial_state.initialization_actions[].arguments.mms_over_wifi: bool
$[].initial_state.initialization_actions[].arguments.app_name: str
$[].initial_state.initialization_actions[].arguments.permission: str
$[].evaluation_criteria.actions[].arguments.app_name: str
$[].evaluation_criteria.actions[].arguments.permission: str
```
- sample: `samples/downloaded_domains_data__telecom__tau2_env__tasks_small.json` (9 KB)

## downloaded_domains_data/telecom/tau2_env/tech_support_manual.md

Размер: 17.2 КБ
Тип: текст, 17544 символов, 206 строк
- head: `samples/downloaded_domains_data__telecom__tau2_env__tech_support_manual.md.txt`

## downloaded_domains_data/telecom/tau2_env/tech_support_workflow.md

Размер: 16.0 КБ
Тип: текст, 16390 символов, 303 строк
- head: `samples/downloaded_domains_data__telecom__tau2_env__tech_support_workflow.md.txt`

## downloaded_domains_data/telecom/tau2_env/tech_support_workflow_solo.md

Размер: 15.1 КБ
Тип: текст, 15470 символов, 299 строк
- head: `samples/downloaded_domains_data__telecom__tau2_env__tech_support_workflow_solo.md.txt`

## downloaded_domains_data/telecom/tau2_env/tools.py

Размер: 25.8 КБ
Тип: текст, 26442 символов, 778 строк
Определения (34): IDGenerator, __init__, get_id, TelecomTools, __init__, get_customer_by_phone, get_customer_by_id, get_customer_by_name, _get_line_by_phone, _get_line_by_id, _get_plan_by_id, _get_device_by_id, _get_bill_by_id, _get_target_line, get_available_plan_ids, get_details_by_id, suspend_line, resume_line, get_bills_for_customer, send_payment_request, _get_bills_awaiting_payment, _set_bill_to_paid, _apply_one_time_charge, get_data_usage, set_data_usage, enable_roaming, disable_roaming, transfer_to_human_agents, refuel_data, suspend_line_for_overdue_bill, assert_data_refueling_amount, assert_line_status, assert_overdue_bill_exists, assert_no_overdue_bill
- head: `samples/downloaded_domains_data__telecom__tau2_env__tools.py.txt`

## downloaded_domains_data/telecom/tau2_env/user_db.toml

Размер: 0.9 КБ
Тип: текст, 933 символов, 43 строк
- head: `samples/downloaded_domains_data__telecom__tau2_env__user_db.toml.txt`

## downloaded_domains_data/telecom/tau2_env/workflows/dot_2_pdf.py

Размер: 1.1 КБ
Тип: текст, 1105 символов, 45 строк
Определения (2): convert_dot_to_pdf, main
- head: `samples/downloaded_domains_data__telecom__tau2_env__workflows__dot_2_pdf.py.txt`

## downloaded_domains_data/telecom/tau2_env/workflows/tech_support_path1_no_service.dot

Размер: 5.7 КБ
Тип: текст, 5821 символов, 102 строк
- head: `samples/downloaded_domains_data__telecom__tau2_env__workflows__tech_support_path1_no_service.dot.txt`

## downloaded_domains_data/telecom/tau2_env/workflows/tech_support_path2_mobile_data.dot

Размер: 12.0 КБ
Тип: текст, 12309 символов, 179 строк
- head: `samples/downloaded_domains_data__telecom__tau2_env__workflows__tech_support_path2_mobile_data.dot.txt`

## downloaded_domains_data/telecom/tau2_env/workflows/tech_support_path3_mms.dot

Размер: 5.8 КБ
Тип: текст, 5953 символов, 97 строк
- head: `samples/downloaded_domains_data__telecom__tau2_env__workflows__tech_support_path3_mms.dot.txt`

## Папки с большим числом файлов

- downloaded_domains_data/banking_knowledge/tau2_env/documents: 698 файлов, показаны 2
- downloaded_domains_data/banking_knowledge/tau2_env/prompts: 14 файлов, показаны 2
- downloaded_domains_data/banking_knowledge/tau2_env/tasks: 97 файлов, показаны 2
- downloaded_domains_data/downloaded_domains_data/airline/secondary_source: 2 файлов, показаны 2
- downloaded_domains_data/retail/secondary_source: 7 файлов, показаны 2
- downloaded_domains_data/retail/secondary_source/env/calls: 16 файлов, показаны 2
- downloaded_domains_data/retail/secondary_source/env/tasks: 245 файлов, показаны 2
- downloaded_domains_data/retail/secondary_source/env/tools: 16 файлов, показаны 2
- downloaded_domains_data/retail/secondary_source/overlays: 458 файлов, показаны 2
- downloaded_domains_data/retail/secondary_source/tasks: 450 файлов, показаны 2
- downloaded_domains_data/retail/secondary_source/verifiers: 444 файлов, показаны 2

## Пропущено

3395 файлов (бинарные/нерелевантные/другие бенчмарки); первые 40: downloaded_domains_data/.DS_Store, downloaded_domains_data/banking_knowledge/.DS_Store, downloaded_domains_data/banking_knowledge/secondary_source/.cache/huggingface/.gitignore, downloaded_domains_data/banking_knowledge/secondary_source/.cache/huggingface/CACHEDIR.TAG, downloaded_domains_data/banking_knowledge/secondary_source/.cache/huggingface/download/README.md.lock, downloaded_domains_data/banking_knowledge/secondary_source/.cache/huggingface/download/README.md.metadata, downloaded_domains_data/banking_knowledge/secondary_source/.cache/huggingface/download/db.json.lock, downloaded_domains_data/banking_knowledge/secondary_source/.cache/huggingface/download/db.json.metadata, downloaded_domains_data/banking_knowledge/secondary_source/.cache/huggingface/download/kb.json.lock, downloaded_domains_data/banking_knowledge/secondary_source/.cache/huggingface/download/kb.json.metadata, downloaded_domains_data/banking_knowledge/secondary_source/.cache/huggingface/download/train.jsonl.lock, downloaded_domains_data/banking_knowledge/secondary_source/.cache/huggingface/download/train.jsonl.metadata, downloaded_domains_data/banking_knowledge/secondary_source/.cache/huggingface/download/validation.jsonl.lock, downloaded_domains_data/banking_knowledge/secondary_source/.cache/huggingface/download/validation.jsonl.metadata, downloaded_domains_data/banking_knowledge/secondary_source/.cache/huggingface/trees/b58b627a3b366bc0fdc5064bc66cb59e92dee2c3.json, downloaded_domains_data/banking_knowledge/tau2_env/.DS_Store, downloaded_domains_data/downloaded_domains_data/.DS_Store, downloaded_domains_data/downloaded_domains_data/airline/.DS_Store, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/.gitignore, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/CACHEDIR.TAG, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/CLEANING_SUMMARY.md.lock, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/CLEANING_SUMMARY.md.metadata, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/README.md.lock, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/README.md.metadata, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/REAL_KEYS_ONLY_AUDIT.md.lock, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/REAL_KEYS_ONLY_AUDIT.md.metadata, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/global_tool_inventory.json.lock, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/global_tool_inventory.json.metadata, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/global_tool_inventory_with_benchmark.json.lock, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/global_tool_inventory_with_benchmark.json.metadata, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/mathhay.jsonl.lock, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/mathhay.jsonl.metadata, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/mathhay.parquet.lock, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/mathhay.parquet.metadata, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/mcpbench.jsonl.lock, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/mcpbench.jsonl.metadata, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/mcpbench.parquet.lock, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/mcpbench.parquet.metadata, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/removal_log.json.lock, downloaded_domains_data/downloaded_domains_data/airline/secondary_source/.cache/huggingface/download/removal_log.json.metadata