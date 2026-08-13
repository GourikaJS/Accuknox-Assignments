import csv
import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

# Create users table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
""")

# Read data from CSV file
with open("users.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute("""
            INSERT INTO users (name, email)
            VALUES (?, ?)
        """, (row["name"], row["email"]))

# Save changes
connection.commit()

print("CSV data inserted into database successfully.")

# Retrieve users from the database
cursor.execute("SELECT * FROM users")

users = cursor.fetchall()

print("\nUsers stored in database:")
print("-" * 50)

for user in users:
    print("ID:", user[0])
    print("Name:", user[1])
    print("Email:", user[2])
    print("-" * 50)

connection.close()