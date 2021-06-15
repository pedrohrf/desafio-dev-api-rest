from bottle import response
from src.app_factory import criar_app
from src.security.configurations import enable_cors
from src.services import account_services
from src.services import transaction_services
from src.services import person_services

app = criar_app()
app.merge(account_services.app)
app.merge(transaction_services.app)
app.merge(person_services.app)


@app.route('/<:re:.*>', method='OPTIONS')
def enable_cors_generic_route():
    enable_cors(response)


def main():
    app.run(debug=False, host='0.0.0.0', reloader=False)


if __name__ == '__main__':
    main()
