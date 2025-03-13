
class Product:
    def __init__(self):
        self.products = {
                "Cereal": ["Basmati Rice", "Wheat Flour", "Maize", "Barley", "Millet", "Oats", "Cornflakes", "Quinoa", "Ragi", "Sorghum", "Foxtail Millet", "Brown Rice", "Amaranth", "Buckwheat", "Wild Rice", "Pearl Millet", "Teff", "Farro", "Freekeh", "Triticale", "Spelt", "Kamut", "Bran", "Semolina", "Broken Wheat", "Whole Wheat", "Rice Bran", "Rice Flakes", "Puffed Rice", "Barley Flakes"],
                "Pulse": ["Toor Dal", "Masoor Dal", "Chana Dal", "Urad Dal", "Moong Dal", "Rajma", "Kabuli Chana", "Black Eyed Peas", "Masoor Whole", "Moth Beans", "Whole Moong", "Black Gram", "Bengal Gram", "Green Peas", "Red Kidney Beans", "Split Peas", "Pigeon Peas", "Horse Gram", "Chickpeas", "Lobia", "Green Gram", "Black Chickpeas", "White Peas", "Yellow Moong Dal", "Dried Lentils", "Whole Black Urad", "Split Urad Dal", "Brown Lentils", "Sprouted Moong", "Masoor Malka Dal"],
                "Spice": ["Turmeric", "Red Chili Powder", "Coriander Powder", "Cumin Seeds", "Black Pepper", "Cardamom", "Cloves", "Cinnamon", "Nutmeg", "Star Anise", "Bay Leaves", "Asafoetida", "Mace", "Fennel Seeds", "Mustard Seeds", "Fenugreek Seeds", "Saffron", "Dry Ginger", "Black Salt", "White Pepper", "Kasuri Methi", "Tamarind", "Dried Mint", "Pomegranate Seeds", "Carom Seeds", "Celery Seeds", "Nigella Seeds", "Black Cardamom", "Dry Mango Powder", "Allspice"],
                "Fruit": ["Mango", "Banana", "Apple", "Orange", "Pineapple", "Grapes", "Watermelon", "Papaya", "Guava", "Pomegranate", "Strawberry", "Blueberry", "Raspberry", "Cherry", "Kiwi", "Pear", "Peach", "Plum", "Blackberry", "Dragon Fruit", "Coconut", "Apricot", "Fig", "Litchi", "Jackfruit", "Persimmon", "Mulberry", "Avocado", "Custard Apple", "Tangerine"],
                "Vegetable": ["Potato", "Tomato", "Onion", "Carrot", "Spinach", "Cabbage", "Cauliflower", "Brinjal", "Ladyfinger", "Capsicum", "Pumpkin", "Bitter Gourd", "Cucumber", "Garlic", "Ginger", "Mushroom", "Peas", "Sweet Corn", "Radish", "Beetroot", "Drumstick", "Bottle Gourd", "Snake Gourd", "French Beans", "Cluster Beans", "Turnip", "Coriander Leaves", "Mint Leaves", "Spring Onion", "Leeks"],
                "Dairy": ["Milk", "Butter", "Cheese", "Paneer", "Curd", "Ghee", "Cream", "Condensed Milk", "Khoya", "Buttermilk", "Lassi", "Flavored Yogurt", "Whey Protein", "Malted Milk", "Evaporated Milk", "Cottage Cheese", "Ricotta Cheese", "Mozzarella", "Parmesan", "Cheddar", "Blue Cheese", "Camembert", "Brie", "Feta", "Goat Cheese", "Sheep Cheese", "Swiss Cheese", "Gouda", "Provolone", "Halloumi"],
                "Beverage": ["Tea", "Coffee", "Green Tea", "Lassi", "Coconut Water", "Lemonade", "Soda", "Fruit Juice", "Sugarcane Juice", "Energy Drink", "Herbal Tea", "Black Tea", "Iced Tea", "Milkshake", "Smoothie", "Thandai", "Butter Milk", "Soft Drink", "Sattu Drink", "Kombucha", "Aloe Vera Juice", "Turmeric Latte", "Barley Water", "Rose Sharbat", "Basil Seed Drink", "Kokum Juice", "Mango Shake", "Watermelon Juice", "Cold Coffee", "Carrot Juice"],
                "Snack": ["Namkeen", "Bhujia", "Papad", "Chips", "Samosa", "Dhokla", "Kachori", "Sev", "Murukku", "Banana Chips", "Khakhra", "Mathri", "Moong Dal", "Peanut Chikki", "Sesame Chikki", "Popcorn", "Rice Crackers", "Puffed Rice", "Nachos", "Corn Puffs", "Ribbon Pakoda", "Shakarpara", "Gajak", "Pani Puri", "Chakli", "Masala Peanuts", "Rusk", "Breadsticks", "Tapioca Chips", "Aloo Bhujia"],
                "Oil": ["Mustard Oil", "Coconut Oil", "Groundnut Oil", "Sunflower Oil", "Olive Oil", "Sesame Oil", "Rice Bran Oil", "Soybean Oil", "Canola Oil", "Palm Oil", "Flaxseed Oil", "Avocado Oil", "Grapeseed Oil", "Hemp Seed Oil", "Almond Oil", "Walnut Oil", "Macadamia Nut Oil", "Peanut Oil", "Corn Oil", "Butter Oil", "Ghee", "Tallow", "Lard", "Fish Oil", "Cod Liver Oil", "Safflower Oil", "Camellia Oil", "Hazelnut Oil", "Pumpkin Seed Oil", "Emu Oil"],
                "Dry Fruits": ["Almonds", "Cashews", "Walnuts", "Pistachios", "Raisins", "Dates", "Figs", "Apricots", "Hazelnuts", "Brazil Nuts", "Macadamia Nuts", "Pine Nuts", "Pecan Nuts", "Black Raisins", "Golden Raisins"],
                "Bakery": ["White Bread", "Brown Bread", "Multigrain Bread", "Buns", "Pav", "Croissants", "Bagels", "Dinner Rolls", "Cookies", "Biscuits", "Cakes", "Muffins", "Pastries", "Doughnuts", "Rusk"],
                "Meat": ["Chicken Breast", "Chicken Legs", "Mutton Curry Cut", "Mutton Mince", "Lamb Chops", "Goat Ribs", "Beef Steak", "Pork Chops", "Duck Meat", "Turkey Breast", "Ham", "Bacon", "Salami", "Sausages", "Meatballs"],
                "Seafood": ["Salmon", "Tuna", "Prawns", "Shrimp", "Crab", "Lobster", "Pomfret", "Hilsa", "Rohu", "Catfish", "King Fish", "Tilapia", "Squid", "Oysters", "Clams"],
                "Frozen Food": ["Frozen Peas", "Frozen Corn", "Frozen Mixed Vegetables", "Frozen French Fries", "Frozen Chicken Nuggets", "Frozen Fish Fillets", "Frozen Parathas", "Frozen Chapatis", "Frozen Spring Rolls", "Frozen Pizza", "Frozen Samosas", "Frozen Meatballs", "Frozen Kebabs", "Frozen Pasta", "Frozen Dumplings"],
                "Pickles & Preserves": ["Mango Pickle", "Lime Pickle", "Mixed Pickle", "Amla Pickle", "Garlic Pickle", "Green Chili Pickle", "Ginger Pickle", "Carrot Pickle", "Red Chili Pickle", "Gooseberry Pickle"],
                "Ready-to-Eat": ["Instant Poha", "Ready-to-eat Dal Tadka", "Instant Upma", "Frozen Paratha", "Ready-to-eat Rajma", "Instant Idli Mix", "Instant Dosa Mix", "Ready-to-eat Pav Bhaji", "Instant Masala Oats", "Frozen Paneer Butter Masala"],
                "Organic Products": ["Organic Turmeric", "Organic Honey", "Organic Jaggery", "Organic Wheat Flour", "Organic Lentils", "Organic Rice", "Organic Green Tea", "Organic Coconut Oil", "Organic Almonds", "Organic Quinoa"],
                "Baking Essentials": ["Baking Powder", "Yeast", "Cocoa Powder", "Chocolate Chips", "Vanilla Extract", "Cake Mix", "Almond Flour", "Cornstarch", "Baking Soda", "Icing Sugar"],
                "Nuts & Seeds": ["Sunflower Seeds", "Flaxseeds", "Chia Seeds", "Sesame Seeds", "Pumpkin Seeds", "Hemp Seeds", "Poppy Seeds", "Cumin Seeds", "Fennel Seeds", "Mustard Seeds"],
                "Health & Supplements": ["Whey Protein", "Multivitamins", "Protein Bars", "Omega-3 Capsules", "Herbal Supplements", "Energy Drinks", "Gluten-free Flour", "Apple Cider Vinegar", "Ashwagandha Powder", "Amla Juice"],
                "Confectionery": ["Dark Chocolate", "Milk Chocolate", "Candies", "Lollipops", "Caramel Toffee", "Jelly Beans", "Gummies", "Fudge", "White Chocolate", "Fruit Jellies"],
                "Pasta & Noodles": ["Spaghetti", "Penne", "Macaroni", "Instant Noodles", "Udon Noodles", "Vermicelli", "Rice Noodles", "Fusilli", "Lasagna Sheets", "Hakka Noodles"],
                "Spreads & Jams": ["Peanut Butter", "Hazelnut Spread", "Strawberry Jam", "Mango Jam", "Orange Marmalade", "Mixed Fruit Jam", "Honey", "Chocolate Spread", "Blueberry Jam", "Fig Jam"],
                "Breakfast Cereals": ["Cornflakes", "Choco Flakes", "Oats", "Granola", "Muesli", "Wheat Flakes", "Porridge Mix", "Ragi Flakes", "Bran Flakes", "Honey Loops"]

            }


















