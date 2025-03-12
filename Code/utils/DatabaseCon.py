import psycopg2
from psycopg2 import sql
import configparser
from pathlib import Path
 

# Get the absolute path of the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent  # Moves two levels up to the project root
print("PROJECT_ROOT :",PROJECT_ROOT)

# Construct the path to the database.ini file dynamically
CONFIG_PATH = PROJECT_ROOT / "config" / "config.ini"

class PostgresDBCon:
    """Represents a sale transaction with multiple sale details."""
    def __init__(self):
        """ Create Connection to Postgreas Database"""

        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)

        self.dbname = config.get('pg_cred', 'dbname')
        self.user = config.get('pg_cred', 'user')
        self.password = config.get('pg_cred', 'password')
        self.host = config.get('pg_cred', 'host')
        self.port = config.get('pg_cred', 'port')

        self.DB_CONFIG = { "dbname": self.dbname, "user": self.user, "password": self.password,"host": self.host, "port": self.port}

    
    def get_connection(self):
        """Establishes and returns a database connection."""
        try:
            conn = psycopg2.connect(**self.DB_CONFIG)
            return conn
        except Exception as e:
            print("Error connecting to the database:", e)
            return None

    def test_connection(self,cursor):
        """Test database connection."""
        print("Testing Connection : ")
        testSQL= """ select current_user ,current_timestamp """
        cursor.execute(testSQL)
        rows = cursor.fetchall()
        user,qry_ts = rows[0]
        print(f"Logged In User: {user}")
        print(f"Logged In Time: {qry_ts}")
        if user ==self.user:
            print("[INFO] Database connection established.")
        else :
            print("Failed To Connect To Postgres Database")


    def close_connection(self,conn, cursor=None):
        """Closes the database connection and cursor safely."""
        if cursor:
            print("Closing Cursor ...")
            cursor.close()
        if conn:
            print("Closing Connection ...")
            conn.close()

if __name__ =="__main__":
    pg_db_obj = PostgresDBCon()
    pg_conn =pg_db_obj.get_connection()
    pg_cursor = pg_conn.cursor()

    if pg_conn :
        pg_db_obj.test_connection(pg_cursor)
    else :
        print("Failed TO Connect")

    pg_db_obj.close_connection(pg_conn,pg_cursor)
