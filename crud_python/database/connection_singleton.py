# Not used
import os
import sys
from dotenv import load_dotenv
import psycopg2 as db
from lessons_310.others.crud_python.config import log


load_dotenv()


class Postgresql:
    """Singleton design pattern to manage postgresql database connections and perform operations."""
    _DATABASE: str = os.getenv('DATABASE')
    _USERNAME: str = os.getenv('DB_USER')
    _PASSWORD: str = os.getenv('PASSWORD')
    _PORT: str = os.getenv('PORT')
    _HOST: str = os.getenv('HOST')
    _connection = None
    _cursor = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            try:
                cls._connection = db.connect(
                    database=cls._DATABASE, host=cls._HOST, password=cls._PASSWORD, port=cls._PORT, user=cls._USERNAME
                )
                log.debug(f"Connection successful: {cls._connection}")
                return cls._connection
            except Exception as e:
                log.error("An exception occurred when attempting to get a connection. "
                          f"{type(e)}: {e}")
                sys.exit()
        else:
            log.debug(f"Returning existing connection: {cls._connection}")
            return cls._connection

    @classmethod
    def get_cursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.get_connection().cursor()
                log.debug(f"Cursor open successfully: {cls._cursor}")
                return cls._cursor
            except Exception as e:
                log.error("An exception occurred when attempting to get a cursor. "
                          f"{type(e)}: {e}")
                sys.exit()
        else:
            log.debug(f"Returning existing cursor: {cls._connection}")
            return cls._cursor

    @classmethod
    def close(cls):
        try:
            cls._connection.close()
            log.info("Connection closed successfully")
        except Exception as e:
            log.error(f"An exception has occurred while attempting to close the db connection: {e}")


if __name__ == '__main__':
    Postgresql.get_connection()
    cursor = Postgresql.get_cursor()
    cursor.execute('SELECT * FROM persona ORDER BY id')
    rows = cursor.fetchall()
    print(rows)
    Postgresql.close()
