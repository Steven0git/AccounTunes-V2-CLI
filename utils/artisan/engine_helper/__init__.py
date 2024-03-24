from .validation import Validation
from .storage import Storage 
from .show import Show
from .prompt import Prompter

class EngineHelper(Validation, Storage,Show,Prompter):
  def __init__(self):
    super().__init__()
 
  def get_temp_store(self) -> list:
     return self._temp_store
