import mysql.connector
from mysql.connector import Error

connection = None

cursor = None

def connect_to_database():
    global connection, cursor
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='past_data',
            user='username',
            password='database_password',
            charset='utf8mb4',
            use_unicode=True,
            autocommit=True
        )
        
        if connection.is_connected():
            cursor = connection.cursor(prepared=True)
            print("Connected to MySQL.")
            
    except Error as e:
        print(f"Connection error: {e}")
        connection = None

def fetch_column_by_ids(column_name, ids):
    """Fetch given column for a list of row IDs"""
    global connection, cursor
    results = {}
    if connection is None or not connection.is_connected():
        print("Not connected to DB.")
        return results

    try:
        
        if not column_name.isidentifier():
            raise ValueError("Invalid column name")

        query = f"SELECT id, {column_name} FROM local_model WHERE id IN ({','.join(['%s']*len(ids))})"
        cursor.execute(query, tuple(ids))

        for row in cursor.fetchall():
            results[row[0]] = row[1]

        return results

    except Error as e:
        print(f"Query error: {e}")
        return {}
    except ValueError as ve:
        print(ve)
        return {}

def write_column_by_id(column_name, value, row_id):
    """Update a specific column in a row by ID"""
    global connection, cursor
    if connection is None or not connection.is_connected():
        print("Not connected to DB.")
        return False

    try:
        if not column_name.isidentifier():
            raise ValueError("Invalid column name")

        query = f"UPDATE local_model SET {column_name} = %s WHERE id = %s"
        cursor.execute(query, (value, row_id))
        if cursor.rowcount == 0:
            print(f"No row found with id = {row_id}")
            return False
        return True

    except Error as e:
        print(f"Update error: {e}")
        return False
    except ValueError as ve:
        print(ve)
        return False

def close_connection():
    global connection, cursor
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()
        print("Connection closed.")

if __name__ == "__main__":
    
    connect_to_database()

    ids_to_read = [1, 2, 3, 42]
    column = "text"
    results = fetch_column_by_ids(column, ids_to_read)
    for i in ids_to_read:
        print(f"{column} at ID {i}: {results.get(i)}")

    # ✅ Write new data to another column
    my_input_text = "This is a test text."
    success = write_column_by_id("text_keywords", my_input_text, 42)
    if success:
        print("Row updated successfully.")

    close_connection()

