from Employes import Employees
from DatabaseCon import PostgresDBCon
from Logger import Logger
import pandas as pd
import random

TABLE_NAME ="Employees"


class GenerateEmployeesData:
    def __init__(self):
        self.logger = Logger()
        self.db_obj = PostgresDBCon()
        self.db_conn =self.db_obj.get_connection()
        self.db_cursor = self.db_conn.cursor()
        self.employees_obj = Employees()
        self.employee_list= self.employees_obj.generate_employee_data()

        
    def create_suppliers_table(self):
        self.logger.write_log("INFO", f"Creating '{TABLE_NAME}' Table ...",__file__)
        create_table_query = f"""
                                CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                                EmployeeID text ,
                                FirstName TEXT NOT NULL,
                                LastName TEXT NOT NULL,
                                Email TEXT UNIQUE,
                                PhoneNumber TEXT,
                                HireDate DATE NOT NULL,
                                JobTitle TEXT,
                                StoreID TEXT
                                );
                            """
        self.logger.write_log("INFO", f"Executing Query :{create_table_query}",__file__)
        self.db_cursor.execute(create_table_query)
        self.db_conn.commit()


    def insert_data_into_salary_table(self):
        self.logger.write_log("INFO", f"Insert Data Into '{TABLE_NAME}' Table ...",__file__)
        insert_data_query = f"""INSERT INTO {TABLE_NAME} 
                                (EmployeeID,FirstName,LastName,Email,PhoneNumber,HireDate,JobTitle, StoreID) 
                                VALUES (%s, %s, %s,%s,%s,%s,%s,%s);"""
        df = pd.DataFrame(self.employee_list, columns=["EmployeeID","FirstName","LastName","Email","PhoneNumber","HireDate","JobTitle", "StoreID"])
        data_to_insert = [tuple(row) for row in df.values]
        try:
            self.db_cursor.executemany(insert_data_query, data_to_insert)
            self.db_conn.commit()
            self.logger.write_log("INFO", f"Sucessfully Inserted {len(data_to_insert)} row(s) Into '{TABLE_NAME}'",__file__)
        except Exception as e:
            self.logger.write_log("ERROR", f"Failed To Insert Data into '{TABLE_NAME}' \n :{e}",__file__)




emp = GenerateEmployeesData()
emp.create_suppliers_table()
emp.insert_data_into_salary_table()