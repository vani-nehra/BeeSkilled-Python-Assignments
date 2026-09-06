import csv
import os

FILE_NAME = "students.csv"


# Create CSV file if it does not exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["Roll Number", "Name", "Marks"])


# Add Student
def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([roll, name, marks])

    print("Student added successfully!")


# Display all students
def display_students():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        print("\n----- STUDENT LIST -----")

        found = False

        for student in reader:
            found = True

            print(
                "Roll Number:", student["Roll Number"],
                "| Name:", student["Name"],
                "| Marks:", student["Marks"]
            )

        if not found:
            print("No students found.")


# Search Student
def search_student():
    roll = input("Enter roll number to search: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["Roll Number"] == roll:
                print("\nStudent Found!")
                print("Roll Number:", student["Roll Number"])
                print("Name:", student["Name"])
                print("Marks:", student["Marks"])
                return

    print("Student not found!")


# Delete Student
def delete_student():
    roll = input("Enter roll number to delete: ")

    students = []
    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["Roll Number"] == roll:
                found = True
            else:
                students.append(student)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            fieldnames = ["Roll Number", "Name", "Marks"]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(students)

        print("Student deleted successfully!")

    else:
        print("Student not found!")


# Update Student
def update_student():
    roll = input("Enter roll number to update: ")

    students = []
    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for student in reader:

            if student["Roll Number"] == roll:
                found = True

                print("Current Name:", student["Name"])
                print("Current Marks:", student["Marks"])

                student["Name"] = input("Enter new name: ")
                student["Marks"] = input("Enter new marks: ")

            students.append(student)

    if found:
        with open(FILE_NAME, "w", newline="") as file:

            fieldnames = ["Roll Number", "Name", "Marks"]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(students)

        print("Student updated successfully!")

    else:
        print("Student not found!")


# Main Menu
def main():

    initialize_file()

    while True:

        print("\n-----------------------------")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("-----------------------------")

        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


main()