import json
from functools import wraps


class User:
    def __init__(self, name):
        self.name = name
        self.ledger = {}

    def to_dict(self):
        return {'name': self.name,
                'owes': self.owes(),
                'owed_by': self.owed_by(),
                'balance': self.balance()}

    @staticmethod
    def from_dict(item: dict):
        user = User(item['name'])
        user.ledger = {k: v for k, v in item['owes'].items()}
        user.ledger.update({k: -v for k, v in item['owed_by'].items()})
        return user

    def balance(self):
        return sum(self.owed_by().values()) - sum(self.owes().values())

    def borrow(self, name: str, amount: int):
        self.ledger[name] = self.ledger.get(name, 0) + amount

    def lend(self, name: str, amount: int):
        self.ledger[name] = self.ledger.get(name, 0) - amount

    def owes(self):
        return {k: v for k, v in self.ledger.items() if v > 0}

    def owed_by(self):
        return {k: -v for k, v in self.ledger.items() if v < 0}


def route(func):
    @wraps(func)
    def wrapped(self, url: str, payload=None):
        if payload:
            payload = json.loads(payload)
        else:
            payload = {}
        return json.dumps(func(self, url, payload))
    return wrapped


class RestAPI(object):
    def __init__(self, database=None):
        self.database = {"users": []}
        if database is not None:
            self.database = {
                "users": {
                    user['name']: User.from_dict(user)
                    for user in database.get('users', [])
                }
            }

    @route
    def get(self, url: str, payload):
        if url == '/users':
            users = self.database.get('users', {})
            return {
                'users': sorted(
                    [
                        user.to_dict()
                        for user in users.values()
                        if payload.get('users') is None or
                        user.name in payload['users']
                    ],
                    key=lambda user: user['name'])
            }

    @route
    def post(self, url, payload):
        if url == '/add':
            self.database['users'][payload['user']] = User(payload['user'])
            return self.database['users'][payload['user']].to_dict()

        if url == '/iou':
            lender = self.database['users'][payload['lender']]
            borrower = self.database['users'][payload['borrower']]
            amount = payload['amount']

            lender.lend(borrower.name, amount)
            borrower.borrow(lender.name, amount)

            return {
                'users': sorted(
                    [lender.to_dict(), borrower.to_dict()],
                    key=lambda user: user['name']
                )
            }
