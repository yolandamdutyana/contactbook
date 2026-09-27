# ==========================
# Contact Management System
# ==========================

# List to store all contacts
contacts = [
    {"name": "John", "phone": "071010111", "email": "john@gmail.com"},
    {"name": "Landzy", "phone": "071010112", "email": "landi@gmail.com"},
    {"name": "Thabo", "phone": "071010113", "email": "thabo@gmail.com"}
]


# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("\nContact added successfully!\n")


# Function to search for a contact by name
def search_contact(name):
    for contact in contacts:
        # lower() allows searching regardless of uppercase/lowercase
        if contact["name"].lower() == name.lower():
            return contact

    return None


# Function to delete a contact by name
def delete_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("\nContact deleted successfully!\n")
            return

    print("\nContact not found.\n")


# Function to display all contacts
def view_all():
    if len(contacts) == 0:
        print("\nNo contacts found.\n")
        return

    print("\n========== CONTACT LIST ==========")

    for contact in contacts:
        print(f"Name : {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print("-" * 30)


# ==========================
# Main Menu
# ==========================

while True:

    print("\n====== CONTACT MANAGEMENT SYSTEM ======")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_name = input("Enter the contact name to search: ")
        result = search_contact(search_name)

        if result:
            print("\nContact Found!")
            print(f"Name : {result['name']}")
            print(f"Phone: {result['phone']}")
            print(f"Email: {result['email']}\n")
        else:
            print("\nContact not found.\n")

    elif choice == "3":
        delete_name = input("Enter the contact name to delete: ")
        delete_contact(delete_name)

    elif choice == "4":
        view_all()

    elif choice == "5":
        print("\nThank you for using the Contact Management System.")
        break

    else:
        print("\nInvalid option. Please choose a number between 1 and 5.\n")
