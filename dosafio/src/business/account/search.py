from src.components import database as db
from src.entities.account import Account
from src.exceptions import NotFoundException
from src.helpers.enum import messages
from src.adapters.db_query.match import account


def by_id(account_id) -> Account:
    acc = db.get(account, account_id=int(account_id))
    if not acc:
        raise NotFoundException(dict(message=messages.ResponsesMessages.ACCOUNT_NOT_FOUND.value))
    return acc
