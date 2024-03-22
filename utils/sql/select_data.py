from .temp_store import Store

class SelectData:
  def __init__(self, connection):
    self.conn = connection
    self.cursor = connection.cursor()
    self.store = Store()
    self.__tables = ()
  
  def show_all_tables(self):
    self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = self.cursor.fetchall()
    for table in tables:
      self.__tables.append(table[0])
    self.store.get_tables_schema(self.__tables)
  def select_tables_name(self):
    self.store.get_tables_schema(self.__tables)
    
  def perform_selection_data(self):
    pass