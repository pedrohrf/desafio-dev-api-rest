from src.entities.account import Account


def account(tx, acc: Account) -> dict:
    result = tx.run(
        "MATCH (a: Account) WHERE id(a) = $account_id "
        "SET a.is_active = $is_active, a.daily_withdraw_limit=$daily_withdraw_limit "
        "RETURN a",
        is_active=acc.is_active,
        daily_withdraw_limit=acc.daily_withdraw_limit,
        account_id=acc.id
    )
    result = result.single()
    return Account.from_db(result['a'])
