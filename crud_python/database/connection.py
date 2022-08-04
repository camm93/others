import os
import sys
from dotenv import load_dotenv
from psycopg2 import pool
from lessons_310.others.crud_python.config import log


load_dotenv()


class Postgresql:
    """Using a connection pool to manage postgresql database connections and perform operations."""
    _DATABASE: str = os.getenv('DATABASE')
    _USERNAME: str = os.getenv('DB_USER')
    _PASSWORD: str = os.getenv('PASSWORD')
    _PORT: str = os.getenv('PORT')
    _HOST: str = os.getenv('HOST')
    _MIN_CONN: int = 1
    _MAX_CONN: int = 5
    _pool = None

    @classmethod
    def get_pool(cls):
        """Singleton pattern to create a single connection pool."""
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CONN, cls._MAX_CONN, database=cls._DATABASE, host=cls._HOST, password=cls._PASSWORD,
                    port=cls._PORT, user=cls._USERNAME
                )
                log.info(f"Creation of Pool Successful: {cls._pool}")
                return cls._pool
            except Exception as e:
                log.error("An exception occurred when attempting to get the connection pool. "
                          f"{type(e)}: {e}")
                sys.exit()
        else:
            log.info(f"There is an existing pool. Returning: {cls._pool}")
            return cls._pool

    @classmethod
    def get_connection(cls):
        conn = cls.get_pool().getconn()
        log.debug(f"Successfully retrieved a connection from the pool: {conn}")
        return conn

    @classmethod
    def release_connection(cls, conn):
        cls.get_pool().putconn(conn)
        log.debug(f"Connection {conn} returned to pool.")

    @classmethod
    def close_connections(cls):
        cls.get_pool().closeall()
        log.debug(f"All connections and pool closed.")


if __name__ == '__main__':
    conn1 = Postgresql.get_connection()
    Postgresql.release_connection(conn1)
    conn2 = Postgresql.get_connection()
    conn3 = Postgresql.get_connection()
    conn4 = Postgresql.get_connection()
    conn5 = Postgresql.get_connection()
    conn6 = Postgresql.get_connection()  # raises PoolError
