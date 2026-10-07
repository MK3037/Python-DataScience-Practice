import mysql.connector as connector

db_config = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "mihir",
    "database": "mkj"
}

try:
    connection = connector.connect(**db_config)
    cursor = connection.cursor()
    print("Connected to database 'mkj' successfully.\n")

    # =========================================================================
    # STEP 1: CREATE THE STORED PROCEDURE
    # =========================================================================
    drop_proc_if_exists = "DROP PROCEDURE IF EXISTS GetMenuByType;"
    cursor.execute(drop_proc_if_exists)

    create_proc_query = """
    CREATE PROCEDURE GetMenuByType(IN item_type VARCHAR(50))
    BEGIN
        SELECT itemid, name, price 
        FROM menu 
        WHERE type = item_type;
    END;
    """
    cursor.execute(create_proc_query)
    print("1. Stored Procedure 'GetMenuByType' created successfully.")

    # =========================================================================
    # STEP 2: CALL THE STORED PROCEDURE
    # =========================================================================
    print("\n2. Calling Stored Procedure 'GetMenuByType' with parameter 'Veg':")
    
    # Pass procedure name and tuple of arguments
    cursor.callproc('GetMenuByType', ('Veg',))

    # Iterate through result sets returned by stored procedure
    for result_set in cursor.stored_results():
        rows = result_set.fetchall()
        print(f"Found {len(rows)} record(s):")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}")

    # =========================================================================
    # STEP 3: DROP THE STORED PROCEDURE
    # =========================================================================
    drop_proc_query = "DROP PROCEDURE IF EXISTS GetMenuByType;"
    cursor.execute(drop_proc_query)
    print("\n3. Stored Procedure 'GetMenuByType' dropped successfully.")

except connector.Error as err:
    print(f"Database Error: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("\nDatabase connection closed.")