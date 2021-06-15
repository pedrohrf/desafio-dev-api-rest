import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'local')
DB_CREDENTIALS = {
    "uri": os.environ.get("DB_URI", ""),
    "auth": (os.environ.get("DB_USER"), os.environ.get("DB_PASSWORD"))
}
