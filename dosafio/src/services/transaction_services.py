from src.app_factory import criar_app, endpoint
from src.business.account import transaction
from src.business.account import search
from src.services.payloads import transaction as payloads
from src.services.utils.responses import response

app = criar_app()


@app.post('/transaction/deposit')
def deposit():
    return response(
        endpoint(
            action=transaction.deposit,
            payload_schema=payloads.deposit
        )
    )


@app.post('/transaction/withdraw')
def withdraw():
    return response(
        endpoint(
            action=transaction.withdraw,
            payload_schema=payloads.withdraw
        )
    )


@app.get('/transactions')
def get_transactions():
    return response(
        endpoint(
            action=transaction.get_transations,
            payload_schema=payloads.get_transations,
            payload_type="query"
        )
    )
