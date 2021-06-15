from src.entities.person import Person
from src.components import database as db
from src.adapters.db_query.create import person


def from_create_person_service(**data):
    new_person = Person.from_person_service(data)
    return dict(body=db.create(person, per=new_person), status=201)
