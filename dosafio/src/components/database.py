from src.helpers.neo4j_helper import Neo4j
from src.helpers.enum import system_variables as sv


def create(func, **kwargs):
    db = Neo4j(**sv.DB_CREDENTIALS)
    return db.write(func, **kwargs)


def update(func, **kwargs):
    db = Neo4j(**sv.DB_CREDENTIALS)
    return db.write(func, **kwargs)


def get(func, **kwargs):
    db = Neo4j(**sv.DB_CREDENTIALS)
    return db.read(func, **kwargs)

