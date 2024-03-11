from .Design import Art
from .Show import Show
from itertools import groupby
from time import sleep
import sys
import os


class Engine(Show):
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

    def prompt(self, message: str) -> str:
        """
        Prompts the user for input.

        Args:
            args (str): The prompt message.

        Returns:
            str: User input.
        """
        args = message
        if not message.strip().endswith(":"):
          args = f"{message}: "
        while True:
            self.art.print_color(f"\n{args}", "yellow", "")
            data_input = input()
            if len(data_input.strip()) < 3:
                self.error_message("Input should be at least 3 characters long.", False)
            else:
                if data := self.data_confirmation(data_input):
                    return data

    def select_menu(self, menu: dict) -> int:
        """
        Displays a menu and prompts the user to select an option.

        Args:
            menu_available (list): List of menu options.

        Returns:
            int: Selected menu option.
        """
        if self.count == 0:
            self.art.menu_list(menu, True)
            self.count += 1
        else:
            self.art.menu_list(menu, False)
         
        menu_available = menu["list"]
        while True:
            self.art.print_color("Select Menu:", "yellow", " ")
            try:
                menu_selected = int(input())
                if 1 <= menu_selected <= len(menu_available):
                    self.art.print_color(
                        f"\tSelected {menu_available[menu_selected-1]}", "green"
                    )
                    if data := self.data_confirmation(str(menu_selected)):
                        return int(data) - 1
                else:
                    self.error_message(
                        "Invalid selection! Please choose a valid option.", False
                    )
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
                    f"Error: Invalid filename format. It should be alphanumeric with a {filetype} extension."
                )

    def request_prompt(self, my_list: list) -> bool:
      """
    Processes user prompt requests.

    Args:
        my_list (list): List containing prompt data.

    Returns:
        bool: True if prompt was successfully processed, False otherwise.
      """
      for data in my_list:
        if not isinstance(data, dict):
            self.error_message("Each item in my_list must be a dictionary!", False)
            return False

        if not all(key in data for key in ["type", "keys"]):
            self.error_message("Title, Type, and keys are required fields!", False)
            return False

        name_type = data.get("type", "").lower()
        if name_type == "menu":
            if "list" not in data:
                self.error_message("Menu list is required!", False)
                return False
            menu = self.select_menu(data)
            self._save((data["keys"], data["list"][menu]))
        elif name_type == "data":
            if "title" not in data:
                self.error_message("Title is required for data type prompt!", False)
                return False
            user_input = self.prompt(data["title"])
            self._save((data["keys"], user_input))
        else:
            self.error_message("Invalid prompt type!", False)
            return False

      return True

    @staticmethod
    def is_valid_filename(filename: str, filetype: str) -> bool:
        """
        Checks if the filename has the specified filetype format.

        Args:
            filename (str): The filename to check.
            filetype (str): The filetype format.

        Returns:
            bool: True if the filename has the correct format, False otherwise.
        """
        if filetype.startswith("."):
            return filename.endswith(filetype)
        else:
            return filename.endswith(f".{filetype}")

    def data_confirmation(self, data):
        """
        Confirms user's input.

        Args:
            data: Data to confirm.

        Returns:
            data if confirmed, False otherwise.
        """
        sleep(0.4)
        self.art.print_color("\nAre you sure (yes/no/quit):", "yellow", " ")
        confirmation = input().lower()
        sleep(0.4)
        if confirmation in ["yes", "y"]:
            self.art.print_color("\tConfirmed!", "green")
            return data
        elif confirmation in ["q", "quit"]:
            self.art.print_color("\tTransaction cancelled.", "red")
            sys.exit(0)
        elif confirmation in ["no", "n"]:
            self.art.print_color("\tSelection canceled.", "red")
            return False
        else:
            self.error_message(
                "Invalid input. Please enter 'yes', 'no', or 'quit'.", False
            )
            return self.data_confirmation(data)

    def save(self) -> bool:
        """
        Saves all prompt data for execution.
        """
        if self._temp_store:
            for key, group in groupby(self._temp_store, key=lambda x: x[0]):
                self._data_store[key] = next(group)[1]
            return True
        else:
            return False

    def _save(self, data: tuple) -> bool:
        """
        Saves temporary data.

        Args:
            data(tuple): It only accepts tuples of length 2.
        """
        if len(data) == 2:
            self._temp_store.append(data)
            return True
        else:
            self.error_message("Error: Invalid data format.", False)
            return False

    def show(self):
        super().readable(self._data_store)

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
         
          