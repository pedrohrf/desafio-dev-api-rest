from src.app_factory import criar_app, endpoint
from src.business.account import register
from src.business.account import search
from src.services.payloads import account as payloads
from src.services.utils.responses import response

app = criar_app()


@app.post('/account')
def create_account():
    return response(
        endpoint(
            action=register.from_create_account_service,
            payload_schema=payloads.create_account
        )
    )


@app.put('/account')
def update_account():
    return response(
        endpoint(
            action=register.from_update_account_service,
            payload_schema=payloads.update_account
        )
    )


@app.get('/account')
def get_account():
    return response(
        endpoint(
            action=search.by_id,
            payload_schema=payloads.get_account,
            payload_type="query"
        )
    )
