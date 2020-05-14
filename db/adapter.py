import mysql.connector
from conf.config import Configuration

class Database:

    def __init__(self):
        self.db = mysql.connector.connect(
            host=Configuration.DB_HOST,
            user=Configuration.DB_USER,
            passwd=Configuration.DB_PASS,
            database=Configuration.DB_NAME
        )


    def execute(self, query):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(query)


    def select(self, query):
        cursor = self.db.cursor()
        cursor.execute(query)

        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return rows


    def commit(self):
        self.db.commit()








