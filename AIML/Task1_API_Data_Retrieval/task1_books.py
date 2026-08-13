import requests
import sqlite3
API_URL = "https://openlibrary.org/search.json?q=python"

def fetch_books():
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()
        return data["docs"]
    else:
        print("Failed to fetch data")
        return []


def create_database():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            publication_year INTEGER
        )
    """)

    connection.commit()
    connection.close()


def store_books(books):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    for book in books:
        title = book.get("title", "Unknown")
        author = book.get("author_name", ["Unknown"])[0]
        year = book.get("first_publish_year", None)

        cursor.execute("""
            INSERT INTO books (title, author, publication_year)
            VALUES (?, ?, ?)
        """, (title, author, year))

    connection.commit()
    connection.close()


def display_books():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    print("\nBooks stored in database:")
    print("-" * 60)

    for book in books:
        print(f"ID: {book[0]}")
        print(f"Title: {book[1]}")
        print(f"Author: {book[2]}")
        print(f"Publication Year: {book[3]}")
        print("-" * 60)

    connection.close()

if __name__ == "__main__":

    create_database()

    books = fetch_books()

    if books:
        store_books(books)

    display_books()