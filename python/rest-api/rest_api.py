import json
from functools import wraps


class User:
    def __init__(self, name):
        self.name = name
        self.ledger = {}

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'owes': self.owes(),
            'owed_by': self.owed_by(),
            'balance': self.balance()}

    @staticmethod
    def from_dict(item: dict):
        user = User(item['name'])
        user.ledger = {k: v for k, v in item['owes'].items()}
        user.ledger.update({k: -v for k, v in item['owed_by'].items()})
        return user
