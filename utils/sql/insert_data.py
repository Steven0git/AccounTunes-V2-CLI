from temp_store import Store

class InsertData:
  def __init__(self, connection):
    self.conn = connection
    self.cursor = connection.cursor()
    self.store = Store().get_insert_schema()
  
  def get_next_id(self, table_name:str) -> int:
        cursor = self.cursor
        # Retrieve the maximum ID from the specified table
        cursor.execute(f"SELECT MAX(id) FROM {table_name}")
        max_id = cursor.fetchone()[0]
       
        if max_id is None:
            next_id = 1
        else:
            next_id = max_id + 1
        return next_id
  
  
"""
import sqlite3

def get_next_id(table_name):
    try:
        conn = sqlite3.connect('your_database_name.db')
        cursor = conn.cursor()

        # Retrieve the maximum ID from the specified table
        cursor.execute(f"SELECT MAX(id) FROM {table_name}")
        max_id = cursor.fetchone()[0]

        # If no records exist, set the ID to 1, otherwise increment by 1
        if max_id is None:
            next_id = 1
        else:
            next_id = max_id + 1

        return next_id
    except sqlite3.Error as e:
        print("Error getting next ID:", e)
        return None
    finally:
        conn.close()

def insert_data():
    try:
        # Connect to the database and create a cursor
        conn = sqlite3.connect('your_database_name.db')
        cursor = conn.cursor()

        # Prompt user for data
        name = input("Enter name: ")
        type = input("Enter type (income/expenditure/planned_exp/record): ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))
        date = input("Enter date (YYYY-MM-DD): ")

        # Generate next available ID for info table
        info_id = get_next_id("info")

        # Insert data into the tables
        cursor.execute("INSERT INTO info (id, name, type, description, trans_id) VALUES (?, ?, ?, ?, ?)",
                       (info_id, name, type, description, info_id))
        cursor.execute("INSERT INTO `transaction` (id, type, amount, date) VALUES (?, ?, ?, ?)",
                       (info_id, type, amount, date))
        cursor.execute("INSERT INTO transaction_plan (id, amount, date_start, date_end, trans_id) VALUES (?, ?, ?, ?, ?)",
                       (info_id, amount, date, date, info_id))
        cursor.execute("INSERT INTO eval_transaction (id, total, saved, date, info_id) VALUES (?, ?, ?, ?, ?)",
                       (info_id, amount, 0, date, info_id))

        # Commit the transaction
        conn.commit()
        print("Data inserted successfully!")
    except sqlite3.Error as e:
        # Rollback the transaction if an error occurs
        conn.rollback()
        print("Error inserting data:", e)
    finally:
        # Close the connection
        conn.close()

# Call the function to insert data
insert_data()

"""