import requests
import sqlite3

url = "https://gutendex.com/books"
r = requests.get(url)

data = r.json()["results"]


conn = sqlite3.connect("books.sqlite")
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS books
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR (500),
                author VARCHAR (500),
                author_birth_year INTEGER,
                author_death_year INTEGER);''')


for book in data:
    author = book["authors"][0]
    book_info = (book["title"], author["name"], author["birth_year"], author["death_year"])
    query = "INSERT INTO books (title, author, author_birth_year, author_death_year) VALUES (?, ?, ?, ?)"
    cursor.execute(query, book_info)
    conn.commit()


print("ინფორმაცია წარმატებით შეინახა")


conn.close()