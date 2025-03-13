

from DataGenerator import *
import pandas as pd


TABLE_NAME = "Suppliers"

if __name__ == '__main__':
    x =DataGenerator()
    conn = get_connection()
    cursor = conn.cursor()
    supplier_rows = []
    supplier_names = x.get_suppliers_name()

    for i in range(len(supplier_names)):
        sup_id = 'SUP_'+str(i).zfill(3)
        sup_name = supplier_names[i]

        sup_contact_person =  x.generate_name()
        sup_contact_number = x.generate_store_phone_number()
        sup_email = sup_contact_person.strip().replace(" ",".")+"@"+ supplier_names[i].replace(" ","").lower()+".com"
        sup_email = random.choice(['retail.sales','sales','customer.sales','keyaccounts']) +"@"+ supplier_names[i].replace(" ","").lower()+".com"

        sup_address = x.generate_address()
        sup_city ="Banglore"
        sup_state= "KARNATAKA"
        sup_zipcode = str(random.choice(range(560100,562000)))
        sup_country = "INDIA"
        sup_row = (sup_id,sup_name,sup_contact_person,sup_contact_number,sup_email,sup_address,sup_city,sup_state,sup_zipcode,sup_country)
        print("Supplier Data :",sup_row)
        supplier_rows.append(sup_row)