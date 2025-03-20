from DatabaseCon import PostgresDBCon
from Logger import Logger
from DataGenerator import DataGenerator
import random
import random
from datetime import datetime, timedelta
import pandas as pd
import configparser,argparse


last_timestamp = None
store_start_time ="07:00:00" # fixed to avoid transaction date moving to next date
TABLE_NAME1 ="sales" 
TABLE_NAME2 ="salesdetails"

def generate_transaction_timestamp(start_date="2024-06-01", start_time=store_start_time):
    global last_timestamp

    # If it's the first call, initialize with the start date and time
    if last_timestamp is None:
        last_timestamp = datetime.strptime(f"{start_date} {start_time}", "%Y-%m-%d %H:%M:%S")
    else:
        # Generate random minutes (1 to 5) and seconds (0 to 59)
        rand_minutes = random.randint(1, 1)
        rand_seconds = random.randint(0,1)
        
        # Update the timestamp
        last_timestamp += timedelta(minutes=rand_minutes, seconds=rand_seconds)
    
    return last_timestamp.strftime("%Y-%m-%d %H:%M:%S")




def get_customer_details_list():
    """Get CustomerID"""
    query = """select customerid from customers"""
    db_cursor.execute(query)
    cust_details = db_cursor.fetchall()
    return cust_details


def get_employee_and_store_details_list():
    """Get Cashier's EmployeeID and StoreID"""
    query = """SELECT StoreID,EmployeeID FROM Employees where JobTitle='Cashier' """
    db_cursor.execute(query)
    emp_store_details = db_cursor.fetchall()
    return emp_store_details

def get_product_details_list():
    """Get ProductId and ProductSellPrice"""
    query = """SELECT productid,cost FROM products """
    db_cursor.execute(query)
    prdid_prdsaleprc_details = db_cursor.fetchall()
    return prdid_prdsaleprc_details
    

# def write_sales_data(sales_data_list):
#     pass


# def write_sales_details_data(sales_detail_data_list):
#     pass


def generate_sales_and_salesdetails_data(input_sale_date,input_max_salesid,input_max_lineid_per_saleid ):
    logger.write_log("ERROR", f"Generating Sales And Sales Details Data . . .",__file__)
    sales_data =[]
    sales_detils_data = []
    transaction_ts = ''

    cust_details = get_customer_details_list()
    prod_details = get_product_details_list()
    emp_str_details = get_employee_and_store_details_list()

    input_date = input_sale_date # '2024-06-01'
    max_sales_counter =input_max_salesid #5
    max_lineid_per_saleid = input_max_lineid_per_saleid #5
    payment_method_types = ['Cash','UPI', 'Credit Card', 'Debit Card', 'Online Payment']
    
    for counter in range(1,max_sales_counter+1):
        sale_date =input_date
        sale_id_unique = f"SALE_{input_date.replace('-','')}_{counter:03d}"
        payment_method = random.choice(payment_method_types)
        total_cost = 0
        transaction_ts = str(generate_transaction_timestamp(start_date=sale_date))
        print(f"transaction_ts :{transaction_ts}")
        
        emp_str_detail =random.choice(emp_str_details)
        cust_detail = random.choice(cust_details)
        sale_counter =+ 1

        for line_id in range(random.randint(2,max_lineid_per_saleid)):
            prd_detail= random.choice(prod_details)

            sale_id =sale_id_unique
            sale_detail_id = f"{sale_id}_{line_id:03d}"
            prod_id= prd_detail[0]
            prod_cost= prd_detail[1]
            prod_quantity = random.choice(range(1,4))
            stor_id = emp_str_detail[0]
            empl_id = emp_str_detail[1]
            cust_id = cust_detail[0]
            sub_total = prod_quantity *prod_cost
            total_cost += sub_total
            # print(f"SalesDetail : ({sale_id},{sale_date},{sale_detail_id},{prod_id},{prod_quantity},{prod_cost},{sub_total},{transaction_ts})")
            sales_detils_data.append((sale_date,sale_id,sale_detail_id,prod_id,prod_quantity,prod_cost,sub_total,transaction_ts))

        # print(f"Sale :({sale_id},{sale_date},{stor_id},{empl_id},{cust_id},{total_cost},{payment_method},{transaction_ts})")
        sales_data.append((sale_date,sale_id,stor_id,empl_id,cust_id,total_cost,payment_method,transaction_ts))
    logger.write_log("ERROR", f"Generated Total Sales Record(s):{len(sales_data)} and Total SalesDetails Record(s):{len(sales_detils_data)}",__file__)

    return sales_detils_data,sales_data



def create_sales_table():
    # drop_table_if_already_exist = f"""DROP TABLE IF EXISTS {TABLE_NAME1} CASCADE;"""
    # logger.write_log("INFO", f"Dropping Table If already ExistS :{drop_table_if_already_exist}",__file__)
    # db_cursor.execute(drop_table_if_already_exist)
    # db_conn.commit()

    logger.write_log("INFO", f"Creating '{TABLE_NAME1}' Table ...",__file__)
    create_table_query = f"""
                        CREATE TABLE IF NOT EXISTS  {TABLE_NAME1} (
                        SaleDate VARCHAR(255) 
                        ,SaleID VARCHAR(255) PRIMARY KEY
                        ,StoreID VARCHAR(255) 
                        ,EmployeeID VARCHAR(255) 
                        ,CustomerID VARCHAR(255) 
                        ,TotalAmount DECIMAL(10,2) NOT NULL
                        ,PaymentMethod VARCHAR(255)
                        ,SalesTransactionTimestamp VARCHAR(255)
                        --,FOREIGN KEY (StoreID) REFERENCES Stores(StoreID)
                        --,FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
                        --,FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
                    )
                        """
    logger.write_log("INFO", f"Executing Query :{create_table_query}",__file__)
    db_cursor.execute(create_table_query)
    db_conn.commit()




