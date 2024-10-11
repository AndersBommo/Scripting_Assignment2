# main.py
from morning_greetings.contacts import Contacts
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message
from morning_greetings.logger import log_message

def main():
    # Create an instance of Contacts
    contact_manager = Contacts()
    
    # Add some test contacts
    contact_manager.add_contact('Alice', 'alice@example.com', '18:27')
    contact_manager.add_contact('Bob', 'bob@example.com', "13:00 PM")

    addcontact = input("Do you wish to add a new Contact to the list? ")

    if addcontact.lower() == "yes": 
        # Assuming contact_manager is an instance of the Contacts class
        user_input = input("Enter: Name, Email Address, and preferred time (separated with , ): ")

        # Split the input into the respective parts
        # This will return a list of strings: [name, email, preferred_time]
        name, email, preferred_time = [x.strip() for x in user_input.split(",")]

        # Call the add_contact method
        contact_manager.add_contact(name, email, preferred_time)




    
    # Get the list of contacts
    contacts = contact_manager.get_contacts()
    
    # Send messages
    for contact in contacts:
        message = generate_message(contact['name'])
        send_message(contact['contact_info'], message)
        log_message(contact, message)

if __name__ == "__main__":
    main()
