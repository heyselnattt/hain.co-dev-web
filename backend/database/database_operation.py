from dotenv import dotenv_values, load_dotenv
import psycopg2 as pg
import os

config = dotenv_values('.env')


class DatabaseOperator:
    def __init__(self, **params):
        load_dotenv()
        self.host = params.get('host', 'ec2-35-153-35-94.compute-1.amazonaws.com')
        self.database_name = params.get('database', 'd2a8coo0jp3akd')
        self.user = params.get('user', 'cxbubumlkovyuu')
        self.password = params.get('password', '7875893fe286b394a64661098d404972f17914786d304ef1fc66705d55840abc')
        self.port = params.get('port', '5432')
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

    def row_count(self, table_name: str = 'admin'):
        table = f'hainco_{table_name}'
        sql = f'SELECT COUNT(*) FROM {table}'

    # def get_next_id(self, table: str):
    #     sql = f'SELECT {table}_id FROM hainco_{table} ORDER BY id DESC LIMIT 1'
    #     print(sql)
    #     # cursor = self.get_cursor()
    #     # cursor.execute(sql)
    #     # max_id = cursor.fetchone()
    #     # return int(max_id) + 1
