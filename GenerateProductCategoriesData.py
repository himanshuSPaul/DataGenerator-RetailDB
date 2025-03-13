from Products import Product
from ProductCategories import ProductCategory
from DatabaseCon import PostgresDBCon
from Logger import Logger
import pandas as pd


"""
CREATE OR REPLACE TABLE  RETAILDB_DEV.RAW_PRODUCT.Categories (
CategoryID VARCHAR(255) PRIMARY KEY 
,CategoryName VARCHAR(100) NOT NULL
,Description TEXT
);
"""

TABLE_NAME = "Categories3"


class GenerateProductCategoriesData:
    def __init__(self):
        self.logger = Logger()
        self.db_obj = PostgresDBCon()
        self.db_conn =self.db_obj.get_connection()
        self.db_cursor = self.db_conn.cursor()
        self.product_categories = ProductCategory()
        # print("Cate :",self.product_categories.prod_cat)
        self.prd_cat_list = [(cat_name , cat_id) for cat_name , cat_id in self.product_categories.prod_cat.items()]
    
    def create_prodcut_categories_table(self):
        self.logger.write_log("INFO", f"Creating '{TABLE_NAME}' Table ...",__file__)

        create_table_query = f"""
                            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                            CategoryID VARCHAR(255) PRIMARY KEY ,
                            CategoryName VARCHAR(100) NOT NULL
                            );
                            """
        self.logger.write_log("INFO", f"Executing Query :{create_table_query}",__file__)
        self.db_cursor.execute(create_table_query)
        self.db_conn.commit()

    def insert_into_product_category_table(self):
        self.logger.write_log("INFO", f"Insert Data Into '{TABLE_NAME}' Table ...",__file__)
        insert_data_query = f"""INSERT INTO {TABLE_NAME} (CategoryID,CategoryName) VALUES (%s, %s)"""
        df = pd.DataFrame(self.prd_cat_list, columns=["CategoryID","CategoryName"])
        data_to_insert = [tuple(row) for row in df.values]
        try:
            self.db_cursor.executemany(insert_data_query, data_to_insert)
            self.db_conn.commit()
            self.logger.write_log("INFO", f"Sucessfully Inserted {len(data_to_insert)} row(s) Into '{TABLE_NAME}'")
        except Exception as e:
            self.logger.write_log("ERROR", f"Failed To Insert Data into '{TABLE_NAME}' \n :{e}",__file__)




x =GenerateProductCategoriesData()
x.create_prodcut_categories_table()
x.insert_into_product_category_table()
