from DatabaseCon import PostgresDBCon
from Logger import Logger
from DataGenerator import DataGenerator
class Stores:
    def __init__(self):
        self.logger = Logger()
        self.db_obj = PostgresDBCon()
        self.db_conn =self.db_obj.get_connection()
        self.db_cursor = self.db_conn.cursor()
        self.datagen =DataGenerator()
        self.store_job_vacancies = {
                    'STORE_101': {"Store Manager": 1, "Cashier": 2, "Stock Associate": 2, "Sales Associate": 2, "House Keeping": 2},
                    'STORE_102': {"Store Manager": 1, "Cashier": 3, "Stock Associate": 3, "Sales Associate": 4, "House Keeping": 2},
                    'STORE_103': {"Store Manager": 1, "Cashier": 2, "Stock Associate": 2, "Sales Associate": 3, "House Keeping": 2},
                    'STORE_104': {"Store Manager": 1, "Cashier": 2, "Stock Associate": 4, "Sales Associate": 4, "House Keeping": 2},
                    'STORE_105': {"Store Manager": 1, "Cashier": 3, "Stock Associate": 6, "Sales Associate": 6, "House Keeping": 1}
                    }
        
    def get_stores_data(self):
        gwt_storeid_str_maneger = """SELECT StoreID,EmployeeID FROM Employees where JobTitle='Store Manager' """
        self.db_cursor.execute(gwt_storeid_str_maneger)
        rows = self.db_cursor.fetchall()
        stores_data= [(row[0],'YourChoiceMart',self.datagen.generate_address(),self.datagen.generate_store_phone_number(),row[1])  for row in rows]
        return  stores_data
        




        # print("store_id :",store_id," role: ",role," position :",position)
