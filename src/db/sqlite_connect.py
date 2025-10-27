import sqlite3

class SQLiteConnectionFactory:
    def __init__ (self, db_path: str):
        self.db_path = db_path
    
    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn


def init_db(conn_factory: SQLiteConnectionFactory):
    with conn_factory.get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensorId TEXT NOT NULL,
            temperature REAL NOT NULL,
            humidity REAL NOT NULL,
            timestamp TEXT NOT NULL
            );
        """)
        conn.commit()


    