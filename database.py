import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='postgres',
    password='1234',
    database='students'
)