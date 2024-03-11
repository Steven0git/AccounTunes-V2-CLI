from utils.artisan.Engine import Engine
from utils.artisan.Design import Art
from time import sleep
import datetime

"""
 This is Class CreateTable.
 Method: 
   exec(): to do some transaction initialization statement from __init__.py 
    
"""


class CreateTable:
    def __init__(self, cursor):
        self.art = Art()
        self.cursor = cursor

    def exec(self, statement, params=None):
        try:
            self.cursor.execute("BEGIN TRANSACTION")

            if params:
                self.cursor.execute(statement, params)
            else:
                self.cursor.execute(statement)

            self.cursor.execute("COMMIT")
        except Exception as e:
            self.cursor.execute("ROLLBACK")
            print("An Error Occurred: ", e)

    def create_table(self):
        date = datetime.datetime.now()
        month_name = date.strftime("%B")
        self.art.print_color("Now, let's get down to business - creating a table!", "cyan")
        sleep(1)
        self.art.spin_load("Creating some shit...", 2)
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
            self.art.print_color("..."*17, "cyan")
            sleep(1)
            self.art.print_color("Table successfully created! And just like that, After long long query statement.", "green")
            self.art.print_color("..."*17, "cyan")
            sleep(2)
            print("\n")
        except Exception as e:
            raise self.art.print_color(f"Error: {e}", "red")
        finally:
            self.art.print_color("Creation complete! It's like hitting the 'start' button on a well-oiled machine - now, let the accounting adventures begin!", "YELLOW")
