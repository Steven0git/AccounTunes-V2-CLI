from .select_data import SelectData
from .insert_data import InsertData
from utils.artisan.Design import Art
import sqlite3 as sql 

class SQLHandler:
    def __init__(self):
        self.conn = None
        self.art = Art()
        self.print = self.art.print_color
        
    def sql_helper(self, method: str):
        method_map = {
            "insert": self.__insert_data,
            "select": self.__select_data
        }
        function_name = method.replace("DATA","").strip().lower()
        method_function = method_map.get(function_name)
        if method_function:
            method_function()
        else:
            self.print("Error! Method doesn't exists!","RED")
            
    def my_connect(self, db_name:str):
        self.conn = sql.connect(db_name)
        
    def sql_table(self, name:str):
        print(name)
        pass
    
    def __select_data(self):
        data_select = SelectData(self.conn)
        data_select.show_all_tables()
        
    def __insert_data(self):
        insert = InsertData(self.conn)
        data = insert.exec_insert()
          #print(data)

 