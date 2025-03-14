from Logger import Logger
from DataGenerator import DataGenerator
import random


TABLE_NAME ="Customers"
no_of_customers = 100

class Customer:
    def __init__(self):
        self.datagen=DataGenerator()
        self.customer_list =self.generate_customer_data()

    def generate_customer_data(self):
        cust_list = []

        for i in range(no_of_customers):
            cust_id = 'CUST_'+str(i).zfill(3)
            cust_f_name = self.datagen.generate_first_name()
            cust_l_name = self.datagen.generate_last_name()
            cust_email  = f"{cust_f_name}.{cust_l_name}@email.com"
            cust_phn_no = self.datagen.generate_phone_number()
            cust_address = self.datagen.generate_address()
            cust_city = 'Bangalore'
            cust_state = 'Karnataka'
            cust_zipcode = str(random.choice(range(560100,562000)))
            cust_country = 'INDIA'
            cust_row = (cust_id,cust_f_name,cust_l_name,cust_email,cust_phn_no,cust_address,cust_city,cust_state,cust_zipcode,cust_country)
            # print(cust_row)
            cust_list.append(cust_row)
        
        return cust_list

