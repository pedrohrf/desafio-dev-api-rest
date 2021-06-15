from src.entities.account import Account
from src.entities.person import Person
from src.entities.transaction import Withdraw, Deposit


def account(tx, acc: Account, per: Person) -> dict:
    result = tx.run(
        "CREATE (a: Account{ "
        "daily_withdraw_limit: $daily_withdraw_limit, "
        "balance: $balance, "
        "is_active: $is_active, "
        "creation_date: $creation_date, "
        "type: $type "
        "}) "
        "WITH a "
        "MATCH (p: Person) WHERE id(p) = $person_id "
        "CREATE (p)-[r:HAS]->(a) "
        "RETURN id(a) as id",
        person_id=per.id,
        daily_withdraw_limit=acc.daily_withdraw_limit,
        balance=acc.balance,
        is_active=acc.is_active,
        creation_date=acc.creation_date,
        type=acc.type
    )
    result = result.single()
    return result['id']


def deposit(tx, dep: Deposit, acc: Account):
    result = tx.run(
        "MATCH  (a: Account) WHERE id(a) = $account_id "
        "SET a.balance = $balance "
        "WITH a "
        "CREATE (t: Transaction{ "
        "value: $value, "
        "creation_date: $creation_date "
        "})-[:DEPOSIT]->(a) "
        ""
        "RETURN id(t) AS id",
        account_id=acc.id,
        value=dep.value,
        creation_date=dep.creation_date,
        balance=acc.balance
    )
    result = result.single()
    return result['id']


def withdraw(tx, wd: Withdraw, acc: Account):
    result = tx.run(
        "MATCH  (a: Account) WHERE id(a) = $account_id "
        "SET a.balance = $balance "
        "WITH a "
        "CREATE (t: Transaction{ "
        "value: $value, "
        "creation_date: $creation_date "
        "})-[:WITHDRAW]->(a) "
        ""
        "RETURN id(t) AS id",
        account_id=acc.id,
        value=wd.value,
        creation_date=wd.creation_date,
        balance=acc.balance
    )
    result = result.single()
    return result['id']


def person(tx, per: Person) -> dict:
    result = tx.run(
        "CREATE (p: Person{ "
        "name: $name, "
        "cpf: $cpf, "
        "born_date: $born_date "
        "})"
        "RETURN id(p) as id",
        name=per.name,
        cpf=per.cpf,
        born_date=per.born_date
    )
    result = result.single()
    return result['id']
