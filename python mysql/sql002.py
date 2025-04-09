class dbconn:
    def __init__(self):
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="0000",
            database="python"
        )