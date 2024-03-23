from .temp_store import Store
from utils.artisan.Design import Art 
from time import sleep
import datetime

class InsertData:
  def __init__(self, connection):
    self.conn = connection
    self.store = Store()
    self.__open_variable = {
      
    }
    self.art = Art()
   
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
        self.__open_variable[get_true_variable] = val[1]
        
  def exec_insert(self):
    self.art.print_color("_"*50,"MAGENTA")
    self.art.print_color("\nData Retrieved!\n", "CYAN")
    sleep(1)
    self.art.spin_load("Loading...", 2)
   
    data_insert = self.store.get_insert_schema()
    print(data_insert)
    self.art.print_color("_"*50,"MAGENTA")
    self.art.print_color("Info: ","green")
    self.art.print_color("- Execution Begin....","red")
    
    #check type insert