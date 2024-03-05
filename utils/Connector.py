import sqlite3 as sql
import os
from time import sleep
from .Design import Art


class Connect:
    """
    This class handles the connection to the database.

    Methods:
        __init__(db: str)
            Initializes the Connect object and establishes a connection to the database.

        Csr()
            Returns a cursor object for executing SQL commands on the connected database.
    """

    def __init__(self, db: str):
        """
        Initializes the Connect object and establishes a connection to the database.

        Args:
            db (str): Path to the database file.
        """
        self.db = db
        self.art = Art()
        self.art.Header("AccountingApp V2")
        sleep(1)
        self.art.Loading("Connecting Into Database...", 4)
        if os.path.exists(self.db):
            self.conn = sql.connect(self.db)
            print()
            self.art.ColorPrint("Successfully Connected Into Database!", "green")
            print()
            sleep(1)
        else:
            raise FileNotFoundError(self.art.ColorPrint("File Not Found!", "red"))

    def Csr(self):
        """
        Returns a cursor object for executing SQL commands on the connected database.

        Returns:
            Cursor: Cursor object for executing SQL commands.
        """
        return self.conn.cursor()
