from utils.artisan.Engine import Engine
from .schema import SqlSchema 

class Store:
    """
    This class represents a temporary store.
    """

    def __init__(self):
        self.sql_scheme = SqlSchema()
        self.sql_engine = Engine()

    def get_insert_schema(self) -> list:
        """
      There are three type transaction, basic insert, planned expenditure, and evaluation data known as records
        """
        engine_sql = self.sql_engine
        scheme = self.sql_scheme
        scheme.set_method("insert")
        type_trans = [{
          "title": "What type transaction?",
          "list": ["Basic -> Basic Insert: Income and Expenditure","Plan -> Planned Expenditure","Record -> Records Data: Income or Expenditure"],
          "keys": "_root_trans_insert_type",
          "type": "menu"
        }]
        engine_sql.request_prompt(type_trans)
        data = engine_sql.get_temp_store() #the data is [()]
        print(data)
        if data[0][0] == "_root_trans_insert_type":
          splitter = data[0][1].lower().strip().split("->")
          scheme.run(True, splitter[0].strip())
        else:
          raise ValueError("Fuckoff you got wrong keys or empty!")
        return scheme.get_data()
     
    def get_select_schema(self):
        pass

    def get_tables_schema(self, list_tables: tuple):
        data = {
            "title": "Select Tables Name: ",
            "list": list_tables,
            "type": "menu",
            "keys": "tables_schema"
        }
        self.sql_engine.request_prompt(data)
        self.sql_engine.save()
        self.sql_engine.show("debug")
