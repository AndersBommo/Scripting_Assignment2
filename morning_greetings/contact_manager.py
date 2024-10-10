#Contact_manager.py
class ContactsManager: 
    def __init__(self) -> None:
        self.contacts = [
            {"name": "Alice", "Email": "abc@example.com", "preferred_time" : "08:00 AM"},
            {"name": "Bob", "Email": "bcd@example.com", "preferred_time" : "09:00 AM"},
            {"name": "Charlie", "Email": "cde@example.com", "preferred_time" : "08:00 AM"}]

    def add_contact(self, name, email, preferred_time="08:00 AM"): 
        contact = {
            'name' : name, 
            'email' : email, 
            'preferred_time' : preferred_time
        }
        self.contact.append(contact)

    def remove_contact(self, name): 
        self.contacts = [c for c in self.contacts if c['name'] != name]
    
    def get_contacts(self): 
        return self.contacts
    
    def list_contacts(self): 
        for contact in self.contacts: 
            print(f'name: {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}')

