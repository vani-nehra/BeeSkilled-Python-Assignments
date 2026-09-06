# contact_book.py

contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")

    for name, details in contacts.items():
        print(f"Name  : {name}")
        print(f"Phone : {details['phone']}")
        print(f"Email : {details['email']}")
        print("-------------------")


def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print("\nContact Found!")
        print("Name :", name)
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")