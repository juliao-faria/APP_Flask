import mysql.connector

database = mysql.connector.connect(
    host='Juliao.mysql.pythonanywhere-services.com',
    user='Juliao',
    password='Aquí usé la passeword con la que cree la base de dato en PythonAnywere',
    database='Juliao$default'
)