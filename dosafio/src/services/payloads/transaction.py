from src.business import cerberus_rules


def deposit():
    return {
        "account_id": cerberus_rules.int(required=True),
        "value": cerberus_rules.floating_point(required=True)
    }


def withdraw():
    return {
        "account_id": cerberus_rules.int(required=True),
        "value": cerberus_rules.floating_point(required=True)
    }


def get_transations():
    return {
        "account_id": cerberus_rules.string_positive_integer(required=True),
        "type": cerberus_rules.transactions_type(),
        "initial_date": cerberus_rules.datetime(),
        "end_date": cerberus_rules.datetime(),
    }

