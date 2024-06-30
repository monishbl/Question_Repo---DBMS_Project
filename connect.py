import mysql.connector
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="<Your_Username>",
        passwd="<Your_Password>",
        database="<Your_Database_Name>",
        auth_plugin='mysql_native_password'
    )