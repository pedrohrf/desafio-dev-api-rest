import json
from unittest import TestCase, mock
from src.entities.person import Person
from src.services import person_services
from tests.helpers.neo4j_mock import Neo4jMock
from src.helpers.adapters.db_query import match, create
from datetime import date


class PersonServiceTest(TestCase):

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_create_person_generic_exception(self, neo4j, request):
        # ARRANGES
        request.json = {
            'name': 'sasdasd asdasd',
            'cpf': '93824591707',
            'born_date': str(date.today())
        }

        Neo4jMock(neo4j)

        # ACT
        result = person_services.create_person()

        # ASSERTS
        self.assertEqual(500, result.status_code)

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_create_person_sucess(self, neo4j, request):
        # ARRANGES
        request.json = {
            'name': 'sasdasd asdasd',
            'cpf': '93824591707',
            'born_date': str(date.today())
        }

        neo = Neo4jMock(neo4j)
        neo.add(create.person, 1)

        # ACT
        result = person_services.create_person()

        # ASSERTS
        self.assertEqual(201, result.status_code)
        self.assertEqual(json.dumps(dict(result=1)), result.body)

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_create_person_invalid_cpf(self, neo4j, request):
        # ARRANGES
        request.json = {
            'name': 'sasdasd asdasd',
            'cpf': '93824591708',
            'born_date': str(date.today())
        }

        neo = Neo4jMock(neo4j)
        neo.add(create.person, 1)

        # ACT
        result = person_services.create_person()

        # ASSERTS
        self.assertEqual(400, result.status_code)
        self.assertEqual(json.dumps(dict(result=dict(cpf=["CPF Inválido"]))), result.body)

    @mock.patch('src.app_factory.request')
    @mock.patch('src.helpers.neo4j_helper.GraphDatabase')
    def test_get_person_sucess(self, neo4j, request):
        # ARRANGES
        request.query = {
            'person_id': '1'
        }
        person_dict = {
            'id': 1,
            'name': 'str',
            'cpf': 'str',
            'born_date': date.today()
        }
        neo = Neo4jMock(neo4j)
        neo.add(match.person, Person(**person_dict))

        # ACT
        result = person_services.get_person()

        # ASSERTS
        person_dict['born_date'] = str(person_dict['born_date'])
        self.assertEqual(200, result.status_code)
        self.assertEqual(json.dumps(dict(result=person_dict)), result.body)
