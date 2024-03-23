class InsertSchema:
  def __init__(self):
    self.__data = []
    self.__encrypt = False

  def run(self, method: str):
    """
    There are three types: basic insert, planning insert, and records insert
    """
    method = method.lower()
    if method in ["basic", "plan", "record"]:
      return getattr(self, f"insert_{method}_data")()
    else:
      raise ValueError("Info: insert_schema.py: Method must be one of: basic, plan, or record")

  @property
  def get_data(self):
    if not self.__encrypt:
      return self.__data
    else:
      raise ValueError("Error: insert_schema.py\n The data is encrypted you must use key!")

  @get_data.setter
  def get_data(self, password: (int or str or float)):
    if self.__encrypt:  # Check encryption before password comparison
      if password == self.__encrypt_key:  # Use a defined key for encryption
        return self.__data
      else:
        raise ValueError("Error! Keys invalid!")
    else:
      raise ValueError("Data is not encrypted. No key required.")

  def insert_basic_data(self):
    try:
      self.add_data([0, "menu", "What type transaction?", "_trans_insert_type", ["Income", "Expenditure"]])
      self.add_data([1, "prompt", "Enter Name Transaction:", "_trans_insert_name"])
      self.add_data([2, "prompt", "Description:", "_trans_insert_desc"])
      self.add_data([3, "prompt", "Amount:", "_trans_insert_amount"])
      self.add_data([4, "prompt", "Date(YYYY-MM-DD):", "_trans_insert_date"])
    except ValueError as err:
      print("Error: ", err)

  def insert_plan_data(self):
    pass

  def insert_record_data(self):
    pass

  def add_data(self, data: list) -> dict:
    """
    Method to add data to the internal list with validation.
    Args:
      data (list): List containing data following the specified format.
    """
    add_result = {}
    if len(data) > 3:
      is_valid = self.validate_data(data, [int, str, str, str])
      if is_valid:
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

  def validate_data(self, data: list, fulfillment: list) -> bool:
    """
    Validates data against the expected data types.
    Args:
      data (list): List containing data to validate.
      fulfillment (list): List containing expected data types.
    Returns:
      bool: True if data is valid, False otherwise.
    """
    if len(data) == len(fulfillment):
      for index, sample in enumerate(data):
        if type(sample) != fulfillment[index]:
          return False
      return True
    else:
      return False
