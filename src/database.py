from sqlite3 import connect
import psycopg2
from psycopg2 import sql
from src.get_carrency import get_carency


class Database():

    def connect(self):
        self.conn = psycopg2.connect(
            database="test", user='test', password='19952882h', host='127.0.0.1', port='5432'
        )
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    def disconnect(self):
        self.conn.close()

    def creat_table(self, headers):
        self.connect()
        # self.cursor.execute('DROP DATABASE IF EXISTS test')
        self.cursor.execute("""CREATE SCHEMA IF NOT EXISTS test
                                AUTHORIZATION test;""")
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS test.test()""")
        self.cursor.execute(
            """ALTER TABLE IF EXISTS test.test OWNER to test;""")
        headers.append("стоимость в руб.")
        for head in headers:
            self.cursor.execute(sql.SQL(
                "ALTER TABLE test ADD COLUMN IF NOT EXISTS {} text;").format(sql.Identifier(head)))
        self.disconnect()

    def insert_into_db(self, headers, dbinfo):
        self.connect()
        carency = get_carency()
        col_names = sql.SQL(', ').join(sql.Identifier(n) for n in headers)
        place_holders = sql.SQL(', ').join(sql.Placeholder() * len(headers))
        query_base = sql.SQL("insert into test ({col_names}) values ({values})").format(
            table_name=sql.Identifier("raw_orderbook"),
            col_names=col_names,
            values=place_holders
        )
        for info in dbinfo:
            rub = float(info[2]) * float(carency["Value"].replace(",", "."))
            info.append(round(rub, 2))
            self.cursor.execute(query_base, info)

        self.disconnect()

    def get_from_database(self):
        self.connect()
        self.cursor.execute("""select * from test""")
        tests = self.cursor.fetchall()
        self.disconnect()
        return tests

    def drop_table(self):
        self.connect()
        self.cursor.execute("""DROP TABLE test;""")
        self.disconnect()