# conn = get_connection()
# cursor = conn.cursor()

# # Define categories and suppliers
# categories = {
#     "Cereal": "CAT_001",
#     "Pulse": "CAT_002",
#     "Spice": "CAT_003",
#     "Fruit": "CAT_004",
#     "Vegetable": "CAT_005",
#     "Dairy": "CAT_006",
#     "Beverage": "CAT_007",
#     "Snack": "CAT_008",
#     "Oil": "CAT_009",
#     "Condiment": "CAT_010",
#     "Dry Fruits": "CAT_011",
#     "Bakery": "CAT_012",
#     "Meat": "CAT_013",
#     "Seafood": "CAT_014",
#     "Frozen Food": "CAT_015",
#     "Pickles & Preserves": "CAT_016",
#     "Ready-to-Eat": "CAT_017",
#     "Organic Products": "CAT_018",
#     "Baking Essentials": "CAT_019",
#     "Nuts & Seeds": "CAT_020",
#     "Health & Supplements": "CAT_021",
#     "Confectionery": "CAT_022",
#     "Pasta & Noodles": "CAT_023",
#     "Spreads & Jams": "CAT_024",
#     "Breakfast Cereals": "CAT_025"
# }

# suppliers = {
#     "CAT_001": "SUP_001",
#     "CAT_002": "SUP_002",
#     "CAT_003": "SUP_003",
#     "CAT_004": "SUP_004",
#     "CAT_005": "SUP_005",
#     "CAT_006": "SUP_006",
#     "CAT_007": "SUP_007",
#     "CAT_008": "SUP_008",
#     "CAT_009": "SUP_009",
#     "CAT_010": "SUP_010",
#     "CAT_011": "SUP_011",
#     "CAT_012": "SUP_012",
#     "CAT_013": "SUP_013",
#     "CAT_014": "SUP_014",
#     "CAT_015": "SUP_015",
#     "CAT_016": "SUP_016",
#     "CAT_017": "SUP_017",
#     "CAT_018": "SUP_018",
#     "CAT_019": "SUP_019",
#     "CAT_020": "SUP_020",
#     "CAT_021": "SUP_021",
#     "CAT_022": "SUP_022",
#     "CAT_023": "SUP_023",
#     "CAT_024": "SUP_024",
#     "CAT_025": "SUP_025",
# }