def insert_data_into_sales_table(sales_detils_data):
    create_sales_table()
    # print("Data to Be Loaded :\n",sales_detils_data)
    logger.write_log("INFO", f"Insert Data Into '{TABLE_NAME1}' Table ...",__file__)
    insert_data_query = f"""INSERT INTO {TABLE_NAME1}  (SaleDate,SaleID,StoreID,EmployeeID,CustomerID,TotalAmount,PaymentMethod,SalesTransactionTimestamp)
                                                VALUES (%s,       %s,   %s,     %s,        %s,        %s,        %s,            %s)"""


    df = pd.DataFrame(sales_detils_data, columns=['SaleDate','SaleID','StoreID','EmployeeID','CustomerID','TotalAmount','PaymentMethod','SalesTransactionTimestamp'])
    data_to_insert = [tuple(row) for row in df.values]
    # print("data_to_insert :",data_to_insert)
    try:
        db_cursor.executemany(insert_data_query, data_to_insert)
        db_conn.commit()
        logger.write_log("INFO", f"Sucessfully Inserted {len(data_to_insert)} row(s) Into '{TABLE_NAME1}'")
    except Exception as e:
        logger.write_log("ERROR", f"Failed To Insert Data into '{TABLE_NAME1}' \n :{e}",__file__)






def create_salesdetail_table():
    # drop_table_if_already_exist = f"""DROP TABLE IF EXISTS {TABLE_NAME1} CASCADE;"""
    # logger.write_log("INFO", f"Dropping Table If already ExistS :{drop_table_if_already_exist}",__file__)
    # db_cursor.execute(drop_table_if_already_exist)
    # db_conn.commit()

    logger.write_log("INFO", f"Creating '{TABLE_NAME2}' Table ...",__file__)
    create_table_query = f"""
                            CREATE TABLE IF NOT EXISTS {TABLE_NAME2} (
                            SaleDate VARCHAR(255) 
                            ,SaleID VARCHAR(255) 
                            ,SaleDetailID VARCHAR(255) 
                            ,ProductID VARCHAR(255) 
                            ,Quantity INT NOT NULL
                            ,UnitPrice DECIMAL(10,2) NOT NULL
                            ,Subtotal DECIMAL(10,2) NOT NULL
                            ,SalesTransactionTimestamp VARCHAR(255) 
                            --,PRIMARY KEY (SaleDetailID,SaleID)
                            -- ,FOREIGN KEY (SaleID) REFERENCES Sales(SaleID)
                            -- ,FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
                            );
                    
                        """
    logger.write_log("INFO", f"Executing Query :{create_table_query}",__file__)
    db_cursor.execute(create_table_query)
    db_conn.commit()



def insert_data_into_salesdetails_table(sales_detils_data):
    # create_salesdetail_table()
    logger.write_log("INFO", f"Insert Data Into '{TABLE_NAME2}' Table ...",__file__)
    insert_data_query = f"""INSERT INTO {TABLE_NAME2}  (SaleDate,SaleID,SaleDetailID, ProductID, Quantity, UnitPrice, Subtotal,SalesTransactionTimestamp) 
                            VALUES                     (      %s,     %s,         %s,        %s,       %s,        %s,       %s,               %s);"""

    df = pd.DataFrame(sales_detils_data, columns=["SALEDATE", "SALEID", "SALEDETAILID" , "PRODUCTID", "QUANTITY", "UNITPRICE", "SUBTOTAL","TRANSACTION_TS"])
    data_to_insert = [tuple(row) for row in df.values]
    try:
        db_cursor.executemany(insert_data_query, data_to_insert)
        db_conn.commit()
        logger.write_log("INFO", f"Sucessfully Inserted {len(data_to_insert)} row(s) Into '{TABLE_NAME2}'")
    except Exception as e:
        logger.write_log("ERROR", f"Failed To Insert Data into '{TABLE_NAME2}' \n :{e}",__file__)







if __name__ == '__main__':
    logger = Logger()
    db_obj = PostgresDBCon()
    db_conn = db_obj.get_connection()
    db_cursor = db_conn.cursor() 

    parser = argparse.ArgumentParser(description="Employee Attendance Tracker")
    parser.add_argument("-d", "--swipe_date", type=str, required=False, help="Share The Date For Which You want to generate Employees Swipe In data")
    args = parser.parse_args()

    in_sale_date = args.swipe_date #'2024-06-09'
    in_max_salesid = 1000
    in_max_lineid_per_saleid = 5
    logger.write_log("INFO", f"Procesing Sales Data For :",__file__)
    logger.write_log("INFO", f"Input Date :{in_sale_date}",__file__)
    logger.write_log("INFO", f"Input Maximum Sales Id To Be Generated :{in_max_salesid}",__file__) 
    logger.write_log("INFO", f"Input Maximum Line Id per Sales To Be Generated :{in_max_lineid_per_saleid}",__file__) 
    sales_detils_data,sales_data = generate_sales_and_salesdetails_data(in_sale_date,in_max_salesid,in_max_lineid_per_saleid )
    insert_data_into_sales_table(sales_data)
    insert_data_into_salesdetails_table(sales_detils_data)





    


            # print("sale_date :",sale_date)
            # print("sale_id :",sale_id)
            # print("sale_detail_id :",sale_detail_id)



