from src.entities.account import Account
from src.entities.person import Person
from src.entities.transaction import Withdraw, Deposit


def account(tx, **kw):
    result = tx.run("MATCH (a: Account) WHERE id(a) = $account_id RETURN a", **kw)
    result = result.single()
    return Account.from_db(result['a'] if result else None)


def person(tx, **kw):
    result = tx.run("MATCH (p: Person) WHERE id(p) = $person_id RETURN p", **kw)
    result = result.single()
    return Person.from_db(result['p'] if result else None)


def transactions(tx, **kwargs):
    parser = {
        "WITHDRAW": Withdraw,
        "DEPOSIT": Deposit
    }
    _type = kwargs.pop('type') if kwargs.get('type') else ''
    result = tx.run(f"MATCH (a: Account)-[r{(':' + _type) if _type else ''}]-(t:Transaction) "
                    f"WHERE id(a) = $account_id "
                    f"{'AND t.creation_date >= $initial_date ' if kwargs.get('initial_date') else ''}"
                    f"{'AND t.creation_date <= $end_date ' if kwargs.get('end_date') else ''}"
                    f"RETURN t as transaction, r as relationship", **kwargs)
    return [parser[r['relationship'].type].from_db(r['transaction']) for r in result]
