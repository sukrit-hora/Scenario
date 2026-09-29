import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="CSV file containing course records")
args = parser.parse_args()

with open(args.filename, "r") as file:
    reader = csv.DictReader(file)
    courses = list(reader)

print("All Course Records:")
for course in courses:
    print(course)

course_id = input("Enter Course ID to search: ")

found = False

for course in courses:
    if course["Course ID"] == course_id:
        print("Course Found:")
        print(course)
        found = True
        break

if not found:
    print("Course not found.")