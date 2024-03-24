from .Design import Art
from .engine_helper import EngineHelper
from itertools import groupby
from time import sleep
import sys
import os


class Engine(EngineHelper):
    """
    A class responsible for user interaction and file-related operations.
    """

    def __init__(self):
        """
        Initializes the Engine class.
        """
        super().__init__()
        self.art = Art()
        self._temp_store = []
        self._data_store = {}
        self.count = 0


    def show(self, type_read: str):
        my_read = type_read.lower()
        if my_read == "debug":
            super().readable(self._data_store)
        elif my_read == "dict":
            return super().data_dict(self._data_store)

    def error_message(self, msg: str, clean_screen: bool = True):
        """
        Displays an error message.

        Args:
            msg (str): The error message to display.
            clean_screen (bool): Whether to clear the screen after displaying the message.
        """
        if len(msg.strip()):
            self.art.print_color(f"{msg}\n", "red")
        else:
            self.art.print_color("Error: Message not provided.\n", "red")
        if clean_screen:
            sleep(0.8)
            os.system("cls" if os.name == "nt" else "clear")
    def suppress_error(self):
        """
        Suppresses error messages.
        """
        try:
            null_device = "NUL" if os.name == "nt" else os.devnull
            with open(null_device, "w") as f:
                sys.stderr = f
        except OSError:
            pass
 