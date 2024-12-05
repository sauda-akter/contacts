def save_all_contacts(all_contacts):
    with open("all_contacts.csv", "w") as contactFile:
        for contact in all_contacts:
            line = f"{contact['name']}, {contact['email']}, {contact['phone']}, {contact['address']}\n"
            contactFile.write(line)