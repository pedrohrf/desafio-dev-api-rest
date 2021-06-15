import json
from functools import singledispatch
from bottle import HTTPResponse, BaseResponse
from dataclasses import asdict

from src.entities.transaction import Transactions
from src.exceptions import BaseHttpResponseException
from src.helpers.enum.messages import ResponsesMessages
from src.security.configurations import config_response_headers
from src.entities.account import Account
from src.entities.person import Person


@singledispatch
def response(entity):
    raise NotImplementedError


def _response(status: int, body: str, headers: dict) -> BaseResponse:
    return config_response_headers(
        HTTPResponse(
            body=body,
            status=status,
            headers=headers
        )
    )


@response.register(Account)
def _dict_response(account: Account) -> BaseResponse:
    return _response(
        status=200,
        body=json.dumps(dict(result={
            "id": account.id,
            "daily_withdraw_limit": account.daily_withdraw_limit,
            "balance": account.balance,
            "is_active": account.is_active,
            "creation_date": str(account.creation_date),
            "type": account.type
        })),
        headers={
            'Content-Type': 'application/json'
        }
    )


@response.register(Person)
def _dict_response(person: Person) -> BaseResponse:
    return _response(
        status=200,
        body=json.dumps(dict(result={
            "id": person.id,
            "name": person.name,
            "cpf": person.cpf,
            "born_date": str(person.born_date)
        })),
        headers={
            'Content-Type': 'application/json'
        }
    )


@response.register(dict)
def _dict_response(_dict: dict) -> BaseResponse:
    return _response(
        status=_dict.get('status', 200),
        body=json.dumps(dict(result=_dict.get("body", {}))),
        headers=_dict.get('headers', {
            'Content-Type': 'application/json'
        })
    )


@response.register(Transactions)
def _list_response(transactions: Transactions) -> BaseResponse:
    return _response(
        status=200,
        body=json.dumps(dict(result=[{
            'id': ts.id,
            'value': ts.value,
            'creation_date': str(ts.creation_date)
        } for ts in transactions])),
        headers={
            'Content-Type': 'application/json'
        }
    )


@response.register(Exception)
def _exception_response(exception: Exception) -> BaseResponse:
    return _response(
        status=500,
        body=json.dumps(dict(result=ResponsesMessages.GENERIC_EXCEPTION.value)),
        headers={
            'Content-Type': 'application/json'
        }
    )


@response.register(BaseHttpResponseException)
def _exception_response(exception: BaseHttpResponseException) -> BaseResponse:
    return _response(
        status=exception.status,
        body=json.dumps(dict(result=exception.body)),
        headers={
            'Content-Type': 'application/json'
        }
    )
