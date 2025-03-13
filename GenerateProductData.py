from Products import Product
from ProductCategories import ProductCategory
from Suplier import Supplier
from DatabaseCon import PostgresDBCon
from Logger import Logger
import pandas as pd
import random

TABLE_NAME ="Products"

class GenerateProductData:
    def __init__(self):
        self.logger = Logger()
        self.db_obj = PostgresDBCon()
        self.db_conn =self.db_obj.get_connection()
        self.db_cursor = self.db_conn.cursor()
        self.suplier = Supplier()
        self.products = Product()
        self.product_categories = ProductCategory()
        self.product_list = self.generate_products()

        # print("Cate :",self.product_categories.prod_cat)
    
    def generate_products(self):
        product_list = []
        product_id = 1
        self.logger.write_log("INFO", f"Generating Prduct Data ...",__file__)
        
        supplier_ids = [supplier_row[0] for supplier_row in self.suplier.suppliers]
        products = self.products.products
        product_categories = self.product_categories.prod_cat
        # print("products: ",products)
        # print("\n\n\n\n")
        # print("product_categories :",product_categories)
        # print("\n\n\n\n")
        # print("Suppliers :",supplier_ids)

        for category, items in products.items():
            category_id = product_categories[category]
            supplier_id = random.choice(supplier_ids)
            for item in items:
                procurement_price = random.randint(10, 50)
                sales_price = round(procurement_price * random.uniform(1.4, 1.6), 2)
                unit_quantity = "1 kg" if category not in ["Spice", "Dairy", "Beverage", "Condiment"] else "500 g"
                # print(f"PROD_{str(product_id).zfill(3)},{item},{category_id},{supplier_id},{unit_quantity},{procurement_price},{sales_price}")
                
                product_list.append((f"PROD_{str(product_id).zfill(3)}",
                                     item, 
                                     category_id,
                                     supplier_id, 
                                     procurement_price, 
                                     sales_price,
                                     unit_quantity,
                                     "Y"
                                     ))
                product_id += 1        
        return product_list
    

    def create_product_table(self):
        drop_table_if_already_exist = f"""DROP TABLE IF EXISTS {TABLE_NAME} CASCADE;"""
        self.logger.write_log("INFO", f"Dropping Table If already ExistS :{drop_table_if_already_exist}",__file__)
        self.db_cursor.execute(drop_table_if_already_exist)
        self.db_conn.commit()

        self.logger.write_log("INFO", f"Creating '{TABLE_NAME}' Table ...",__file__)
        create_table_query = f"""
                                CREATE TABLE {TABLE_NAME} (
                                ProductID VARCHAR(255) PRIMARY KEY
                                ,ProductName VARCHAR(100) NOT NULL
                                ,CategoryID VARCHAR(255) 
                                ,SupplierID VARCHAR(255) 
                                ,Price DECIMAL(10,2) NOT NULL
                                ,Cost DECIMAL(10,2) NOT NULL
                                ,StockUnitQuantity  VARCHAR(255)
                                ,IsActive BOOLEAN DEFAULT TRUE
                                -- ,FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
                                --,FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
                                );
                            """
        self.logger.write_log("INFO", f"Executing Query :{create_table_query}",__file__)
        self.db_cursor.execute(create_table_query)
        self.db_conn.commit()

    def insert_data_into_product_table(self):
        # self.create_product_table()
        self.logger.write_log("INFO", f"Insert Data Into '{TABLE_NAME}' Table ...",__file__)
        insert_data_query = f"""INSERT INTO {TABLE_NAME} 
                                (ProductID,ProductName,CategoryID,SupplierID,Price,Cost,StockUnitQuantity,IsActive) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""

        df = pd.DataFrame(self.product_list, columns=["ProductID","ProductName","CategoryID","SupplierID","Price","Cost","StockUnitQuantity","IsActive"])
        data_to_insert = [tuple(row) for row in df.values]
        try:
            self.db_cursor.executemany(insert_data_query, data_to_insert)
            self.db_conn.commit()
            self.logger.write_log("INFO", f"Sucessfully Inserted {len(data_to_insert)} row(s) Into '{TABLE_NAME}'")
        except Exception as e:
            self.logger.write_log("ERROR", f"Failed To Insert Data into '{TABLE_NAME}' \n :{e}",__file__)



s = GenerateProductData()
s.create_product_table()
s.insert_data_into_product_table()

    
