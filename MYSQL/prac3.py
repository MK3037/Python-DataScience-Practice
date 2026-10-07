import mysql.connector as connector

try:
    # 1. Establish Connection
    connection = connector.connect(
    host="127.0.0.1",
    port=3306,  # Check port in MySQL Workbench connection settings
    user="root",
    password="mihir",
    database="mkj",
)
    cursor = connection.cursor()

    # 4. Create Table 'menu'
    create_table = """
    CREATE TABLE IF NOT EXISTS menu (
        itemid INT AUTO_INCREMENT, 
        name VARCHAR(50), 
        type VARCHAR(50), 
        price INT, 
        PRIMARY KEY(itemid)
    )
    """
    cursor.execute(create_table)

    # 5. Insert Sample Records
    insert_query = """
    INSERT INTO menu (name, type, price) VALUES 
    ('Paneer Butter Masala', 'Veg', 250),
    ('Chicken Biryani', 'Non-Veg', 320)
    """
    cursor.execute("TRUNCATE TABLE menu")  # Reset table on run
    cursor.execute(insert_query)
    connection.commit()

    update_query = """
    UPDATE menu set price=300 where itemid=1"""
    cursor.execute(update_query)
    connection.commit()

    # 6. Fetch & Print Table Structure
    print("--- MENU TABLE STRUCTURE ---")
    cursor.execute("DESCRIBE menu")
    for field in cursor.fetchall():
        print(field)

    # 7. Fetch & Print Table Data
    print("\n--- MENU TABLE DATA ---")
    cursor.execute("SELECT * FROM menu")
    for row in cursor.fetchall():
        print(row)

except connector.Error as err:
    print(f"Error: {err}")

finally:
    # 8. Clean up resources
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("\nCursor and MySQL connection closed.")