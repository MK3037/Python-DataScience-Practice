import mysql.connector as connector
from mysql.connector import errorcode
import pandas as pd

try:
    connection = connector.connect(host="127.0.0.1", port=3306, user="root", password="mihir")

    cursor=connection.cursor()

    querry1="show databases"
    cursor.execute(querry1)
    print('---DATABASES---')
    for database in cursor.fetchall():
        print(str(database).strip('(),'))

    cursor.execute('create database if not exists mkj ')
    cursor.execute('use mkj')

    print('---TABLES---')
    cursor.execute('show tables')
    for tables in cursor.fetchall():
        print(tables)

    create_table="create table if not exists menu(itemid int auto_increment, name varchar(50),type varchar(50), price int, primary key(itemid))"
    cursor.execute(create_table)
    cursor.execute('desc menu')
    for field in cursor.fetchall():
        print(field)
        
except connector.Error as err:
    print(err)