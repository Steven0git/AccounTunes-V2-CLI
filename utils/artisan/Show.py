from .Design import Art
from tabulate import tabulate
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
        table_data = [[key, value] for key, value in data.items()]
        self.print(f"\n{tabulate(table_data, headers=['id','Keys', 'Value'], tablefmt='gird', numalign='center',stralign='center', showindex=True)}", "cyan")
    
    def data_dict(self, data:dict):
      print(data)
      return data