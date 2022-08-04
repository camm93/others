import psycopg2 as db


class Postgresql:
    _DATABASE: str
    _USERNAME: str
    _PASSWORD: str
    _DB_PORT: str
    _HOST: str
    connection: str
    cursor: str

    def __init__(self):
        pass

    @classmethod
    def get_connection(cls):
        pass

    @classmethod
    def get_cursor(cls):
        pass

    @classmethod
    def close(cls):
        pass
