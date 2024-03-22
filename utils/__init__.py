from .artisan.Design import Art
from .artisan.Engine import Engine
from .core.CreateTable import CreateTable
import sqlite3 as sql
import os
import time


class Connect:
    """
    The Connect class is your gateway to the database world. It's like a magic portal to store and retrieve data!

    Methods:
        __init__(db: str)
            Prepare yourself for the adventure as you initialize the Connect object and journey into the database realm.
    """

    def __init__(self, db=None):
        self.engine = Engine()
        self.art = Art()
        self.conn = None
        self.db = db if db else self._prompt_database_path()
        self.checker()
        time.sleep(1)
        self.makeTable()
        self.open_panel()

    def checker(self):
        time.sleep(1)
        if os.path.exists(self.db):
            self.art.print_color("So, you've entered the database name as", "cyan", " ")
            self.art.print_color(f'"{self.db}"', "yellow", " ")
            self.art.print_color("? Well, Enjoy the ride!", "cyan")
            time.sleep(1.5)
            self.art.print_header("Welcome to the Accounting App V2!")
            self.art.spin_load("Connecting to the database...", 2)
            self.conn = sql.connect(self.db)
            print()
            self.art.print_color(
                "Success! You're now officially in the Matrix of financial wizardry! ",
                "green",
            )
            print()
            time.sleep(1)
            self.art.spin_load(
                "Gathering your data...", 3
            )
            time.sleep(0.5)
            self.art.print_color(
                "Voila! Data collection complete! We've scooped up those numbers faster than a kid in a candy store!\n",
                "green",
            )
        else:
            raise FileNotFoundError(
                self.art.print_color("Oops! File Not Found!", "red")
            )

    def makeTable(self):
        make = CreateTable(self.conn.cursor())
        make.create_table()

    def _prompt_database_path(self):
        return self.engine.fprompt("Enter Database Name: ", "db")
    
    def open_panel(self):
      """
     Panel Selection 
      """
      menu_offered = [{
          "title": "What You Wanted Todo",
          "list": ["SELECT DATA","INSERT DATA", "UPDATE DATA", "DELETE DATA"],
          "type": "menu",
          "keys": "_sql_method"
        }]
      self.engine.request_prompt(menu_offered)
     