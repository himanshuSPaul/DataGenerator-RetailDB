import random
from DataGenerator import DataGenerator
from DatabaseCon import PostgresDBCon
from Logger import Logger

class Supplier:
    def __init__(self):
        self.logger = Logger()
        self.db_obj = PostgresDBCon()
        self.db_conn =self.db_obj.get_connection()
        self.db_cursor = self.db_conn.cursor()
        self.datagen = DataGenerator()
        self.suppliers = self.generate_supplier_data ()


    def generate_supplier_data (self):
        self.logger.write_log("INFO", f"Generating Supplier Data ...",__file__)
        supplier_rows = []
        supplier_names = self.datagen.get_suppliers_name()
        # print("supplier_names :",supplier_names)

        for i in range(len(supplier_names)):
            sup_id = 'SUP_'+str(i).zfill(3)
            sup_name = supplier_names[i]

            sup_contact_person =  self.datagen.generate_name()
            sup_contact_number = self.datagen.generate_store_phone_number()
            sup_email = sup_contact_person.strip().replace(" ",".")+"@"+ supplier_names[i].replace(" ","").lower()+".com"
            sup_email = random.choice(['retail.sales','sales','customer.sales','keyaccounts']) +"@"+ supplier_names[i].replace(" ","").lower()+".com"

            sup_address = self.datagen.generate_address()
            sup_city ="Banglore"
            sup_state= "KARNATAKA"
            sup_zipcode = str(random.choice(range(560100,562000)))
            sup_country = "INDIA"
            sup_row = (sup_id,sup_name,sup_contact_person,sup_contact_number,sup_email,sup_address,sup_city,sup_state,sup_zipcode,sup_country)
            # print("Supplier Data :",sup_row)
            supplier_rows.append(sup_row)
        
        return supplier_rows
        

        
s = Supplier()
s.generate_supplier_data()
