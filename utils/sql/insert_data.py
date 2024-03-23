from .temp_store import Store
from utils.artisan.Design import Art 
from utils.artisan.Engine import Engine 
from time import sleep
import datetime

class InsertData:
  def __init__(self, connection):
    self.conn = connection
    self.store = Store()
    self.__table_column = {}
    self.art = Art()
    self.engine = Engine()
   
  def get_next_id(self) -> int:
        table_name = f"info_{datetime.datetime.now().strftime('%B')}"
        cursor = self.conn.cursor()
        # Retrieve the maximum ID from the specified table
        cursor.execute(f"SELECT MAX(id) FROM {table_name}")
        max_id = cursor.fetchone()[0]
       
        if max_id is None:
            next_id = 1
        else:
            next_id = max_id + 1
        return next_id
  def data_handler(self,data:dict):
    #checking if all data is insert type.
    for key,val in enumerate(data.items()):
      if val[0].startswith("_trans_insert"):
        # only works if _ one data
        get_true_variable = val[0].split("_trans_insert_")[-1]
        self.__table_column[get_true_variable] = val[1]
        
  def exec_insert(self):
    self.art.print_header("INSERT - TRANSACTION", "sub")
    self.art.print_color(" \nInfo: ask user input","green")
    my_prompt_list = self.store.get_insert_schema()
    self.engine.request_prompt(my_prompt_list)
    self.art.spin_load("Saving your prompt...",2)
    self.save()
    self.art.print_color("\nHere your data: ", "green")
    self.show("debug")