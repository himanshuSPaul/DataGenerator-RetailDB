from Stores import Stores
from DatabaseCon import PostgresDBCon
from Logger import Logger
import pandas as pd
# from DataGenerator import DataGenerator
# import random


TABLE_NAME ="Stores"

class GenerateStoresData:
    def __init__(self):
        self.logger = Logger()
        self.db_obj = PostgresDBCon()
        self.db_conn =self.db_obj.get_connection()
        self.db_cursor = self.db_conn.cursor()
        self.stroes_list = Stores().get_stores_data()
        # self.datagen = DataGenerator()

    def create_store_table(self):
        drop_table_if_already_exist = f"""DROP TABLE IF EXISTS {TABLE_NAME} CASCADE;"""
        self.logger.write_log("INFO", f"Dropping Table If already ExistS :{drop_table_if_already_exist}",__file__)
        self.db_cursor.execute(drop_table_if_already_exist)
        self.db_conn.commit()

        self.logger.write_log("INFO", f"Creating '{TABLE_NAME}' Table ...",__file__)
        create_table_query = f"""
                            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                            StoreID VARCHAR(255) PRIMARY KEY 
                            ,StoreName VARCHAR(100) NOT NULL
                            ,Location VARCHAR(255) NOT NULL
                            ,ContactNumber VARCHAR(20)
                            ,ManagerID VARCHAR(255)
                            );
                            """
        self.logger.write_log("INFO", f"Executing Query :{create_table_query}",__file__)
        self.db_cursor.execute(create_table_query)
        self.db_conn.commit()

    def insert_data_into_store_table(self):
        # self.create_product_table()
        self.logger.write_log("INFO", f"Insert Data Into '{TABLE_NAME}' Table ...",__file__)
        insert_data_query = f"""INSERT INTO {TABLE_NAME} (StoreID,StoreName,Location,ContactNumber,ManagerID)
                                VALUES (%s, %s, %s,%s,%s)"""

        df = pd.DataFrame(self.stroes_list, columns=["StoreID","StoreName","Location","ContactNumber","ManagerID"])
        data_to_insert = [tuple(row) for row in df.values]
        try:
            self.db_cursor.executemany(insert_data_query, data_to_insert)
            self.db_conn.commit()
            self.logger.write_log("INFO", f"Sucessfully Inserted {len(data_to_insert)} row(s) Into '{TABLE_NAME}'")
        except Exception as e:
            self.logger.write_log("ERROR", f"Failed To Insert Data into '{TABLE_NAME}' \n :{e}",__file__)



x =GenerateStoresData()
x.create_store_table()
x.insert_data_into_store_table()