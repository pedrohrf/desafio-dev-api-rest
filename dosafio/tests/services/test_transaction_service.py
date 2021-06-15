import json
from unittest import TestCase, mock

from src.entities.transaction import Withdraw, Deposit
from src.services import transaction_services
from tests.helpers.neo4j_mock import Neo4jMock
from src.helpers.adapters.db_query import match, create
from src.entities.account import Account
from datetime import datetime
from src.helpers.enum.messages import ResponsesMessages


class TransactionServiceTest(TestCase):

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_get_transactions_sucess(self, neo4j, request):
        # ARRANGES
        request.query = {
            "account_id": '123'
        }
        transaction_dict = {
            'id': 0,
            'value': 50,
            'creation_date': datetime.now(),
        }

        neo = Neo4jMock(neo4j)
        neo.add(match.transactions, [
            Withdraw(**transaction_dict),
            Deposit(**transaction_dict)
        ])

        # ACT
        result = transaction_services.get_transactions()

        # ASSERTS
        self.assertEqual(200, result.status_code)

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_get_transactions_date_sucess(self, neo4j, request):
        # ARRANGES
        request.query = {
            "account_id": "123",
            "initial_date": "2020-01-01",
            "end_date": '2020-01-01',
        }
        transaction_dict = {
            'id': 0,
            'value': 50,
            'creation_date': datetime.now(),
        }

        neo = Neo4jMock(neo4j)
        neo.add(match.transactions, [
            Withdraw(**transaction_dict),
            Deposit(**transaction_dict)
        ])

        # ACT
        result = transaction_services.get_transactions()

        # ASSERTS
        self.assertEqual(200, result.status_code)

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_get_transactions_not_found(self, neo4j, request):
        # ARRANGES
        request.query = {
            "account_id": '123'
        }

        neo = Neo4jMock(neo4j)
        neo.add(match.transactions, [])

        # ACT
        result = transaction_services.get_transactions()

        # ASSERTS
        self.assertEqual(404, result.status_code)
        self.assertEqual(json.dumps(
            dict(result=dict(message=ResponsesMessages.TRANSACTIONS_NOT_FOUND.value))),
            result.body
        )

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_deposit_sucess(self, neo4j, request):
        # ARRANGES
        request.json = {
            "account_id": 123,
            "value": 100
        }
        account_dict = {
            'id': 0,
            'daily_withdraw_limit': 0,
            'balance': 0,
            'is_active': True,
            'creation_date': datetime.now(),
            'type': 0
        }

        neo = Neo4jMock(neo4j)
        neo.add(match.account, Account(**account_dict))
        neo.add(create.deposit, 1)

        # ACT
        result = transaction_services.deposit()

        # ASSERTS
        self.assertEqual(201, result.status_code)
        self.assertEqual(json.dumps(dict(result=1)), result.body)

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_deposit_account_not_active(self, neo4j, request):
        # ARRANGES
        request.json = {
            "account_id": 123,
            "value": 100
        }
        account_dict = {
            'id': 0,
            'daily_withdraw_limit': 0,
            'balance': 0,
            'is_active': False,
            'creation_date': datetime.now(),
            'type': 0
        }

        neo = Neo4jMock(neo4j)
        neo.add(match.account, Account(**account_dict))

        # ACT
        result = transaction_services.deposit()

        # ASSERTS
        self.assertEqual(400, result.status_code)
        self.assertEqual(json.dumps(
            dict(result=dict(message=ResponsesMessages.INVALID_OPERATION_BLOCKED_ACCOUNT.value))),
            result.body
        )

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_deposit_account_not_found(self, neo4j, request):
        # ARRANGES
        request.json = {
            "account_id": 123,
            "value": 100
        }

        neo = Neo4jMock(neo4j)
        neo.add(match.account, None)

        # ACT
        result = transaction_services.deposit()

        # ASSERTS
        self.assertEqual(404, result.status_code)
        self.assertEqual(json.dumps(
            dict(result=dict(message=ResponsesMessages.ACCOUNT_NOT_FOUND.value))),
            result.body
        )

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_withdraw_sucess(self, neo4j, request):
        # ARRANGES
        request.json = {
            "account_id": 123,
            "value": 100
        }
        account_dict = {
            'id': 0,
            'daily_withdraw_limit': 300,
            'balance': 300,
            'is_active': True,
            'creation_date': datetime.now(),
            'type': 0
        }

        neo = Neo4jMock(neo4j)
        neo.add(match.account, Account(**account_dict))
        neo.add(match.transactions, [])
        neo.add(create.withdraw, 1)

        # ACT
        result = transaction_services.withdraw()

        # ASSERTS
        self.assertEqual(201, result.status_code)
        self.assertEqual(json.dumps(dict(result=1)), result.body)

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_withdraw_limit(self, neo4j, request):
        # ARRANGES
        request.json = {
            "account_id": 123,
            "value": 100
        }
        account_dict = {
            'id': 0,
            'daily_withdraw_limit': 50,
            'balance': 300,
            'is_active': True,
            'creation_date': datetime.now(),
            'type': 0
        }

        neo = Neo4jMock(neo4j)
        neo.add(match.account, Account(**account_dict))
        neo.add(match.transactions, [])

        # ACT
        result = transaction_services.withdraw()

        # ASSERTS
        self.assertEqual(400, result.status_code)
        self.assertEqual(json.dumps(
            dict(result=dict(message=ResponsesMessages.INVALID_OPERATION_INSUFIENT_LIMIT.value))),
            result.body
        )

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_withdraw_balance(self, neo4j, request):
        # ARRANGES
        request.json = {
            "account_id": 123,
            "value": 100
        }
        account_dict = {
            'id': 0,
            'daily_withdraw_limit': 200,
            'balance': 50,
            'is_active': True,
            'creation_date': datetime.now(),
            'type': 0
        }

        neo = Neo4jMock(neo4j)
        neo.add(match.account, Account(**account_dict))
        neo.add(match.transactions, [])

        # ACT
        result = transaction_services.withdraw()

        # ASSERTS
        self.assertEqual(400, result.status_code)
        self.assertEqual(json.dumps(
            dict(result=dict(message=ResponsesMessages.INVALID_OPERATION_INSUFIENT_BALANCE.value))),
            result.body
        )

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_withdraw_account_not_found(self, neo4j, request):
        # ARRANGES
        request.json = {
            "account_id": 123,
            "value": 100
        }

        neo = Neo4jMock(neo4j)
        neo.add(match.account, None)

        # ACT
        result = transaction_services.withdraw()

        # ASSERTS
        self.assertEqual(404, result.status_code)
        self.assertEqual(json.dumps(
            dict(result=dict(message=ResponsesMessages.ACCOUNT_NOT_FOUND.value))),
            result.body
        )

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_withdraw_account_not_active(self, neo4j, request):
        # ARRANGES
        request.json = {
            "account_id": 123,
            "value": 100
        }
        account_dict = {
            'id': 0,
            'daily_withdraw_limit': 0,
            'balance': 0,
            'is_active': False,
            'creation_date': datetime.now(),
            'type': 0
        }

        neo = Neo4jMock(neo4j)
        neo.add(match.account, Account(**account_dict))

        # ACT
        result = transaction_services.withdraw()

        # ASSERTS
        self.assertEqual(400, result.status_code)
        self.assertEqual(json.dumps(
            dict(result=dict(message=ResponsesMessages.INVALID_OPERATION_BLOCKED_ACCOUNT.value))),
            result.body
        )
