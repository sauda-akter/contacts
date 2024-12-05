
def remove_contact(contacts):
    name = input("Enter the name of the contact to remove: ").strip().lower()
    new_contacts = [contact for contact in contacts if contact['name'].lower() != name]
    
    if len(new_contacts) < len(contacts):
        print("Contact removed successfully.")
    else:
        print("No contact found with that name.")
    
    return new_contacts
