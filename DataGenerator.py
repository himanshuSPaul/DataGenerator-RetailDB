import random
from datetime import datetime, timedelta
# from faker import Faker
from collections import deque
from pathlib import Path


# Get the absolute path of the project root
PROJECT_ROOT = Path(__file__).resolve().parent #.parent  # Moves two levels up to the project root
# Construct the path to the database.ini file dynamically
ADDRESS_LIST_FILE = PROJECT_ROOT / "Code" / "config" / "address.txt"
FIRST_NAME_LIST_FILE = PROJECT_ROOT / "Code" / "config" / "first_name.txt"
MIDDLE_NAME_LIST_FILE = PROJECT_ROOT / "Code" / "config" / "middle_name.txt"
LAST_NAME_LIST_FILE = PROJECT_ROOT / "Code" / "config" / "last_name.txt"
NAMES_LIST_FILE = PROJECT_ROOT / "Code" / "config" / "names.txt"
SUPPLIER_NAME_LIST_FILE = PROJECT_ROOT / "Code" / "config" / "supplier_name.txt"


class DataGenerator:
    def __init__(self):
        """Initialize the Employee class and read names from the text file."""
        self.dob_start_date = datetime(1980, 1, 1)
        self.dob_end_date = datetime(2005, 12, 31)
        self.store_start_date = datetime(2024, 2, 1)
        self.store_inaguration_date = datetime(2024, 6, 1)

        self.employee_id = ["EMP_"+str(e) for e in range(100,150)]
        self.employee_queue = deque()
        # self.employee_queue = deque(random.sample(self.employee_id, len(self.employee_id)))
        
        self.store_id = ["STORE_"+str(s) for s in range(100,110)]  
        # random.shuffle(self.employee_id)

        self.job_roles_with_limits = {"Store Manager": 10,"Cashier": 10,"Stock Associate": 20,"Sales Associate": 20,"House Keeping": 10 }
        self.no_of_employee_in_store = {'STORE100':7,'STORE101':7,'STORE102':7,'STORE103':7,'STORE104':7,'STORE105':7,'STORE106':7,'STORE107':7,'STORE108':7,'STORE109':7}
        store_vacancy = { 

                        } 

        self.pick_counts = {role: 0 for role in self.job_roles_with_limits}
        
        self.store_job_role =["Cashier", "Store Manager", "Stock Associate", "Sales Associate", "Assistant Manager"]
        
        
        
        self.person_name =[]
        with open(NAMES_LIST_FILE, "r") as name_file:
            self.names = [line.split(",") for line in name_file.readlines()][0]

        self.address =[]
        with open(ADDRESS_LIST_FILE, "r") as address_file:
            self.address = address_file.readlines()

        self.first_name =[]
        with open(FIRST_NAME_LIST_FILE, "r") as first_name_file:
            self.first_name = [f.strip() for f in first_name_file.readlines()[0].split(",")]

        self.middle_name =[]
        with open(MIDDLE_NAME_LIST_FILE, "r") as middle_name_file:
            self.middle_name = [f.strip() for f in middle_name_file.readlines()[0].split(",")]

        self.last_name =[]
        with open(LAST_NAME_LIST_FILE, "r") as last_name_file:
            self.last_name = [f.strip() for f in last_name_file.readlines()[0].split(",")]

        self.suuplier =[]
        with open(SUPPLIER_NAME_LIST_FILE, "r") as supplier_name_file:
            self.supplier_name = [f.strip() for f in supplier_name_file.readlines()]



    def get_suppliers_name(self):
        return self.supplier_name


    def reset(self):
        """Resets the selection counts for all job roles"""
        self.pick_counts = {role: 0 for role in self.job_roles_with_limits}
        self.employee_queue = deque(random.sample(self.employee_queue , len(self.employee_queue )))



    def generate_name(self):
        """Generate a unique EmployeeID in the format EMP_XXX"""
        return random.choice(self.names)
    
    def generate_address(self):
        """Generate a unique EmployeeID in the format EMP_XXX"""
        return random.choice(self.address).strip("\n")
    
    def generate_first_name(self):
        """Generate a unique EmployeeID in the format first_name_file"""
        return random.choice(self.first_name)
    
    def generate_middle_name(self):
        """Generate a unique middle_name in the format first_name_file"""
        return random.choice(self.middle_name).strip("\n")
    
    def generate_last_name(self):
        """Generate a unique middle_name in the format first_name_file"""
        return random.choice(self.last_name).strip("\n")
    
    def generate_job_title(self):
        available_roles = [role for role, max_limit in self.job_roles_with_limits.items() if self.pick_counts[role] < max_limit]
        if not available_roles:
            raise ValueError("All job roles have been picked the maximum number of times!")
        chosen_role = random.choice(available_roles)
        self.pick_counts[chosen_role] += 1  # Increment the pick count for the role
        return chosen_role

        # return random.choice(self.store_job_role).strip("\n")
    
    def generate_phone_number(self):
        return '+91-'+str(random.randrange(6000000000, 9999999999))

    def generate_store_phone_number(self):
        return '(+91)'+str(random.randrange(000,111))+str(random.randrange(333333,888888))



    def generate_dob(self):
        """Generate a random date between two dates."""
        delta = self.dob_end_date - self.dob_start_date
        random_days = random.randint(2, delta.days)
        return (self.dob_start_date + timedelta(days=random_days)).date()

    def generate_hire_date(self):
        """Generate a random date between two dates."""
        delta = self.store_inaguration_date - self.store_start_date
        random_days = random.randint(2, delta.days)
        return (self.store_start_date + timedelta(days=random_days)).date()
    
    # def generate_employee_id(self):
    #     if not self.employee_queue:
    #         raise ValueError("No more unique strings available!")
    #     return self.employee_queue.popleft()

    #     return random.choice(self.employee_id).pop()

    def reshulffe_employee_deque(self):
        """Reshuffles and refills the queue when exhausted."""
        shuffled = random.sample(self.employee_id, len(self.employee_id))
        self.employee_queue.extend(shuffled)

    def generate_unique_employee_id(self):
        """Returns a unique string each time, without repetition"""
        # if not self.employee_queue:
        self.reshulffe_employee_deque()
            # raise ValueError("xxxxxxxxx   No more unique strings available!")
        return self.employee_queue.popleft()
        # return random.choice(self.employee_id).pop()
    
    def generate_store_id(self):
        return random.choice(self.store_id)
    

    
    
