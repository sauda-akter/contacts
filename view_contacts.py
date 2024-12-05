def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