# # Define products in each category (expanded to include at least 30 products per category)
# products = {
#     "Cereal": ["Basmati Rice", "Wheat Flour", "Maize", "Barley", "Millet", "Oats", "Cornflakes", "Quinoa", "Ragi", "Sorghum", "Foxtail Millet", "Brown Rice", "Amaranth", "Buckwheat", "Wild Rice", "Pearl Millet", "Teff", "Farro", "Freekeh", "Triticale", "Spelt", "Kamut", "Bran", "Semolina", "Broken Wheat", "Whole Wheat", "Rice Bran", "Rice Flakes", "Puffed Rice", "Barley Flakes"],
#     "Pulse": ["Toor Dal", "Masoor Dal", "Chana Dal", "Urad Dal", "Moong Dal", "Rajma", "Kabuli Chana", "Black Eyed Peas", "Masoor Whole", "Moth Beans", "Whole Moong", "Black Gram", "Bengal Gram", "Green Peas", "Red Kidney Beans", "Split Peas", "Pigeon Peas", "Horse Gram", "Chickpeas", "Lobia", "Green Gram", "Black Chickpeas", "White Peas", "Yellow Moong Dal", "Dried Lentils", "Whole Black Urad", "Split Urad Dal", "Brown Lentils", "Sprouted Moong", "Masoor Malka Dal"],
#     "Spice": ["Turmeric", "Red Chili Powder", "Coriander Powder", "Cumin Seeds", "Black Pepper", "Cardamom", "Cloves", "Cinnamon", "Nutmeg", "Star Anise", "Bay Leaves", "Asafoetida", "Mace", "Fennel Seeds", "Mustard Seeds", "Fenugreek Seeds", "Saffron", "Dry Ginger", "Black Salt", "White Pepper", "Kasuri Methi", "Tamarind", "Dried Mint", "Pomegranate Seeds", "Carom Seeds", "Celery Seeds", "Nigella Seeds", "Black Cardamom", "Dry Mango Powder", "Allspice"],
#     "Fruit": ["Mango", "Banana", "Apple", "Orange", "Pineapple", "Grapes", "Watermelon", "Papaya", "Guava", "Pomegranate", "Strawberry", "Blueberry", "Raspberry", "Cherry", "Kiwi", "Pear", "Peach", "Plum", "Blackberry", "Dragon Fruit", "Coconut", "Apricot", "Fig", "Litchi", "Jackfruit", "Persimmon", "Mulberry", "Avocado", "Custard Apple", "Tangerine"],
#     "Vegetable": ["Potato", "Tomato", "Onion", "Carrot", "Spinach", "Cabbage", "Cauliflower", "Brinjal", "Ladyfinger", "Capsicum", "Pumpkin", "Bitter Gourd", "Cucumber", "Garlic", "Ginger", "Mushroom", "Peas", "Sweet Corn", "Radish", "Beetroot", "Drumstick", "Bottle Gourd", "Snake Gourd", "French Beans", "Cluster Beans", "Turnip", "Coriander Leaves", "Mint Leaves", "Spring Onion", "Leeks"],
#     "Dairy": ["Milk", "Butter", "Cheese", "Paneer", "Curd", "Ghee", "Cream", "Condensed Milk", "Khoya", "Buttermilk", "Lassi", "Flavored Yogurt", "Whey Protein", "Malted Milk", "Evaporated Milk", "Cottage Cheese", "Ricotta Cheese", "Mozzarella", "Parmesan", "Cheddar", "Blue Cheese", "Camembert", "Brie", "Feta", "Goat Cheese", "Sheep Cheese", "Swiss Cheese", "Gouda", "Provolone", "Halloumi"],
#     "Beverage": ["Tea", "Coffee", "Green Tea", "Lassi", "Coconut Water", "Lemonade", "Soda", "Fruit Juice", "Sugarcane Juice", "Energy Drink", "Herbal Tea", "Black Tea", "Iced Tea", "Milkshake", "Smoothie", "Thandai", "Butter Milk", "Soft Drink", "Sattu Drink", "Kombucha", "Aloe Vera Juice", "Turmeric Latte", "Barley Water", "Rose Sharbat", "Basil Seed Drink", "Kokum Juice", "Mango Shake", "Watermelon Juice", "Cold Coffee", "Carrot Juice"],
#     "Snack": ["Namkeen", "Bhujia", "Papad", "Chips", "Samosa", "Dhokla", "Kachori", "Sev", "Murukku", "Banana Chips", "Khakhra", "Mathri", "Moong Dal", "Peanut Chikki", "Sesame Chikki", "Popcorn", "Rice Crackers", "Puffed Rice", "Nachos", "Corn Puffs", "Ribbon Pakoda", "Shakarpara", "Gajak", "Pani Puri", "Chakli", "Masala Peanuts", "Rusk", "Breadsticks", "Tapioca Chips", "Aloo Bhujia"],
#     "Oil": ["Mustard Oil", "Coconut Oil", "Groundnut Oil", "Sunflower Oil", "Olive Oil", "Sesame Oil", "Rice Bran Oil", "Soybean Oil", "Canola Oil", "Palm Oil", "Flaxseed Oil", "Avocado Oil", "Grapeseed Oil", "Hemp Seed Oil", "Almond Oil", "Walnut Oil", "Macadamia Nut Oil", "Peanut Oil", "Corn Oil", "Butter Oil", "Ghee", "Tallow", "Lard", "Fish Oil", "Cod Liver Oil", "Safflower Oil", "Camellia Oil", "Hazelnut Oil", "Pumpkin Seed Oil", "Emu Oil"],
#     "Dry Fruits": ["Almonds", "Cashews", "Walnuts", "Pistachios", "Raisins", "Dates", "Figs", "Apricots", "Hazelnuts", "Brazil Nuts", "Macadamia Nuts", "Pine Nuts", "Pecan Nuts", "Black Raisins", "Golden Raisins"],
#     "Bakery": ["White Bread", "Brown Bread", "Multigrain Bread", "Buns", "Pav", "Croissants", "Bagels", "Dinner Rolls", "Cookies", "Biscuits", "Cakes", "Muffins", "Pastries", "Doughnuts", "Rusk"],
#     "Meat": ["Chicken Breast", "Chicken Legs", "Mutton Curry Cut", "Mutton Mince", "Lamb Chops", "Goat Ribs", "Beef Steak", "Pork Chops", "Duck Meat", "Turkey Breast", "Ham", "Bacon", "Salami", "Sausages", "Meatballs"],
#     "Seafood": ["Salmon", "Tuna", "Prawns", "Shrimp", "Crab", "Lobster", "Pomfret", "Hilsa", "Rohu", "Catfish", "King Fish", "Tilapia", "Squid", "Oysters", "Clams"],
#     "Frozen Food": ["Frozen Peas", "Frozen Corn", "Frozen Mixed Vegetables", "Frozen French Fries", "Frozen Chicken Nuggets", "Frozen Fish Fillets", "Frozen Parathas", "Frozen Chapatis", "Frozen Spring Rolls", "Frozen Pizza", "Frozen Samosas", "Frozen Meatballs", "Frozen Kebabs", "Frozen Pasta", "Frozen Dumplings"],
#     "Pickles & Preserves": ["Mango Pickle", "Lime Pickle", "Mixed Pickle", "Amla Pickle", "Garlic Pickle", "Green Chili Pickle", "Ginger Pickle", "Carrot Pickle", "Red Chili Pickle", "Gooseberry Pickle"],
#     "Ready-to-Eat": ["Instant Poha", "Ready-to-eat Dal Tadka", "Instant Upma", "Frozen Paratha", "Ready-to-eat Rajma", "Instant Idli Mix", "Instant Dosa Mix", "Ready-to-eat Pav Bhaji", "Instant Masala Oats", "Frozen Paneer Butter Masala"],
#     "Organic Products": ["Organic Turmeric", "Organic Honey", "Organic Jaggery", "Organic Wheat Flour", "Organic Lentils", "Organic Rice", "Organic Green Tea", "Organic Coconut Oil", "Organic Almonds", "Organic Quinoa"],
#     "Baking Essentials": ["Baking Powder", "Yeast", "Cocoa Powder", "Chocolate Chips", "Vanilla Extract", "Cake Mix", "Almond Flour", "Cornstarch", "Baking Soda", "Icing Sugar"],
#     "Nuts & Seeds": ["Sunflower Seeds", "Flaxseeds", "Chia Seeds", "Sesame Seeds", "Pumpkin Seeds", "Hemp Seeds", "Poppy Seeds", "Cumin Seeds", "Fennel Seeds", "Mustard Seeds"],
#     "Health & Supplements": ["Whey Protein", "Multivitamins", "Protein Bars", "Omega-3 Capsules", "Herbal Supplements", "Energy Drinks", "Gluten-free Flour", "Apple Cider Vinegar", "Ashwagandha Powder", "Amla Juice"],
#     "Confectionery": ["Dark Chocolate", "Milk Chocolate", "Candies", "Lollipops", "Caramel Toffee", "Jelly Beans", "Gummies", "Fudge", "White Chocolate", "Fruit Jellies"],
#     "Pasta & Noodles": ["Spaghetti", "Penne", "Macaroni", "Instant Noodles", "Udon Noodles", "Vermicelli", "Rice Noodles", "Fusilli", "Lasagna Sheets", "Hakka Noodles"],
#     "Spreads & Jams": ["Peanut Butter", "Hazelnut Spread", "Strawberry Jam", "Mango Jam", "Orange Marmalade", "Mixed Fruit Jam", "Honey", "Chocolate Spread", "Blueberry Jam", "Fig Jam"],
#     "Breakfast Cereals": ["Cornflakes", "Choco Flakes", "Oats", "Granola", "Muesli", "Wheat Flakes", "Porridge Mix", "Ragi Flakes", "Bran Flakes", "Honey Loops"]

