from src.components import database as db
from src.entities.person import Person
from src.exceptions import NotFoundException
from src.helpers.enum import messages
from src.adapters.db_query.match import person


def by_id(person_id) -> Person:
    per = db.get(person, person_id=int(person_id))
    if not per:
        raise NotFoundException(dict(message=messages.ResponsesMessages.PERSON_NOT_FOUND.value))
    return per
