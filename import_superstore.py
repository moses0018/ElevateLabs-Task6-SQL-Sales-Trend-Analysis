import pymysql
import pandas as pd

# Load CSV file
df = pd.read_csv("/Users/moses/Desktop/Sample - Superstore.csv", encoding='latin1')

# Convert date columns to MySQL-friendly format
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y")

# Connect to MySQL
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="kingofjungle",
    database="superstore_db"
)

cursor = connection.cursor()

# Insert rows into MySQL
for index, row in df.iterrows():
    sql = """
    INSERT INTO superstore_sales
    (order_id, order_date, ship_date, ship_mode, customer_id, segment, country, city, state,
     postal_code, region, product_id, category, sub_category, product_name, sales, quantity,
     discount, profit)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    cursor.execute(sql, (
        row["Order ID"], 
        row["Order Date"].strftime("%Y-%m-%d"),
        row["Ship Date"].strftime("%Y-%m-%d"),
        row["Ship Mode"], 
        row["Customer ID"], 
        row["Segment"], 
        row["Country"], 
        row["City"], 
        row["State"], 
        str(row["Postal Code"]) if not pd.isna(row["Postal Code"]) else None,
        row["Region"], 
        row["Product ID"], 
        row["Category"], 
        row["Sub-Category"], 
        row["Product Name"], 
        row["Sales"], 
        row["Quantity"], 
        row["Discount"], 
        row["Profit"]
    ))

connection.commit()
cursor.close()
connection.close()

print("Superstore data imported successfully!")
