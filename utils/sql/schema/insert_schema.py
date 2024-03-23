class InsertSchema:
    def __init__(self):
        self.__data = []
        self.__encrypt = False
        self.__key
    def run(self, method: str):
        """
        There are three types: basic insert, planning insert, and records insert
        """
        method = method.lower()
        if method in ["basic", "plan", "record"]:
            return getattr(self, f"__insert_{method}_data")()
        else:
            raise ValueError("Info insert_schema.py: Method must be one of: basic, plan, or record")
    
    @property
    def get_data(self):
      if not self.__encrypt:
       return self.__data
      else:
       raise ValueError("Error: insert_schema.py\n The data is encrypted you must use key!")
    @get_data.setter
    def get_data(self,password: (int or str or float)):
      if self.__pass == password:
        return self.__data
      else:
        raise ValueError("Error! Keys invalid!")
    def __insert_basic_data(self):
      try:
        self.__add([0,"menu","What type transaction?","_trans_insert_type",["Income","Expenditure"]])
        self.__add([1,"prompt","Enter Name Transaction:","_trans_insert_name"])
        self.__add([2,"prompt","Description:","_trans_insert_desc"])
        self.__add([3,"prompt","Amount:","_trans_insert_amount"])
        self.__add([4,"prompt","Date(YYYY-MM-DD):","_trans_insert_date"])
      except ValueError as err:
        print("Error: ", err)
    def __insert_plan_data(self):
      pass
    def __insert_record_data(self):
      pass
    def __add(self, data: list) -> dict:
        """
        Method __add helps for InsertSchema self.__data.
        Args:
            data (list): 
                - First data must be "order" id.
                - Second data must be "type": prompt or menu.
                - Third data must be "title": title name.
                - Fourth data must be "keys" unique identifier: must start with _trans_insert_(your data)
                - The last one if you use menu must add "list" data: [list of menu]
        """
        add_result = {}
        if len(data) > 3:
            validate = self.__validate(data, [int, str, str, str])
            if validate:
                add_result["order"] = data[0]
                add_result["type"] = "prompt" if data[3].lower() in ["prompt", "input"] else "menu"
                add_result["title"] = data[2]
                add_result["keys"] = data[3]
                if add_result["type"] == "menu":
                    add_result["list"] = data[4] if len(data) > 4 else []
            else:
                raise ValueError("Error: insert_schema.py: Data invalid")
        else:
            raise ValueError("Info: insert_schema.py: Input data arguments required not fulfilled")
        self.__data.append(add_result)
    def __validate(self, data: list, fulfillment: list) -> bool:
        if len(data) == len(fulfillment):
            for index, sample in enumerate(data):
                if type(sample) != fulfillment[index]:
                    return False
            return True
        else:
            return False
