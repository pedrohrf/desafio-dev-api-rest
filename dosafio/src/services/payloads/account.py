from src.business import cerberus_rules


def create_account():
    return {
        "person_id": cerberus_rules.int(required=True),
        "daily_withdraw_limit": cerberus_rules.floating_point(required=True),
        "is_active": cerberus_rules.boolean(required=True),
        "type": cerberus_rules.int(required=True)
    }


def update_account():
    return {
        "account_id": cerberus_rules.int(required=True),
        "is_active": cerberus_rules.boolean(),
        "daily_withdraw_limit": cerberus_rules.floating_point()
    }


def get_account():
    return {
        "account_id": cerberus_rules.string_positive_integer(required=True)
    }
