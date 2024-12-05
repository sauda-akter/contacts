# Contact Book Management System

import add_contact
import view_contacts
import search_contacts
import remove_contact
import file_manager

def main():
    all_contacts = file_manager.load_contacts()
    
    while True:
        print("\nWelcome to Contact Book Management System")
        print("0. Exit")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Remove Contact")

        menu = input("Select an option: ")

        if menu == "0":
            print("Thanks for using 'Contact Book Management System'!")
            file_manager.save_contacts(all_contacts)
            break

        elif menu == "1":
            all_contacts = add_contact.add_contact(all_contacts)

        elif menu == "2":
            view_contacts.view_contacts(all_contacts)

        elif menu == "3":
            search_contacts.search_contacts(all_contacts)

        elif menu == "4":
            all_contacts = remove_contact.remove_contact(all_contacts)

        else:
            print("Select an existing option!")

if __name__ == "__main__":
    main()