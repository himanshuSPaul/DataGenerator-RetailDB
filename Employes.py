import pandas as pd
import psycopg2
from DataGenerator import *
from Stores import Stores

class Employees:
    def __init__(self):
        self.employee_counter = 1
        self.store_vacancies = Stores().store_job_vacancies
        self.total_employees = sum(sum(jobs.values()) for jobs in self.store_vacancies.values())
        self.employee_ids = [f"EMP{str(i).zfill(3)}" for i in range(1, self.total_employees + 1)]
        self.datagen = DataGenerator()
        # self.employee_list = self.generate_employee_data ()

    def generate_employee_data(self):
        employee_list =[]
        for store_id, vacencies in self.store_vacancies.items():
            for role,position in vacencies.items():
                for _ in range(position):
                    empid = f"EMP_{self.employee_counter:03d}"
                    first_name = self.datagen.generate_first_name()
                    last_name = self.datagen.generate_last_name()
                    email = f'{first_name}.{last_name}@email.com'
                    phone_number = self.datagen.generate_phone_number()
                    hire_date = self.datagen.generate_hire_date()
                    job_title = role
                    storeid = store_id
                    employee_list.append((empid,first_name,last_name,email,phone_number,hire_date,job_title,storeid))
                    self.employee_counter += 1
        return employee_list
        
    
#     def generate_employee_data(self):
#         emp_iterator = iter(self.employee_ids)
#         employee_job_store_mapping = []  # List to store (Employee ID, Job Role, Store)
#         for store, job_roles in self.store_vacancies.items():
#             for job_title, count in job_roles.items():
#                 for _ in range(count):
#                     employee_id =next(emp_iterator)
#                     first_name = self.datagen.generate_first_name()
#                     last_name = self.datagen.generate_last_name()
#                     email = f'{first_name}.{last_name}@email.com'
#                     phone_number = self.datagen.generate_phone_number()
#                     hire_date = self.datagen.generate_hire_date()
#                     job_title = self.datagen.generate_job_title()
#                     store_id = self.datagen.generate_store_id()
#                     employee_job_store_mapping.append((employee_id,first_name,last_name,email,phone_number,hire_date,job_title,store))
#         return employee_job_store_mapping
    




# ss = Employees()
# print(ss.generate_employee_data())



# x =DataGenerator()
# # Define the store-wise job roles and vacancies
# store_job_vacancies = {
#     'STORE_101': {"Store Manager": 1, "Cashier": 2, "Stock Associate": 2, "Sales Associate": 2, "House Keeping": 2},
#     'STORE_102': {"Store Manager": 1, "Cashier": 3, "Stock Associate": 3, "Sales Associate": 4, "House Keeping": 2},
#     'STORE_103': {"Store Manager": 1, "Cashier": 2, "Stock Associate": 2, "Sales Associate": 3, "House Keeping": 2},
#     'STORE_104': {"Store Manager": 1, "Cashier": 2, "Stock Associate": 4, "Sales Associate": 4, "House Keeping": 2},
#     'STORE_105': {"Store Manager": 1, "Cashier": 3, "Stock Associate": 6, "Sales Associate": 6, "House Keeping": 1}
# }

# # Generate Employee IDs based on total vacancies
# # total_employees = sum(sum(jobs.values()) for jobs in store_job_vacancies.values())
# # employee_ids = [f"EMP{str(i).zfill(3)}" for i in range(1, total_employees + 1)]

# # Assign Employee IDs to job vacancies in each store
# # emp_iterator = iter(employee_ids)
# # employee_job_store_mapping = []  # List to store (Employee ID, Job Role, Store)

# """
# emp_id =  x.generate_unique_employee_id()  #x.generate_employee_id()
# first_name = x.generate_first_name()
# last_name = x.generate_last_name()
# email = f'{first_name}.{last_name}@email.com'
# phone_number = x.generate_phone_number()
# hire_date = x.generate_hire_date()
# job_title = x.generate_job_title()
# store_id = x.generate_store_id()


# """


# for store, job_roles in store_job_vacancies.items():
#     for role, count in job_roles.items():
#         for _ in range(count):
#             first_name = x.generate_first_name()
#             last_name = x.generate_last_name()
#             email = f'{first_name}.{last_name}@email.com'
#             phone_number = x.generate_phone_number()
#             hire_date = x.generate_hire_date()
#             job_title = x.generate_job_title()
#             store_id = x.generate_store_id()
#             employee_job_store_mapping.append((next(emp_iterator),
#                                                first_name,
#                                                last_name,
#                                                email,
#                                                phone_number,
#                                                hire_date,
#                                                role, 
#                                                store))

# # Convert to a DataFrame for better visualization
# df = pd.DataFrame(employee_job_store_mapping, columns=["EmployeeID","FirstName","LastName","Email","PhoneNumber","HireDate","JobTitle", "StoreID"])


# # "dbname=postgres user=postgres password=postgres host=localhost"
# # Database configuration (Modify as per your PostgreSQL setup)
# DB_CONFIG = {
#     "dbname": "postgres",
#     "user": "postgres",
#     "password": "postgres",
#     "host": "localhost",  # Change if using a remote server
#     "port": "5432"  # Default PostgreSQL port
# }

# # Define the table schema (Make sure this table exists in your PostgreSQL database)
# TABLE_NAME = "Employees"

# # Establish a connection to PostgreSQL and insert the data
# try:
#     # Connect to PostgreSQL
#     conn = psycopg2.connect(**DB_CONFIG)
#     cursor = conn.cursor()

#     # Create table if it doesn't exist
#     create_table_query = f"""
#     CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
#     EmployeeID text ,
#     FirstName TEXT NOT NULL,
#     LastName TEXT NOT NULL,
#     Email TEXT UNIQUE,
#     PhoneNumber TEXT,
#     HireDate DATE NOT NULL,
#     JobTitle TEXT,
#     StoreID TEXT
#     );
#     """
#     cursor.execute(create_table_query)
#     conn.commit()

#     cursor.execute(f'truncate table {TABLE_NAME}')
#     conn.commit()




#     # Insert data into the table
#     insert_query = f"""INSERT INTO {TABLE_NAME} (EmployeeID,FirstName,LastName,Email,PhoneNumber,HireDate,JobTitle, StoreID)
#       VALUES (%s, %s, %s,%s,%s,%s,%s,%s)"""
#     data_to_insert = [tuple(row) for row in df.values]

#     cursor.executemany(insert_query, data_to_insert)
#     conn.commit()

#     print(f"Successfully inserted {len(data_to_insert)} records into {TABLE_NAME}")

# except Exception as e:
#     print("Error inserting data:", e)

# finally:
#     # Close the connection properly
#     if cursor:
#         cursor.close()
#     if conn:
#         conn.close()

# # # Display the dataset
# # import ace_tools as tools
# # tools.display_dataframe_to_user(name="Generated Employee IDs for Store Vacancies", dataframe=df)
