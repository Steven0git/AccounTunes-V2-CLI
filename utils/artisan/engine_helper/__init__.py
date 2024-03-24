from .validation import Validation
from .storage import Storage 
from .show import Show
from .design import Art 
from .prompt import Prompter

class EngineUtils(Validation, Storage,Show,Prompter):
  def __init__(self):
    self._temp_store = ["tsst"] 
    self._data_store = {}
    self.art = Art()
   
    super().__init__()
   
  def getStore(self):
    return self.store

"""
Test = EngineUtils()
data = Test.data_dict({"file": "This is method from Show.py"})
print(data)
print(EngineUtils.mro())
"""
test2 = EngineUtils()
 
data = test2._temp_store
print(data)