from .Design import Art
import os
import sys
import re

class Engine:
    def __init__(self):
        self.art = Art()

    def prompt(self):
        pass

    def fprompt(self, prompt_msg: str, filetype: str):
        while True:
            self.art.ColorPrint(prompt_msg, 'green', '') 
            file_name = input()  # Get user input without coloring
            if self.is_exist(file_name, filetype):
                return file_name
            else:
                self.ErrorMessage(f"Error: Invalid filename format. It should be alphanumeric with a .{filetype} extension.")

    def is_exist(self, filename, filetype):
        pattern = fr'^[a-zA-Z0-9_]+\.{filetype}$'
        return bool(re.match(pattern, filename))

    def ErrorMessage(self, msg):
         self.art.ColorPrint(msg, 'red')

    @staticmethod
    def suppress_errors():
        try:
            if os.name == "posix":
                sys.stderr = open(os.devnull, "w")
            elif os.name == "nt":
                sys.stderr = open("NUL", "w")
        except Exception:
            pass