from dataclasses import dataclass
from datetime import date


@dataclass
class Person:
    id: int
    name: str
    cpf: str
    born_date: date

    @classmethod
    def from_db(cls, data):
        if not data:
            return None
        return cls(
            id=data.id,
            name=data.get('name'),
            cpf=data.get('cpf'),
            born_date=data.get('born_date').to_native(),
        )

    @classmethod
    def from_person_service(cls, data: dict):
        return cls(
            id=0,
            name=data.get('name'),
            cpf=data.get('cpf'),
            born_date=date.fromisoformat(data['born_date'])
        )
