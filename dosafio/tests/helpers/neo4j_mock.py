from unittest.mock import MagicMock


class Neo4jMock:
    def __init__(self, magic_mock: MagicMock):
        self.side_effect = {}
        self.session = MagicMock()
        self.session.__enter__.return_value = self.session
        self.session.write_transaction.side_effect = self
        self.session.read_transaction.side_effect = self
        self.driver = MagicMock()
        self.driver.session.return_value = self.session
        magic_mock.driver.return_value = self.driver

    def __call__(self, func, **kwargs):
        return self.side_effect.get(func, []).pop()

    def add(self, func, result):
        if not self.side_effect.get(func):
            self.side_effect[func] = []
        self.side_effect[func].append(result)
