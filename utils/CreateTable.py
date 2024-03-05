from .Connector import Connect
 

# Creating Table:
class CreateTable(Connect):
    def __init__(self):
        DB_name = input("Enter Database Name: ")
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
