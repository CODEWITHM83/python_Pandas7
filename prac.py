import sqlite3

# Create database (it will auto-create file)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    region TEXT,
    sales_amount INTEGER
)
""")

# Insert sample data
data = [
    ("Laptop", "East", 50000),
    ("Mobile", "West", 20000),
    ("Tablet", "North", 15000),
    ("Laptop", "South", 55000),
    ("Mobile", "East", 22000),
    ("Tablet", "West", 12000)
]

cursor.executemany("INSERT INTO sales (product, region, sales_amount) VALUES (?, ?, ?)", data)

conn.commit()
conn.close()

print("Database created and data inserted!")