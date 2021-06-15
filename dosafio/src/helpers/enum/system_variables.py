import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'local')
DB_CREDENTIALS = {
    "uri": os.environ.get("DB_URI", "bolt://localhost:7687/"),
    "auth": (os.environ.get("DB_USER", "neo4j"), os.environ.get("DB_PASSWORD", "neo4j"))
}