# }


# # Generate product list
# def generate_products():
#     product_list = []
#     product_id = 1
    
#     for category, items in products.items():
#         category_id = categories[category]
#         supplier_id = suppliers[category_id]
        
#         for item in items:
#             procurement_price = random.randint(10, 50)
#             sales_price = round(procurement_price * random.uniform(1.4, 1.6), 2)
#             unit_quantity = "1 kg" if category not in ["Spice", "Dairy", "Beverage", "Condiment"] else "500 g"
            
#             product_list.append((
#                 f"PROD_{str(product_id).zfill(3)}", item, category, category_id, supplier_id, unit_quantity, procurement_price, sales_price
#             ))
            
#             product_id += 1
    
#     return product_list

# # Print the generated products
# generated_products = generate_products()
# for product in generated_products:
#     print(product)


# """
# ProductID VARCHAR(255) PRIMARY KEY
# ,ProductName VARCHAR(100) NOT NULL
# ,CategoryID VARCHAR(255) 
# ,SupplierID VARCHAR(255) 
# ,Price DECIMAL(10,2) NOT NULL
# ,Cost DECIMAL(10,2) NOT NULL
# ,StockQuantity INT DEFAULT 0
# ,IsActive BOOLEAN DEFAULT TRUE
# """

# df = pd.DataFrame(generated_products, columns=["ProductID","ProductName","ProductCategory","CategoryID","SupplierID","StockQuantity","Price","Cost"])

# insert_query = f"""INSERT INTO Products2 (ProductID,ProductName,ProductCategory,CategoryID,SupplierID,StockQuantity,Price,Cost)
#                     VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"""
# data_to_insert = [tuple(row) for row in df.values]
# print("data_to_insert :",data_to_insert)
# cursor.executemany(insert_query, data_to_insert)
# conn.commit()
# print(f"Successfully inserted {len(data_to_insert)} records into Products2")

