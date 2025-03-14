import random
from datetime import datetime, timedelta
import configparser,argparse
from pathlib import Path
from DatabaseCon import PostgresDBCon
from Logger import Logger
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent #.parent  # Moves two levels up to the project root
print("PROJECT_ROOT :")
print("PROJECT_ROOT :",PROJECT_ROOT)

# Construct the path to the database.ini file dynamically
CONFIG_PATH = PROJECT_ROOT / "Code" / "config" / "config.ini"
INPUT_DATE_STR ='2024-06-02'
TABLE_NAME = "EMPLOYEE_TIMESHEET"

def random_timestamp(start_time, end_time):
    """Generate a random timestamp between two datetime objects."""
    time_diff = end_time - start_time
    random_seconds = random.randint(0, int(time_diff.total_seconds()))  # Random offset in seconds
    return start_time + timedelta(seconds=random_seconds)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Employee Attendance Tracker")
    parser.add_argument("-d", "--swipe_date", type=str, required=False, help="Share The Date For Which You want to generate Employees Swipe In data")
    args = parser.parse_args()
    
    config = configparser.ConfigParser()    
    config.read(CONFIG_PATH)
    emp_in_start_hr = int(config["configs"]["emp_in_start_hr"])
    emp_in_end_hr = int(config["configs"]["emp_in_end_hr"])
    emp_out_start_hr = int(config["configs"]["emp_out_start_hr"])
    emp_out_end_hr = int(config["configs"]["emp_out_end_hr"])

    db_obj = PostgresDBCon()
    db_conn = db_obj.get_connection()
    db_cursor = db_conn.cursor()

    if args.swipe_date: 
        date_str = str(args.swipe_date).replace("_","-")
    else :
        date_str =INPUT_DATE_STR

    # Entry Time is between 8:00AM 12:00PM
    entry_start = datetime.strptime(date_str, "%Y-%m-%d").replace(hour=emp_in_start_hr, minute=0, second=0)
    entry_end = datetime.strptime(date_str, "%Y-%m-%d").replace(hour=emp_in_end_hr, minute=0, second=0)

    # Exit Time is between 18:00AM 21:00PM
    exit_start = datetime.strptime(date_str, "%Y-%m-%d").replace(hour=emp_out_start_hr, minute=0, second=0)
    exit_end = datetime.strptime(date_str, "%Y-%m-%d").replace(hour=emp_out_end_hr, minute=0, second=0)
    # Generate random timestamps
    entry_time = random_timestamp(entry_start, entry_end)
    exit_time = random_timestamp(exit_start, exit_end)
    attendance_date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y%m%d")
    print("attendance_date :",attendance_date)
    
    employee_attendance=  []
    try:
        query = "SELECT StoreID,EmployeeID FROM Employees"  # Modify with your table
        print("Query :",query)
        db_cursor.execute(query)
        rows = db_cursor.fetchall()

        for row in rows:
            attendance_row =(datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y%m%d")+'_'+row[1].replace('EMP',""),
                            row[1],
                            row[0],
                            datetime.strptime(date_str, "%Y-%m-%d"),
                            random_timestamp(entry_start, entry_end),
                            random_timestamp(exit_start, exit_end),
                            )
            # print("Data To Be Inserted :",attendance_row)
            employee_attendance.append(attendance_row)
            
        # Convert to a DataFrame for better visualization
        df = pd.DataFrame(employee_attendance, columns=["AttendanceID","EmployeeID","StoreID","AttendanceDate","CheckInTime","CheckOutTime"])

        table_ddl = f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                        AttendanceID TEXT PRIMARY KEY,  
                        EmployeeID TEXT,              
                        StoreID TEXT, 
                        AttendanceDate TEXT,
                        CheckInTime TIMESTAMP,
                        CheckOutTime TIMESTAMP
                        );
                    """
        print("Query :",table_ddl)
        db_cursor.execute(table_ddl)
        db_conn.commit()

        # db_cursor.execute(f'truncate table {TABLE_NAME}')
        # db_conn.commit()

        insert_query = f"""INSERT INTO {TABLE_NAME} (AttendanceID,EmployeeID,StoreID,AttendanceDate,CheckInTime,CheckOutTime)
                            VALUES (%s, %s, %s,%s,%s,%s)"""
        data_to_insert = [tuple(row) for row in df.values]
        db_cursor.executemany(insert_query, data_to_insert)
        db_conn.commit()
        print(f"Successfully inserted {len(data_to_insert)} records into {TABLE_NAME}")

    except Exception as e:
        print("Error fetching data:", e)
    
