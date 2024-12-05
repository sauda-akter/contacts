def search_contacts(contacts):
    query = input("Enter name, email, or phone to search: ").lower()
    results = [contact for contact in contacts if query in contact['name'].lower() or query in contact['email'].lower() or query in contact['phone']]
    
    if results:
        print("Search results:")
        for contact in results:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
    else:
        print("No contacts found.")
