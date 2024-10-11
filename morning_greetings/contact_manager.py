#Contact_manager.py

"""
This class manages a list of contacts. It provides functionality to add, remove, retrieve, 
and list contacts, each having a name, email address, and preferred time for receiving messages.
"""
class ContactsManager: 
    def __init__(self) -> None:
        self.contacts = [
            {"name": "Alice", "Email": "abc@example.com", "preferred_time" : "08:00 AM"},
            {"name": "Bob", "Email": "bcd@example.com", "preferred_time" : "09:00 AM"},
            {"name": "Charlie", "Email": "cde@example.com", "preferred_time" : "08:00 AM"}]

    def add_contact(self, name, email, preferred_time="08:00 AM"): 
        #Adds a new contact to the contact list using the parameters name, email, preferred time
        contact = {
            'name' : name, 
            'email' : email, 
            'preferred_time' : preferred_time
        }
        self.contact.append(contact)

    def remove_contact(self, name): 
        #Removes a contact in the based on the name of the contact
        self.contacts = [c for c in self.contacts if c['name'] != name]
    
    def get_contacts(self): 
        #Returns the list of contacts saved
        return self.contacts
    
    def list_contacts(self): 
        # Prints the list of contacts saved, their email and their preferred time of message
        for contact in self.contacts: 
            print(f'name: {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}')

