#3. JSON File Reader
import json

with open("data.json", "r") as file:
    data = json.load(file)

print("----- STUDENT DETAILS -----")

print("Name:", data["name"])
print("Age:", data["age"])
print("Course:", data["course"])

print("Skills:")
for skill in data["skills"]:
    print("-", skill)