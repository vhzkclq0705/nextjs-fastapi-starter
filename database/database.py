from dotenv import load_dotenv
import os
import psycopg
from psycopg.rows import dict_row

load_dotenv()
db_config = {
    "dbname": os.getenv("POSTGRES_DATABASE"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT", "5432")
}

# Database management class
class Database:
    def get_lunch_menus(self) -> list:
        lunch_menus = self.select_data()
        data = [vars(lunch_menu) for lunch_menu in lunch_menus]

        return data

    def execute_query(self, query, data=None) -> list:
        with psycopg.connect(**db_config, row_factory=dict_row) as conn:
            cur = conn.execute(query)
            row = cur.fetchall()
            return row

    def select_data(self) -> list:
        query = "SELECT * FROM view_select_all"
        data = self.execute_query(query)
        return data