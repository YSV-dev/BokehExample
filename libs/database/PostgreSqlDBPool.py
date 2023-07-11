import traceback
from typing import Any

import psycopg2
from psycopg2 import pool
from psycopg2.extras import execute_values

from libs.database.abstraction.DBPool import DBPool


class PostgreSqlDBPool(DBPool):
    def __init__(self, connection_params: dict = None):
        super().__init__(connection_params)

    def connect(self):
        try:
            self.pool = psycopg2.pool.SimpleConnectionPool(self.min_con,
                                                           self.max_con,
                                                           user=self.user,
                                                           password=self.password,
                                                           host=self.host,
                                                           port=self.port,
                                                           database=self.db_name)
            if self.pool:
                print("Connection pool created successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            traceback.print_exc()
            print("Error while connecting to PostgreSQL:", error)

    def getConnection(self):
        return self.pool.getconn()

    def closeAllConnection(self):
        self.pool.closeall()

    def execute(self, sql: str) -> dict[Any, Any]:
        try:
            con = self.getConnection()
            if con:
                cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
                cursor.execute(sql)
                records = cursor.fetchall()

                result = []
                for row in records:
                    result.append(dict(row))

                for row in result:
                    print(row)

                cursor.close()

                self.pool.putconn(con)
                return records
        except (Exception, psycopg2.DatabaseError) as error:
            traceback.print_exc()
            print("Error while executing PostgreSQL", error)

    def execute_file(self, sql_file_path: str) -> list:
        pass
