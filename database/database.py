from dotenv import load_dotenv
import os
import psycopg

load_dotenv()
db_config = {
    "dbname": os.getenv('DB_NAME'),
    "user": os.getenv('DB_USERNAME'),
    "password": os.getenv('DB_PASSWORD'),
    "host": os.getenv('DB_HOST'),
    "port": os.getenv('DB_PORT')
}

# Database management class
class Database:
    def __init__(self):
        self.conn = psycopg.connect(**db_config)
        self.cursor = self.conn.cursor()
        self.lunch_menus = self.select_data()

    def get_lunch_menus(self) -> list:
        lunch_menus = self.select_data()
        data = [vars(lunch_menu) for lunch_menu in lunch_menus]

        return data

    def execute_query(self, query, data=None):
        if data:
            self.cursor.execute(query, data)
        else:
            self.cursor.execute(query)
        self.conn.commit()

    # def insert_data(self, lunch_menu: LunchMenu):
    #     members = self.get_member_dict()
    #     data = (lunch_menu.menu_name, members[lunch_menu.member_name], lunch_menu.date)
    #     query = '''
    #     INSERT INTO lunch_menu (menu_name, member_id, dt)
    #     VALUES (%s, %s, %s)
    #     '''
    #     self.execute_query(query, data)

    def get_member_need_enter(self) -> list:
        query = '''
        select
            m.name
        from
            member m
        left join lunch_menu l
            on m.id = l.member_id and l.dt = current_date
        where
            l.member_id is null
        '''
        self.execute_query(query)
        results = self.cursor.fetchall()

        return ',  '.join([record[0] for record in results])

    def select_data(self) -> list:
        query = '''
        SELECT
            menu_name,
            name,
            dt
        FROM lunch_menu l
        JOIN member m ON l.member_id = m.id
        '''
        self.execute_query(query)
        data = self.cursor.fetchall()

        return data

    def get_member_dict(self) -> dict:
        query = '''
        SELECT jsonb_object_agg(name, id)
        FROM member;
        '''
        self.execute_query(query)
        return self.cursor.fetchone()[0]

    def close_connection(self):
        self.cursor.close()
        self.conn.close()