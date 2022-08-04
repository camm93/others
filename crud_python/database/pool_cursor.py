from lessons_310.others.crud_python.config import log
from .connection import Postgresql


class PoolCursor:
    """Resource manager for cursors."""

    def __init__(self):
        self._connection = None
        self._cursor = None

    def __enter__(self):
        log.debug("Executing with(__enter__)")
        self._connection = Postgresql.get_connection()
        self._cursor = self._connection.cursor()
        return self._cursor

    def __exit__(self, excepcion_type, exception_value, excepcion_traceback):
        log.debug("Executing with(__exit__)")
        if exception_value:
            self._connection.rollback()
            log.error(f"An exception has occurred: {exception_value} {excepcion_traceback}. Performing rollback.")
        else:
            self._connection.commit()
            log.info("Transaction committed.")
        self._cursor.close()
        Postgresql.release_connection(self._connection)


if __name__ == "__main__":
    with PoolCursor() as cursor:
        cursor.execute("SELECT * FROM persona")
        print(cursor.fetchall())
