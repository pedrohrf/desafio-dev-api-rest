from typing import Any
from bottle import Bottle, request
from src.helpers.cerberus_validator import validate_payload


def criar_app() -> Bottle:
    app = Bottle()
    return app


def endpoint(action, payload_schema, payload_type="json") -> Any:
    try:
        body = dict(getattr(request, payload_type))
        validate_payload(payload_schema(), body)
        return action(**body)
    except Exception as e:
        return e
