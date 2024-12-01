# PDF Scrapper using pypdf

from pypdf import PdfReader
import sqlite3
import os

from character import Character
from skills import Skill

reader = PdfReader("../../Users/Rock/Documents/testpdfs/testpdf1.pdf")

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('''
               INSERT INTO users (name, age, email)
               VALUES(?, ?, ? )
               ''', ("Alice", 30, "alice@example.com"))
conn.commit()

cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)
#List<Character> investigatorRoster = ""

fields = reader.get_fields()
for field_name, field_data in fields.items():
    print(f"{field_name}: {field_data.get('/V')}")