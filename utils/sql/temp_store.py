from utils.artisan.Engine import Engine
"""
 This is known as temporary store
"""

class Store:
  def __init__(self):
    self.__insert_data = []
    self.__select_data = []
    self.sql_engine = Engine()

  def get_insert_schema(self):
    self.__insert_data.append({
      "order": 1,
      "data": "Name Transaction: ",
      "type": "prompt",
      "expected": str,
      "keys": "_trans_name"
    })
    self.__insert_data.append({
      "order": 2,
      "title": "What the type? ",
      "type": "menu",
      "list": ["Exp -> Expenditure", "Inc -> Income", "plan -> Accounting Plan", "rec -> Record total money you have"],
      "expected": int,
      "keys": "_trans_type"
    })
    self.__insert_data.append({
      "order": 3,
      "data": "Enter Amount: ",
      "type": "prompt",
      "expected": int or float,
      "keys": "_trans_amount"
    })
    self.__insert_data.append({
      "order": 4,
      "data": "Description Transaction: ",
      "type": "prompt",
      "expected": str,
      "keys": "_trans_desc"
    })
    self.__insert_data.append({
      "order": 5,
      "data": "Enter Date (YYYY-MM-DD): ",
      "type": "prompt",
      "expected": str,
      "keys": "_trans_date"
    })
    self.sql_engine.request_prompt(self.__insert_data)
    self.sql_engine.save()
    self.sql_engine.show()
  
# Selection perform
  def get_select_schema(self):
    pass
  
  def get_tables_schema(self, list_tables:tuple):
    data = {
      "title": "Select Tables Name: ",
      "list": list_tables,
      "type": "menu",
      "keys": "tables_schema"
    }
    self.sql_engine.request_prompt(data)
    self.sql_engine.save()
    self.sql_engine.show()