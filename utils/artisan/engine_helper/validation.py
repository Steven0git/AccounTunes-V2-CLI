from time import sleep
import sys


class Validation:
    def is_valid_filename(self, filename: str, filetype: str) -> bool:
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
