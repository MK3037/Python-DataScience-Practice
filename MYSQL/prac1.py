import mysql.connector as connector
from mysql.connector import errorcode

try:
    connection = connector.connect(
    host="127.0.0.1",
    port=3306,  # Check port in MySQL Workbench connection settings
    user="root",
    password="mihir",
    database="mkj",
)
except connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("connection user or password are incorrect")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("database does not exist")
    else:
        print(err)