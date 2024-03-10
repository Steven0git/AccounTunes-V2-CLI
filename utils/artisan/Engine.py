from .Design import Art
from time import sleep
import re
import os
import sys


class Engine:
    """
    Engine class containing methods for user interaction and file-related operations.
    """

    def __init__(self):
        """
        Initializes the Engine class.
        """
        self.art = Art()

    def prompt(self, args: str) -> str:
        """
        Prompts the user for input.

        Args:
            args (str): The prompt message.

        Returns:
            str: User input.
        """
        while True:
            self.art.print_color(f"\n{args}", "yellow", "")
            data_input = input()
            if len(data_input.strip()) < 3:
                self.error_message("C'mon don't play dumb on me!", False)
            else:
                if data := self.data_confirmation(data_input):
                    return data

    def select_menu(self, menu_available: list) -> int:
        """
        Displays a menu and prompts the user to select an option.

        Args:
            menu_available (list): List of menu options.

        Returns:
            int: Selected menu option.
        """
        while True:
            self.art.print_color("Select Menu:", "yellow", " ")
            try:
                menu_selected = int(input())
                if 1 <= menu_selected <= len(menu_available):
                    self.art.print_color(
                        f"\tSelected {menu_available[menu_selected-1]}", "green"
                    )
                    if data := self.data_confirmation(menu_selected):
                        return data
                else:
                    self.error_message("Wrong Selection!", False)
            except ValueError:
                self.error_message(
                    "Invalid input! Please enter a valid integer.", False
                )

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
            self.art.print_color(prompt_msg, "green", "")
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

    def data_confirmation(self, data):
        """
        Confirms user's input.

        Args:
            data: Data to confirm.

        Returns:
            data if confirmed, False otherwise.
        """
        self.art.print_color("\nAre you sure (yes/no/quit):", "yellow", " ")
        confirmation = input().lower()
        if confirmation in ["yes", "y"]:
            self.art.print_color("\tConfirmed!", "green")
            return data
        elif confirmation in ["q", "quit"]:
            self.art.print_color("\tTransaction cancelled.", "red")
            sys.exit(1)
        elif confirmation in ["no", "n"]:
            self.art.print_color("\tSelection canceled.", "red")
            return False
        else:
            self.error_message(
                "Invalid input. Please enter 'yes', 'no', or 'quit'.", False
            )
            self.data_confirmation(data)

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

    @property
    def SuppressError(self):
        """
        Suppresses error messages.
        """
        try:
            null_device = "NUL" if os.name == "nt" else os.devnull
            with open(null_device, "w") as f:
                sys.stderr = f
        except OSError:
            pass

 