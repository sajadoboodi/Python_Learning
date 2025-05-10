import mysql.connector
from mysql.connector import Error

def fetch_text_by_id(record_id):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='past_data',
            user='root',
            password='Admin@4321',
            charset='utf8mb4',
            use_unicode=True
        )

        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT text FROM local_model WHERE id = %s"
            cursor.execute(query, (record_id,))
            result = cursor.fetchone()

            if result:
                return result[0]  # The text column value
            else:
                print(f"No record found with id = {record_id}")
                return None

    except Error as e:
        print(f"Database error: {e}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
if __name__ == "__main__":
    row_id = 42  # Example: fetch the row with id = 42
    text = fetch_text_by_id(row_id)
    if text:
        print("Text:", text)
