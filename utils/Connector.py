import sqlite3 as sql


# Connector to database.
class Connect:
    def __init__(self, db):
        self.db: str = db
        self.conn = sql.connect(self.db)

    def Csr(self):
        return self.conn.cursor()
