from .Design import Art
from time import sleep


class Show:
    """
    The Show class is used to display information, such as JSON data. It can be utilized for exporting logs or selecting queries.
    """

    def __init__(self):
        """
        Initialize the Show Class
        """
        self.art = Art()
        self.print = self.art.print_color

    def readable(self, data: dict):
        """
        Read and display the dictionary data in a colorful and well-designed format.

        Args:
            data (dict): The dictionary containing keys and values to be displayed.
        """
        self.print("_" * 40, "MAGENTA")
        self.print("Your saved data: \n", "GREEN")
        for index, (key, value) in enumerate(data.items()):
            self.print(f"\t{index+1}: {key}", "yellow", "")
            self.print(" --> ", "RED", "")
            self.print(value, "green")
            sleep(0.1)
        self.print("_" * 40, "MAGENTA")
