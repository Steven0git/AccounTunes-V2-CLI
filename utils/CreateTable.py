from .Connector import Connect
from .Engine import Engine
from .Design import Art
from time import sleep
import datetime
"""
 This is Class CreateTable.
 Method: 
   exec(): to do some transaction initialization statement from __init__.py 
    
"""


class CreateTable(Connect):
    def __init__(self):
        self.engine = Engine()
        self.art = Art()
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
    
    def TableCreate(self):
        date = datetime.datetime.now()
        month_name = date.strftime("%B")
        self.art.Loading("Creating Table...", 2)
        try:
            sql_statements = [
                f"""
                CREATE TABLE IF NOT EXISTS info_{month_name} (
                    id INTEGER PRIMARY KEY,  
                    name TEXT,  
                    transaction_type TEXT CHECK(transaction_type IN ('income', 'expenditure', 'planned_exp', 'record')),  
                    description TEXT,  
                    trans_id INTEGER,  
                    FOREIGN KEY(trans_id) REFERENCES "transaction"(id)  
                )
                """,
                f"""
                CREATE TABLE IF NOT EXISTS "transaction_{month_name}" (
                    id INTEGER PRIMARY KEY,  
                    transaction_type TEXT CHECK(transaction_type IN ('income', 'expenditure')),
                    amount REAL,  
                    date DATE  
                )
                """,
                f"""
                CREATE TABLE IF NOT EXISTS transaction_plan_{month_name} (
                    id INTEGER PRIMARY KEY,  
                    amount REAL NOT NULL,  
                    date_start DATE NOT NULL,  
                    date_end DATE NOT NULL,  
                    trans_id INTEGER NOT NULL,  
                    FOREIGN KEY(trans_id) REFERENCES info_{month_name}(id)  
                )
                """,
                f"""
                CREATE TABLE IF NOT EXISTS eval_transaction_{month_name} (
                    id INTEGER PRIMARY KEY,  
                    total REAL NOT NULL,  
                    saved REAL NOT NULL,  
                    date DATE NOT NULL,  
                    info_id INTEGER,  
                    FOREIGN KEY(info_id) REFERENCES info_{month_name}(id)  
                )
                """,
                f"""
                CREATE TABLE IF NOT EXISTS log_trans_{month_name} (
                    id INTEGER PRIMARY KEY,  
                    date DATE,  
                    transaction_type TEXT CHECK(transaction_type IN ('income', 'expenditure')),  
                    trans_id INTEGER,  
                    FOREIGN KEY(trans_id) REFERENCES "transaction_{month_name}"(id)  
                )
                """,
                f"""
                CREATE TRIGGER IF NOT EXISTS log_transaction_trigger_{month_name} AFTER INSERT ON "transaction_{month_name}"
                BEGIN
                    INSERT INTO log_trans_{month_name} (date, transaction_type, trans_id)  
                    VALUES (NEW.date, NEW.transaction_type, NEW.id);
                END;
                """,
            ]

            for statement in sql_statements:
                self.exec(statement)
            sleep(1)
            self.art.ColorPrint(".....", "cyan")
            sleep(2)
            self.art.ColorPrint("Table successfully created!", "green")
            self.art.ColorPrint(".....", "cyan")
            sleep(1)
            print("\n")
        except Exception as e:
            raise self.art.ColorPrint(f"Error: {e}", "red")
        finally:
            self.art.ColorPrint("Creation Complete!", "YELLOW")
