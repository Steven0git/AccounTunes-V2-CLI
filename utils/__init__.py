from CreateTable import CreateTable
import datetime

if __name__ == "__main__":
    date = datetime.datetime.now()  # Use datetime.datetime.now() instead of datetime.now()
    month_name = date.strftime("%B")  # Get the full name of the current month
    sql_statements = [
        # Table: info_{month_name}
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

        # Table: "transaction_{month_name}"
        f"""
        CREATE TABLE IF NOT EXISTS "transaction_{month_name}" (
            id INTEGER PRIMARY KEY,  
            transaction_type TEXT CHECK(transaction_type IN ('income', 'expenditure')),
            amount REAL,  
            date DATE  
        )
        """,

        # Table: transaction_plan_{month_name}
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

        # Table: eval_transaction_{month_name}
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

        # Table: log_trans_{month_name}
        f"""
        CREATE TABLE IF NOT EXISTS log_trans_{month_name} (
            id INTEGER PRIMARY KEY,  
            date DATE,  
            transaction_type TEXT CHECK(transaction_type IN ('income', 'expenditure')),  
            trans_id INTEGER,  
            FOREIGN KEY(trans_id) REFERENCES "transaction_{month_name}"(id)  
        )
        """,

        # Trigger: log_transaction_trigger_{month_name}
        f"""
        CREATE TRIGGER IF NOT EXISTS log_transaction_trigger_{month_name} AFTER INSERT ON "transaction_{month_name}"
        BEGIN
            INSERT INTO log_trans_{month_name} (date, transaction_type, trans_id)  
            VALUES (NEW.date, NEW.transaction_type, NEW.id);
        END;
        """
    ]
    Create = CreateTable()
    for statement in sql_statements:
        Create.exec(statement)