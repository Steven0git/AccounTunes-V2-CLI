from .CreateTable import CreateTable
from .Design import Art


class InitializeTables():
    def __init__(self):
        self.Create = CreateTable()
        self.art = Art()

    def create_tables(self):
        self.Create.TableCreate()
        
    @property
    def SuppressError(self):
        import os
        import sys
        """
        Initializes the SuppressError class.
        """
        try:
            null_device = "NUL" if os.name == "nt" else os.devnull
            with open(null_device, "w") as f:
                sys.stderr = f
        except OSError:
            pass
