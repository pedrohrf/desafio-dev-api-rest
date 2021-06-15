from dataclasses import dataclass
from datetime import datetime


@dataclass
class Account:
    id: int
    daily_withdraw_limit: float
    balance: float
    is_active: bool
    creation_date: datetime
    type: int

    @classmethod
    def from_db(cls, data):
        if not data:
            return None
        return cls(
            id=data.id,
            balance=data.get('balance'),
            creation_date=data.get('creation_date').to_native(),
            daily_withdraw_limit=data.get('daily_withdraw_limit'),
            is_active=data.get('is_active'),
            type=data.get('type'),
        )

    @classmethod
    def from_account_service(cls, data: dict):
        return cls(
            id=0,
            balance=0,
            creation_date=datetime.now(),
            daily_withdraw_limit=data.get('daily_withdraw_limit'),
            is_active=data.get('is_active'),
            type=data.get('type'),
        )
