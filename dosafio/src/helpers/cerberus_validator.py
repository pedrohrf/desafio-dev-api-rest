from cerberus import Validator
from src.exceptions import BadRequestException


class CustomValidator(Validator):
    def _check_with_cpf(self, field, value):
        pass


def validate_payload(schema: dict, data: dict, **kwargs) -> None:
    v = CustomValidator(schema, **kwargs)
    if not v.validate(data):
        raise BadRequestException(v.errors)
