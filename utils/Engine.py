from .Design import Art
from time import sleep
import re
import os

class Engine:
    """
    Engine Class with file-related methods.
    """

    def __init__(self):
        """
        Initializes the Engine class.
        """
        self.art = Art()

    def prompt(self):
        """
        Prompts the user.
        """
        pass

    def fprompt(self, prompt_msg: str, filetype: str) -> str:
        """
        Prompts the user for a filename with the specified filetype format.

        Args:
            prompt_msg (str): The prompt message.
            filetype (str): The filetype format.

        Returns:
            str: The valid filename entered by the user.
        """
        while True:
            self.art.ColorPrint(prompt_msg, "green", "")
            file_name = input()

            if self.is_valid_filename(file_name, filetype):
                return file_name
            else:
                self.error_message(
                    f"Error: Invalid filename format. It should be alphanumeric with a .{filetype} extension."
                )

    def is_valid_filename(self, filename: str, filetype: str) -> bool:
        """
        Checks if the filename has the specified filetype format.

        Args:
            filename (str): The filename to check.
            filetype (str): The filetype format.

        Returns:
            bool: True if the filename has the correct format, False otherwise.
        """
        pattern = re.compile(rf"^[a-zA-Z0-9_]+\.{filetype}$")
        return bool(pattern.match(filename))

    def error_message(self, msg: str):
        """
        Displays an error message.

        Args:
            msg (str): The error message to display.
        """
        if len(msg.strip()):
            self.art.ColorPrint(f"{msg}\n", "red")
        else:
            self.art.ColorPrint("You're an asshole! add some words!\n", "red")
        sleep(0.8)
        os.system("cls" if os.name == "nt" else "clear")

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
