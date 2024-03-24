class Prompter:
    def __init__(self):
        pass

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
                self.error_message(
                    "Each item in my_list must be a dictionary and array [{}]!", False
                )
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

            elif name_type in ["input", "data", "prompt"]:
                if "title" not in data:
                    self.error_message("Title is required for data type prompt!", False)
                    return False
                user_input = self.prompt(data["title"])
                self._save((data["keys"], user_input))
            else:
                self.error_message("Invalid prompt type!", False)
                return False
        return True

    def prompt(self, message: str) -> str:
        """
        Prompts the user for input.

        Args:
            message (str): The prompt message.

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
            menu (dict): Dictionary containing menu options.

        Returns:
            int: Selected menu option index.
        """
        if type(menu.get("clean")) is bool and menu.get("clean") is True:
            self.art.menu_list(menu, True)
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
