from neo4j import GraphDatabase


class Neo4j:
    def __init__(self, **kwargs):
        self.driver = GraphDatabase.driver(**kwargs)

    def write(self, func, **kwargs):
        with self.driver.session() as session:
            return session.write_transaction(func, **kwargs)

    def read(self, func, **kwargs):
        with self.driver.session() as session:
            return session.read_transaction(func, **kwargs)
