# Contact.py

class Contacts:
    def __init__(self) -> None:
        # Initialize an empty list to store contact information
        self.contacts = []

    def add_contact(self, name, contact_info, preferred_time='08:00 AM'):
        # Add a contact to the list with name, contact info, and preferred time
        contact = {
            'name': name,
            'contact_info': contact_info,
            'preferred_time': preferred_time
        }
        self.contacts.append(contact)  # Add the new contact to the contacts list

    def remove_contact(self, name):
        # Remove a contact by filtering out the one with the matching name
        self.contacts = [c for c in self.contacts if c['name'] != name]

    def get_contacts(self):
        # Return the entire list of contacts
        return self.contacts
