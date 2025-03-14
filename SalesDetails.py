

import pandas as pd
import random
from datetime import datetime
from PostgresCon import get_connection, close_connection


conn = get_connection()
cursor = conn.cursor()

class Product:
    """get product id and prduct unit price from database """

    # 
    query = "select ProductID,saleprice from Products"  # Modify with your table
    cursor.execute(query)
    products_list = cursor.fetchall()





class SaleIDGenerator:
    """Generates unique SaleID based on date."""
    sale_counter = 1  # Shared counter for unique SaleIDs

    @classmethod
    def generate_sale_id(cls, date):
        """Generates a unique SaleID in format YYYYMMDD00<incremental_number>"""
        sale_id = f"{date}_{cls.sale_counter:03d}"
        cls.sale_counter += 1
        return sale_id
    


class Sale:
    """Represents a sale transaction with multiple sale details."""
    def __init__(self, date,max_item_per_sales_id):
        self.date = date
        self.sale_id = SaleIDGenerator.generate_sale_id(date)
        self.sale_details = self.generate_sale_details(max_item_per_sales_id)

    def generate_sale_details(self,max_item_per_sales_id):
        """Generates 2 to 4 SaleDetail records linked to the SaleID."""
        num_details = random.randint(2, max_item_per_sales_id)
        return [SaleDetail(self.sale_id, i, random.choice(Product.products_list)) for i in range(1, num_details + 1)]

    def get_sale_details_tuples(self):
        """Returns all sale details as a list of tuples (SaleID, SaleDetailID, ProductID, ProductUnitPrice)."""
        return [detail.get_detail_tuple() for detail in self.sale_details]


class SaleDetail:
    """Represents individual sale details related to a SaleID."""
    def __init__(self, sale_id, detail_number, product_tuple):
        self.sale_id = sale_id
        self.sale_detail_id = f"{sale_id}_{detail_number:03d}"
        self.product_id = product_tuple[0]  # Extracting ProductID
        self.product_price = product_tuple[1]  # Extracting ProductUnitPrice
        self.quantity = random.choice(range(1,4))
        self.subtotal= self.product_price *  self.quantity

    def get_detail_tuple(self):
        """Returns the sale detail as a tuple (SaleID, SaleDetailID, ProductID, ProductUnitPrice)."""
        return (self.sale_id, self.sale_detail_id, self.product_id,self.quantity, self.product_price,self.subtotal)

