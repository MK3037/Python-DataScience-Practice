import mysql.connector as connector

db_config = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "mihir",  # Set to your password
    "database": "mkj"
}

try:
    connection = connector.connect(**db_config)
    print("Connected to database 'mkj' successfully.\n")

    # =========================================================================
    # TASK 1: Retrieve all existing table names in 'mkj'
    # =========================================================================
    print("--- TASK 1: Existing Tables in 'mkj' ---")
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    
    for table in cursor.fetchall():
        print(table[0])  # Prints table name
    cursor.close()

    # =========================================================================
    # TASK 2: Standard Cursor vs. Buffered Cursor Test
    # =========================================================================
    print("\n--- TASK 2: Standard Cursor vs. Buffered Cursor ---")
    
    # 1. Standard Cursor Test
    print("\n1. Testing Standard Cursor with consecutive queries:")
    standard_cursor = connection.cursor()
    try:
        standard_cursor.execute("SELECT * FROM menu")
        # Second query on unbuffered cursor triggers the error
        standard_cursor.execute("DESCRIBE menu")
    except connector.Error as err:
        print(f"Standard Cursor Error: {err}")
    
    # IMPORTANT FIX: Consume remaining results so standard_cursor can close cleanly
    try:
        standard_cursor.fetchall()
    except connector.Error:
        pass
    standard_cursor.close()

    # 2. Buffered Cursor Test
    print("\n2. Testing Buffered Cursor with consecutive queries:")
    buffered_cursor = connection.cursor(buffered=True)
    try:
        buffered_cursor.execute("SELECT * FROM menu")
        print("Successfully executed 'SELECT * FROM menu'")
        
        buffered_cursor.execute("DESCRIBE menu")
        print("Successfully executed 'DESCRIBE menu' without fetching previous results first!")
        
        fields = buffered_cursor.fetchall()
        print(f"Fetched {len(fields)} field descriptions for table 'menu'.")
    except connector.Error as err:
        print(f"Buffered Cursor Error: {err}")
    finally:
        buffered_cursor.close()

    # =========================================================================
    # TASK 3: Dictionary Cursor
    # =========================================================================
    print("\n--- TASK 3: Dictionary Cursor ---")
    dict_cursor = connection.cursor(dictionary=True)
    dict_cursor.execute("SHOW TABLES")
    
    for row in dict_cursor.fetchall():
        table_name = list(row.values())[0]
        formatted_dict = {"mkj": table_name}
        print(formatted_dict)
        
    dict_cursor.close()

except connector.Error as err:
    print(f"Database Error: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("\nDatabase connection closed.")