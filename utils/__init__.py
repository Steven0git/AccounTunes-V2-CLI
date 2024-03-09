from .CreateTable import CreateTable
from .Design import Art
from time import sleep
import datetime


class InitializeTables():
    def __init__(self):
        self.Create = CreateTable()
        self.art = Art()

    def create_tables(self):
        self.Create.TableCreate()