from src.components import database as db
from src.entities.transaction import Deposit, Withdraw, Transactions
from src.entities.account import Account
from src.business.account import search
from src.exceptions import BadRequestException, NotFoundException
from src.helpers.enum import messages
from src.adapters.db_query.create import deposit as c_deposit, withdraw as c_withdraw
from src.adapters.db_query.match import transactions
from datetime import datetime


def _check_account_status(account: Account) -> None:
    if not account.is_active:
        raise BadRequestException(dict(message=messages.ResponsesMessages.INVALID_OPERATION_BLOCKED_ACCOUNT.value))


def _check_account_balance(account: Account) -> None:
    if account.balance < 0:
        raise BadRequestException(dict(message=messages.ResponsesMessages.INVALID_OPERATION_INSUFIENT_BALANCE.value))


def _check_account_daily_withdraw_limit(account: Account, wd: Withdraw) -> None:
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    total = sum([w.value for w in db.get(transactions, account_id=account.id, type="WITHDRAW", initial_date=today)])
    if account.daily_withdraw_limit < -1*(total + wd.value):
        raise BadRequestException(dict(message=messages.ResponsesMessages.INVALID_OPERATION_INSUFIENT_LIMIT.value))


def deposit(**data) -> dict:
    dp = Deposit.from_service(data)
    account = search.by_id(data['account_id'])
    _check_account_status(account)
    account.balance += dp.value
    return dict(body=db.create(c_deposit, dep=dp, acc=account), status=201)


def withdraw(**data) -> dict:
    wd = Withdraw.from_service(data)
    account = search.by_id(data['account_id'])
    _check_account_status(account)
    _check_account_daily_withdraw_limit(account, wd)
    account.balance += wd.value
    _check_account_balance(account)
    return dict(body=db.create(c_withdraw, wd=wd, acc=account), status=201)


def get_transations(**kwargs) -> Transactions:
    kwargs['account_id'] = int(kwargs['account_id'])
    if kwargs.get('initial_date'):
        kwargs['initial_date'] = datetime.fromisoformat(kwargs['initial_date'])
    if kwargs.get('end_date'):
        kwargs['end_date'] = datetime.fromisoformat(kwargs['end_date'])
    ts = db.get(transactions, **kwargs)
    if not ts:
        raise NotFoundException(dict(message=messages.ResponsesMessages.TRANSACTIONS_NOT_FOUND.value))
    return Transactions(ts)
