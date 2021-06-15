from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    id: int
    value: float
    creation_date: datetime

    @classmethod
    def from_db(cls, data):
        if not data:
            return None
        return cls(
            id=data.id,
            value=data.get('value'),
            creation_date=data.get("creation_date").to_native(),
        )


class Deposit(Transaction):
    @classmethod
    def from_service(cls, data: dict):
        return cls(
            value=data["value"],
            creation_date=datetime.now(),
            id=0
        )


class Withdraw(Transaction):
    @classmethod
    def from_service(cls, data: dict):
        return cls(
            value=-1*data["value"],
            creation_date=datetime.now(),
            id=0
        )


class Transactions:
    def __init__(self, transactions):
        self.ts = transactions
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.ts[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result
