import mysql.connector
from mysql.connector import Error

#połaczenie z serwerem mySQL
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

#utworzenie bazy danych
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

#łaczenie z wybrana baza danych
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection



def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except mysql.connector.Error as err:
        print("Error executing query:", err)
    finally:
        cursor.close()

def execute_list_query(connection, querry, list_of_values:list):
    cursor = connection.cursor()
    try:
        cursor.executemany(querry, list_of_values)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
