from .Design import Art
from time import sleep

class Show:
  def __init__(self):
    self.art = Art()
    self.print = self.art.print_color
    
  def readable(self, data: dict):
    self.print("_"*40, "MAGENTA")
    self.print("Your saved data: \n", "GREEN")
    for index,(key, value) in enumerate(data.items()):
      self.print(f"\t{index+1}: {key}", "yellow", "")
      self.print(" --> ", "RED", "")
      self.print(value, "green")
      sleep(0.1)
    self.print("_"*40, "MAGENTA")