"""
 Class InsertSchema, is used for data_insert its help for basis query.
 Route Method:
  1. start with initialize the class.
  2. then use run() must have args method name.
  3. after that you can get_data() the output a list
"""


class InsertSchema:
    def __init__(self):
        self.__data = []
        self.__encrypt = False

    def run(self, method: str):
        method = method.lower()
        if method in ["basic", "plan", "record"]:
            return getattr(self, f"insert_{method}_data")()
        else:
            raise ValueError(
                "Info: insert_schema.py: Method must be one of: basic, plan, or record"
            )

    @property
    def get_data(self) -> list:
        if not self.__encrypt:
            return self.__data
        else:
            raise ValueError(
                "Error: insert_schema.py\n The data is encrypted you must use key!"
            )

    @get_data.setter
    def get_data(self, password: (int, str, float)):
        if self.__encrypt and password == self.__encrypt_key:
            return self.__data
        raise ValueError(
            "Error! Keys invalid!"
            if self.__encrypt
            else "Data is not encrypted. No key required."
        )

    def insert_basic_data(self):
        """
        DON'T TOUCH THIS!

        insert_basic_data, fundamental inserting data.
        """
        self.add_data(
            [
                0,
                "menu",
                "What type transaction?",
                "_trans_insert_type",
                ["Income", "Expenditure"],
            ]
        )
        self.add_data([1, "prompt", "Enter Name Transaction:", "_trans_insert_name"])
        self.add_data([2, "prompt", "Description:", "_trans_insert_desc"])
        self.add_data([3, "prompt", "Amount:", "_trans_insert_amount"])
        self.add_data([4, "prompt", "Date(YYYY-MM-DD):", "_trans_insert_date"])

    def insert_plan_data(self):
        pass

    def insert_record_data(self):
        pass

    def add_data(self, data: list) -> None:
        """
        The bone or skeleton of adding the data.
        """
        if len(data) > 3:
            is_valid = self.validate_data(
                data,
                [int, str, str, str, list]
                if data[1] == "menu"
                else [int, str, str, str],
            )
            if is_valid:
                add_result = {
                    "order": data[0],
                    "type": "prompt"
                    if data[1].lower() in ["prompt", "input"]
                    else "menu",
                    "title": data[2],
                    "keys": data[3],
                }
                if add_result["type"] == "menu":
                    add_result["list"] = data[4]
                    add_result["clean"] = False
                self.__data.append(add_result)
            else:
                raise ValueError("Error: insert_schema.py: Data invalid")
        else:
            raise ValueError(
                "Info: insert_schema.py: Input data arguments required not fulfilled"
            )

    @staticmethod
    def validate_data(data: list, fulfillment: list) -> bool:
        """
        validate your data:
        Args:
         data and fulfillment must same
        """
        return len(data) == len(fulfillment) and all(
            type(sample) == expected_type
            for sample, expected_type in zip(data, fulfillment)
        )
