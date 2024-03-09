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
        Header(title: str)
            Prints a styled header with the provided title.

        ColorPrint(name: str, color: str, end: str = "")
            Prints the given name in the specified color.

        Loading(name: str, duration: int)
            Displays a loading animation for the specified duration.

    """

    def __init__(self):
        # ANSI escape codes for colors
        self.GREEN = "\033[92m"
        self.YELLOW = "\033[93m"
        self.RED = "\033[91m"
        self.BLUE = "\033[94m"
        self.MAGENTA = "\033[95m"
        self.CYAN = "\033[96m"
        self.RESET = "\033[0m"

    def Header(self, title: str):
        """
        Prints a styled header with the provided title.

        Args:
            title (str): The title name for the header.
        """
        print(self.CYAN)
        print("_" * 50)
        print(self.RESET)
        print(f"\t{self.BLUE}{title}{self.RESET}{self.CYAN}")
        print("_" * 50)
        print(self.RESET)

    def ColorPrint(self, name: str, color: str, ends="\n"):
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

    def Loading(self, name: str, duration: int):
        """
        Displays a loading animation for the specified duration.

        Args:
            name (str): Name of the progress.
            duration (int): Duration of the loading animation in seconds.
        """
        widgets = [f"{self.YELLOW}{name}{self.RESET}", progressbar.AnimatedMarker()]
        bar = progressbar.ProgressBar(widgets=widgets).start()

        for i in range(1, duration + 1):
            sleep(1)
            bar.update(i)

        bar.finish()
