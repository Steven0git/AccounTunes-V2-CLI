from .artisan.Design import Art
from .artisan.Engine import Engine
from .core.CreateTable import CreateTable
import sqlite3 as sql
import os
import time


class Connect:
    """
    This class handles the connection to the database.

    Methods:
        __init__(db: str)
            Initializes the Connect object and establishes a connection to the database.

        cursor()
            Returns a cursor object for executing SQL commands on the connected database.
    """

    def __init__(self, db=None):
        self.engine = Engine()
        self.art = Art()
        self.conn = None
        self.db = db if db else self._prompt_database_path()
        self.checker()
        time.sleep(1)
        self.makeTable()

    def checker(self):
        time.sleep(1)
        if os.path.exists(self.db):
            self.art.Header("AccountingApp V2")
            self.art.Loading("Connecting Into Database...", 2)
            self.conn = sql.connect(self.db)
            print()
            self.art.print_color("Successfully Connected Into Database!", "green")
            print()
            time.sleep(1)
            self.art.Loading("Cursoring data....", 3)
            self.art.print_color("Done!\n", "green")

        else:
            raise FileNotFoundError(self.art.print_color("File Not Found!", "red"))

    def makeTable(self):
        make = CreateTable(self.conn.cursor())
        make.create_table()

    def _prompt_database_path(self):
        return self.engine.fprompt("Enter Database Name: ", "db")
