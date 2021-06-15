from src.business import cerberus_rules


def create_person():
    return {
        "name": cerberus_rules.string(),
        "cpf": cerberus_rules.cpf(),
        "born_date": cerberus_rules.date(),
    }


def get_person():
    return {
        "person_id": cerberus_rules.string_positive_integer()
    }
