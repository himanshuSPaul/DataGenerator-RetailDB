from Customer import Customer
from DatabaseCon import PostgresDBCon
from Logger import Logger
import pandas as pd


TABLE_NAME ="Customers"

class GenerateCustomerData:
    def __init__(self):
        self.customer_list= Customer().generate_customer_data()
        self.logger = Logger()
        self.db_obj = PostgresDBCon()
        self.db_conn =self.db_obj.get_connection()
        self.db_cursor = self.db_conn.cursor()
    
    
    def create_customer_table(self):
        drop_table_if_already_exist = f"""DROP TABLE IF EXISTS {TABLE_NAME} CASCADE;"""
        self.logger.write_log("INFO", f"Dropping Table If already ExistS :{drop_table_if_already_exist}",__file__)
        self.db_cursor.execute(drop_table_if_already_exist)
        self.db_conn.commit()

        self.logger.write_log("INFO", f"Creating '{TABLE_NAME}' Table ...",__file__)
        create_table_query = f"""
                            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                            CustomerID VARCHAR(255) PRIMARY KEY
                            ,FirstName VARCHAR(50) NOT NULL
                            ,LastName VARCHAR(50) NOT NULL
                            ,Email VARCHAR(100) UNIQUE
                            ,PhoneNumber VARCHAR(255)
                            ,Address VARCHAR(255)
                            ,City VARCHAR(255)
                            ,State VARCHAR(255)
                            ,ZipCode VARCHAR(255)
                            ,Country VARCHAR(255)
                            );
                            """
        self.logger.write_log("INFO", f"Executing Query :{create_table_query}",__file__)
        self.db_cursor.execute(create_table_query)
        self.db_conn.commit()

    def insert_data_into_customer_table(self):
        # self.create_product_table()
        self.logger.write_log("INFO", f"Insert Data Into '{TABLE_NAME}' Table ...",__file__)
        insert_data_query = f"""INSERT INTO {TABLE_NAME} (CustomerID,FirstName,LastName,Email,PhoneNumber,Address,City,State,ZipCode,Country)
                                VALUES  (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        df = pd.DataFrame(self.customer_list, columns=["CustomerID","FirstName","LastName","Email","PhoneNumber","Address","City","State","ZipCode","Country"])
        data_to_insert = [tuple(row) for row in df.values]
        try:
            self.db_cursor.executemany(insert_data_query, data_to_insert)
            self.db_conn.commit()
            self.logger.write_log("INFO", f"Sucessfully Inserted {len(data_to_insert)} row(s) Into '{TABLE_NAME}'")
        except Exception as e:
            self.logger.write_log("ERROR", f"Failed To Insert Data into '{TABLE_NAME}' \n :{e}",__file__)


x =GenerateCustomerData()
x.create_customer_table()
x.insert_data_into_customer_table()