x =DataGenerator()
# x.reset()    


# x =DataGenerator()
# print("Address :",x.generate_address())
# print("First Name :",x.generate_first_name())
# print("Middle Name :",x.generate_middle_name())
# print("Last Name :",x.generate_last_name())
# print(f"Full Name : {x.generate_last_name()} {x.generate_middle_name()} {x.generate_last_name()}")
# print("JOb Role :",x.generate_job_title())
# print("JOb Date OF Birthday :",x.generate_dob())
# print("Employee id :",x.generate_employee_id())









# def generate_address():

# # fake = Faker()

# # def generate_employee_id():
# #     """Generate a unique EmployeeID in the format EMP_XXX"""
# #     return f"EMP_{random.randint(100, 999)}"

# # def generate_store_id(n):
# #     start = 100
# #     """Generate a unique StoreID in the format STORE_XXX"""
# #     return f"STORE_{random.randint(start, start+n)}"

# # def generate_product_id():
# #     """Generate a unique StoreID in the format PROD_XXX"""
# #     return f"PROD_{random.randint(100, 1)}"

# # def generate_phone_number():
# #     """Generate a unique StoreID in the format PROD_XXX"""
# #     return f"PROD_{random.randint(100, 1)}"

# # def generate_store_id():
# #     """Generate a unique StoreID in the format Store_XX"""
# #     return f"Store_{random.randint(10, 99)}"


# # def generate_store_id():
# #     """Generate a unique StoreID in the format Store_XX"""
# #     return f"Store_{random.randint(10, 99)}"


# # def generate_store_id():
# #     """Generate a unique StoreID in the format Store_XX"""
# #     return f"Store_{random.randint(10, 99)}"


# print(generate_store_id(2))
# print(generate_store_id(2))
# print(generate_store_id(2))
# print(generate_store_id(2))
# print(generate_store_id(2))
# print(generate_store_id(2))
# print(generate_store_id(2))











# def generate_hire_date(start_date="2024-06-01", end_date=None):
#     """Generate a random hire date after 2024-06-01"""
#     start_date = datetime.strptime(start_date, "%Y-%m-%d")
#     end_date = datetime.strptime(end_date, "%Y-%m-%d") if end_date else datetime.today()
#     return (start_date + timedelta(days=random.randint(0, (end_date - start_date).days))).strftime('%Y-%m-%d')

# # def generate_employee():
# #     """Generate a realistic employee record"""
# #     return {
# #         "EmployeeID": generate_employee_id(),
# #         "FirstName": fake.first_name(),
# #         "LastName": fake.last_name(),
# #         "Email": fake.email(),
# #         "PhoneNumber": fake.phone_number(),
# #         "HireDate": generate_hire_date(),
# #         "JobTitle": random.choice(["Cashier", "Store Manager", "Stock Associate", "Sales Associate", "Assistant Manager"]),
# #         "StoreID": generate_store_id()
# #     }
