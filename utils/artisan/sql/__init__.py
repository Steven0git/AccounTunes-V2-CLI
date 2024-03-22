from .insert_data import InsertData

class SQL:
    def __init__(self):
        pass

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
            print("Invalid method")
    def sql_table(self, name:str):
      print(name)
      pass
    
    def __select_data(self):
        print("Executing SELECT method")
    def __insert_data(self):
        print("Executing INSERT method")


# Example usage
sql = SQL()
sql.sql_helper("INSERT DATA")