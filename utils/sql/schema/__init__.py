from .insert_schema import InsertSchema


class SqlSchema:
    def __init__(self):
        self.__result = None
        self.__type = None
        self.__output = None

    def set_method(self, method: str):
        if method.lower() in ["insert", "select", "update", "delete"]:
            self.__type = method.lower()
        else:
            raise ValueError(
                "Invalid method. Method must be one of: insert, select, update, delete"
            )

    def run(self, requirement=False, *additional_args):
        """
        This is the third method after set_method required.
        Args:
            requirement(bool): Whether additional arguments are required.
            additional_args: Additional user input.
        """
        title = f"sql_schema_{self.__type}"
        if self.__type:
            if not requirement:
                return self.sql_schema_insert()
            elif requirement and additional_args:
                return getattr(self, title)(True, *additional_args)
            else:
                raise ValueError("Additional arguments are required but not provided.")
        else:
            raise ValueError("Method not set.")

    def get_data(self):
        if self.__output:
            return self.__output
        else:
            raise ValueError("The data is empty!")

    def sql_schema_insert(self, arg=False, *args):
        schema_insert = InsertSchema()
        if arg is True and args:
            schema_insert.run(*args)
        else:
            schema_insert.run()
        data = schema_insert.get_data
        print(f"Your data: {data}")
        if data and isinstance(data, list):
            sorted_data = sorted(data, key=lambda x: x["order"])
            self.__output = sorted_data
        else:
            raise ValueError("There is an error in inserting data")

    def sql_schema_select(self):
        pass

    def sql_schema_update(self):
        pass

    def sql_schema_delete(self):
        pass
