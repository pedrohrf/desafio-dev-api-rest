from src.app_factory import criar_app, endpoint
from src.business.person import register
from src.business.person import search
from src.services.payloads import person
from src.services.utils.responses import response

app = criar_app()


@app.post('/person')
def create_person():
    return response(
        endpoint(
            action=register.from_create_person_service,
            payload_schema=person.create_person
        )
    )


@app.get('/person')
def get_person():
    return response(
        endpoint(
            action=search.by_id,
            payload_schema=person.get_person,
            payload_type="query"
        )
    )
