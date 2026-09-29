import csv
import re

with open("books.csv","r")as file:
    books=list(csv.DictReader(file))

print("All book details: ")
for book in books:
    print(book)

keyword=input("Enter title keyword: ")
pattern=re.compile(r"^"+re.escape(keyword),re.IGNORECASE)

print("\nMatching books: ")
found=False

for book in books:
    if pattern.search(book["Title"]):
        print (book)
        found=True
if(not found):
    print("No matching books found")