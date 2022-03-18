from dotenv import dotenv_values, load_dotenv
import psycopg2 as pg
import os

config = dotenv_values('.env')


class DatabaseOperator:
    def __init__(self, **params):
        load_dotenv()
        self.host = params.get('host', os.getenv('DATABASE_HOST'))
        self.database_name = params.get('database', os.getenv('DATABASE_NAME'))
        self.user = params.get('user', os.getenv('DATABASE_USER'))
        self.password = params.get('password', os.getenv('DATABASE_PASSWORD'))
        self.port = params.get('port', os.getenv('DATABASE_PORT'))
        self.cursor_factory = params.get('cursor_factory', None)
        self.conn = pg.connect(
            host=self.host,
            database=self.database_name,
            user=self.user,
            password=self.password,
            port=self.port,
            cursor_factory=self.cursor_factory,
        )

    def get_cursor(self):
        return self.conn.cursor()

    def close_cursor(self):
        self.conn.cursor().close()

    def close_connection(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    # def get_next_id(self, table: str):
    #     sql = f'SELECT {table}_id FROM hainco_{table} ORDER BY id DESC LIMIT 1'
    #     print(sql)
    #     # cursor = self.get_cursor()
    #     # cursor.execute(sql)
    #     # max_id = cursor.fetchone()
    #     # return int(max_id) + 1
