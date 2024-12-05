from save_all_contacts import save_all_contacts

def add_contact(contacts):
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")
    
    # Prevent duplicate phone numbers
    if any(contact['phone'] == phone for contact in contacts):
        print("Phone number already exists!")
        return contacts

    contact = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address
    }
    contacts.append(contact)
    save_all_contacts(contacts)
    print("Contact added successfully!")
    return contacts
