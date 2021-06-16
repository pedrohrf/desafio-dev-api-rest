from cerberus import Validator
from src.exceptions import BadRequestException
from pycpfcnpj import cpfcnpj


class CustomValidator(Validator):
    def _check_with_cpf(self, field, value):
        if not cpfcnpj.validate(value):
            self._error(field, "CPF Inválido")


def validate_payload(schema: dict, data: dict, **kwargs) -> None:
    v = CustomValidator(schema, **kwargs)
    if not v.validate(data):
        raise BadRequestException(v.errors)
