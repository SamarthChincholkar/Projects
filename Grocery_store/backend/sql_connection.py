import mysql.connector  # type: ignore

__cnx = None  # Global variable for single connection

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='Samarth@2001',
                                         host='127.0.0.1',
                                         database='grocery_store')
    return __cnx