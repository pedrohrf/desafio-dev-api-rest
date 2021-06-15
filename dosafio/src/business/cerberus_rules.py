from datetime import date as d, datetime as dt


def string(required=False, empty=False, nullable=True):
    return {
        'required': required,
        'nullable': nullable,
        'empty': empty,
        'type': 'string'
    }


def int(required=False, empty=False, nullable=True):
    return {
        'required': required,
        'nullable': nullable,
        'empty': empty,
        'type': 'integer'
    }


def floating_point(required=False, empty=False, nullable=True):
    return {
        'required': required,
        'nullable': nullable,
        'empty': empty,
        'type': 'float'
    }


def boolean(required=False, empty=False, nullable=True):
    return {
        'required': required,
        'nullable': nullable,
        'empty': empty,
        'type': 'boolean'
    }


def string_positive_integer(required=False, nullable=True):
    return {
        'required': required,
        'nullable': nullable,
        'regex': r'[0-9]*',
        'type': 'string'
    }


def cpf(required=False, empty=False, nullable=True):
    return {
        'required': required,
        'nullable': nullable,
        'empty': empty,
        'check_with': 'cpf',
        'type': 'string'
    }


def date(required=False, empty=False, nullable=True):
    return {
        'required': required,
        'nullable': nullable,
        'empty': empty,
        'coerce': lambda s: d.fromisoformat(s),
        'type': 'date'
    }


def datetime(required=False, empty=False, nullable=True):
    return {
        'required': required,
        'nullable': nullable,
        'empty': empty,
        'coerce': lambda s: dt.fromisoformat(s),
        'type': 'datetime'
    }


def transactions_type(required=False, empty=False, nullable=True):
    return {
        'required': required,
        'nullable': nullable,
        'empty': empty,
        'type': 'string',
        'allowed': ['WITHDRAW', 'DEPOSIT']
    }

