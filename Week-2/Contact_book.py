#Contact book

contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone
    print("Contact added successfully!")


def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print("Name:", name)
        print("Phone:", contacts[name])
    else:
        print("Contact not found!")


def update_contact():
    name = input("Enter name to update: ")

    if name in contacts:
        new_phone = input("Enter new phone number: ")
        contacts[name] = new_phone
        print("Contact updated successfully!")
    else:
        print("Contact not found!")


def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")


while True:
    print("\n----- Contact Book -----")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Show all contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("\nAll Contacts:")
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "6":
        print("Exiting contact book...")
        break

    else:
        print("Enter a valid choice!")

