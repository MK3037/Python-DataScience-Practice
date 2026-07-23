import mysql.connector

try:
    # Establish the connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mihir",
        database="javaprac"
    )

    # Create a cursor object to execute queries
    cursor = conn.cursor()
    
    # Execute the query
    cursor.execute("SELECT * FROM diet")
    
    # Fetch all rows
    rows = cursor.fetchall()
    
    for row in rows:
        print(f"{row[0]}\t{row[1]}\t{row[2]}")      #or print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")