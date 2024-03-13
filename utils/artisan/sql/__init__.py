class SQL:
    def __init__(self):
        pass

    def sql_helper(self, method: str):
        method_map = {
            "insert": self.__insert,
            "select": self.__select
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
    def __select(self):
        print("Executing SELECT method")

    def __insert(self):
        print("Executing INSERT method")


# Example usage
sql = SQL()
sql.sql_helper("INSERT DATA")