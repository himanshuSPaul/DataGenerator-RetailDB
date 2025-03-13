from Suplier import Supplier
from DatabaseCon import PostgresDBCon
from Logger import Logger
import pandas as pd
import random

TABLE_NAME ="Suppliers"


class GenerateSupplierData:
    def __init__(self):
        self.logger = Logger()
        self.db_obj = PostgresDBCon()
        self.db_conn =self.db_obj.get_connection()
        self.db_cursor = self.db_conn.cursor()
        self.supplier_obj = Supplier()
        self.supplier_list= self.supplier_obj.suppliers

        
    def create_suppliers_table(self):
        self.logger.write_log("INFO", f"Creating '{TABLE_NAME}' Table ...",__file__)
        create_table_query = f"""
                                CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                                SupplierID VARCHAR(255) PRIMARY KEY 
                                ,SupplierName VARCHAR(100) NOT NULL
                                ,SupplierContactPerson VARCHAR(100)
                                ,SupplierContactNumber VARCHAR(20)
                                ,SupplierContactEmail VARCHAR(100) 
                                ,Address  VARCHAR(255) 
                                ,City VARCHAR(255) 
                                ,State VARCHAR(255) 
                                ,ZipCode VARCHAR(255) 
                                ,Country VARCHAR(255)
                                );
                            """
        self.logger.write_log("INFO", f"Executing Query :{create_table_query}",__file__)
        self.db_cursor.execute(create_table_query)
        self.db_conn.commit()


    def insert_data_into_salary_table(self):
        self.logger.write_log("INFO", f"Insert Data Into '{TABLE_NAME}' Table ...",__file__)
        insert_data_query = f"""INSERT INTO {TABLE_NAME} 
                                (SupplierID,SupplierName,SupplierContactPerson,SupplierContactNumber,SupplierContactEmail,Address,City,State,ZipCode,Country) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        df = pd.DataFrame(self.supplier_list, columns=["SupplierID","SupplierName","SupplierContactPerson","SupplierContactNumber","SupplierContactEmail","Address","City","State","ZipCode","Country"])
        data_to_insert = [tuple(row) for row in df.values]
        try:
            self.db_cursor.executemany(insert_data_query, data_to_insert)
            self.db_conn.commit()
            self.logger.write_log("INFO", f"Sucessfully Inserted {len(data_to_insert)} row(s) Into '{TABLE_NAME}'",__file__)
        except Exception as e:
            self.logger.write_log("ERROR", f"Failed To Insert Data into '{TABLE_NAME}' \n :{e}",__file__)





sup_data =GenerateSupplierData()
sup_data.create_suppliers_table()
sup_data.insert_data_into_salary_table()