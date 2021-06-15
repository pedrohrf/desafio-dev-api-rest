import json
from unittest import TestCase, mock
from src.entities.account import Account
from src.entities.person import Person
from src.helpers.enum.messages import ResponsesMessages
from src.services import account_services
from tests.helpers.neo4j_mock import Neo4jMock
from src.adapters.db_query import match, create, update
from datetime import date, datetime


class AccountServiceTest(TestCase):

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_create_account_sucess(self, neo4j, request):
        # ARRANGES
        request.json = {
            "person_id": 123,
            'daily_withdraw_limit': 0,
            'is_active': True,
            'type': 0
        }
        person_dict = {
            'id': 1,
            'name': 'str',
            'cpf': 'str',
            'born_date': date.today()
        }

        neo = Neo4jMock(neo4j)
        neo.add(match.person, Person(**person_dict))
        neo.add(create.account, 1)

        # ACT
        result = account_services.create_account()

        # ASSERTS
        self.assertEqual(201, result.status_code)
        self.assertEqual(json.dumps(dict(result=1)), result.body)

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_create_account_person_not_found(self, neo4j, request):
        # ARRANGES
        request.json = {
            "person_id": 123,
            'daily_withdraw_limit': 0,
            'is_active': True,
            'type': 0
        }

        neo = Neo4jMock(neo4j)
        neo.add(match.person, None)

        # ACT
        result = account_services.create_account()

        # ASSERTS
        self.assertEqual(404, result.status_code)
        self.assertEqual(json.dumps(
            dict(result=dict(message=ResponsesMessages.PERSON_NOT_FOUND.value))),
            result.body
        )

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_update_account_sucess(self, neo4j, request):
        # ARRANGES
        request.json = {
            'account_id': 1,
            'daily_withdraw_limit': 0,
            'is_active': True
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
        neo.add(update.account, Account(**account_dict))

        # ACT
        result = account_services.update_account()

        # ASSERTS
        account_dict['creation_date'] = str(account_dict['creation_date'])
        self.assertEqual(200, result.status_code)
        self.assertEqual(json.dumps(dict(result=account_dict)), result.body)

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_get_account_sucess(self, neo4j, request):
        # ARRANGES
        request.query = {
            'account_id': '1'
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

        # ACT
        result = account_services.get_account()

        # ASSERTS
        account_dict['creation_date'] = str(account_dict['creation_date'])
        self.assertEqual(200, result.status_code)
        self.assertEqual(json.dumps(dict(result=account_dict)), result.body)
