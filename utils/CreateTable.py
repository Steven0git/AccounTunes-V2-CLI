from .Connector import Connect
from .Engine import Engine

"""
 This is Class CreateTable.
 Method: 
   exec(): to do some transaction initialization statement from __init__.py 
    
"""


class CreateTable(Connect):
    def __init__(self):
        self.engine = Engine()
        DB_name = self.engine.fprompt("Your Database File Path: ", "db")
        super().__init__(DB_name)

    # Using transaction
    def exec(self, statement, params=None):
        cursor = super().Csr()
        try:
            cursor.execute("BEGIN TRANSACTION")

            if params:
                cursor.execute(statement, params)
            else:
                cursor.execute(statement)

            cursor.execute("COMMIT")
        except Exception as e:
            cursor.execute("ROLLBACK")
            print("An Error Occurred: ", e)
