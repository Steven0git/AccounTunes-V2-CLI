from utils.artisan.Engine import Engine
from .schema import SqlSchema 

class Store:
    """
    This class represents a temporary store.
    """

    def __init__(self):
        self.sql_scheme = SqlSchema()
        self.sql_engine = Engine()

    def get_insert_schema(self):
        """
      There are three type transaction, basic insert, planned expenditure, and evaluation data known as records
        """
        engine_sql = self.sql_engine
        type_trans = [{
          "title": "What type transaction?",
          "list": ["Basic Insert","Planned Expenditure","Records Data: Income or Expenditure"],
          "keys": "_root_trans_insert_type",
          "type": "menu"
        }]
        engine_sql.request_prompt(type_trans)
        data = engine_sql.get_temp_store()
        print(data)
        #self.sql_engine.show("debug")
        #return self.sql_engine.show("dict")
     
    def get_select_schema(self):
        # Implement select schema functionality here
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
