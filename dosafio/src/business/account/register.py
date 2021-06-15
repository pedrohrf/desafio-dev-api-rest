from src.components import database as db
from src.adapters.db_query.create import account as c_account
from src.adapters.db_query.update import account as u_account
from src.entities.account import Account
from src.business.account import search as search_account
from src.business.person import search as search_person


def from_create_account_service(**data) -> dict:
    new_account = Account.from_account_service(data)
    person = search_person.by_id(data['person_id'])
    return dict(body=db.create(c_account, acc=new_account, per=person), status=201)


def from_update_account_service(**data) -> Account:
    account = search_account.by_id(data['account_id'])
    account.is_active = data.get('is_active', account.is_active)
    account.daily_withdraw_limit = data.get('daily_withdraw_limit', account.daily_withdraw_limit)
    return db.update(u_account, acc=account)
