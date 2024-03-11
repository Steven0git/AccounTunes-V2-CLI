from sys import exit
import os
from time import sleep
import progressbar


class Art:
    """
    This class provides styling options for text, such as headers and colored printing,
    as well as a loading animation.

    Attributes:
        GREEN (str): ANSI escape code for green color.
        YELLOW (str): ANSI escape code for yellow color.
        RED (str): ANSI escape code for red color.
        BLUE (str): ANSI escape code for blue color.
        MAGENTA (str): ANSI escape code for magenta color.
        CYAN (str): ANSI escape code for cyan color.
        RESET (str): ANSI escape code to reset text color to default.

    Methods:
        print_header(title: str)
            Prints a styled header with the provided title.

        print_color(name: str, color: str, end: str = "")
            Prints the given name in the specified color.

        spin_loadname: str, duration: int)
            Displays a loading animation for the specified duration.

        menu_list(data, clean: bool = False)
            Prints a menu list with optional screen cleaning.
    """

    def __init__(self):
        self.GREEN = "\033[92m"
        self.YELLOW = "\033[93m"
        self.RED = "\033[91m"
        self.BLUE = "\033[94m"
        self.MAGENTA = "\033[95m"
        self.CYAN = "\033[96m"
        self.RESET = "\033[0m"

    def print_header(self, title: str, type='main'):
        """
        Prints a styled header with the provided title.

        Args:
            title (str): The title name for the header.
            type (str): only have main and sub
        """
        if type.lower() == 'main':
          
          self.print_color("_" * 50,"blue")
          print()
          self.print_color(f"\t{title.upper()}", "CYAN")
          self.print_color("_"*50, "blue")
          print(self.RESET)
          
        elif type.lower() == 'sub':
          self.print_color("-"*40,"MAGENTA")
          self.print_color(f"\t{title}","GREEN")
          self.print_color("-"*40,"MAGENTA")
   

    def print_color(self, name: str, color: str, ends="\n"):
        """
        Prints the given name in the specified color.

        Args:
            name (str): The text to be printed.
            color (str): The color to apply to the text.
            end (str, optional): The ending character(s) for the print statement. Default is an empty string.
        """
        color_upper = color.upper()
        if hasattr(self, color_upper):
            color_code = getattr(self, color_upper)
            print(f"{color_code}{name}{self.RESET}", end=ends)
        else:
            print(f"Color '{color}' not found.")

    def spin_load(self, name: str, duration: int, color: str = "YELLOW"):
        """
        Displays a loading animation for the specified duration.

        Args:
            name (str): Name of the progress.
            duration (int): Duration of the loading animation in seconds.
            color (str, optional): The color of the loading bar. Defaults to "YELLOW".
        """
        color_upper = color.upper()
        if not hasattr(self, color_upper):
            self.print_color("\n\tYou're Jerks!", "RED")
            sleep(0.4)
            self.print_color("\tError: Color name not found.", "RED")
            exit(1)

        widgets = [
            f"{getattr(self, color_upper)}{name}{self.RESET}",
            progressbar.AnimatedMarker(),
        ]
        bar = progressbar.ProgressBar(widgets=widgets).start()
        for i in range(duration * 10):
            sleep(0.1)
            bar.update(i)

        bar.finish()

    def menu_list(self, data:dict, clean: bool = False):
        """
        Prints a menu list with optional screen cleaning.

        Args:
            data (dict): Dictionary containing title menu and list of data.
            clean (bool, optional): Whether to clean the screen before printing. Defaults to False.
        """
        
        sleep(0.5)
        #check args clean
        if clean:
            self.spin_load("Your screen is dirty, some cleaning....", 2)
            os.system("cls" if os.name == "nt" else "clear")

         
        self.print_header(f'\t{data["title"].upper()}', "sub")
        self.spin_load("listing...", 1, "MAGENTA")
        
        self.print_color("\nList of menu:", "GREEN")
        
        for index, item in enumerate(data["list"], start=1):
            self.print_color(f"\t{index}: ", "GREEN", " ")
            self.print_color(item, "YELLOW")
            sleep(0.3)
