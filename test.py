import unittest
from morning_greetings.contacts import Contacts
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message
from morning_greetings.logger import log_message
import os  # To manage file operations like removing the log file


# Test suite for Contacts class
class TestContacts(unittest.TestCase):
    def setUp(self):
        # Set up a new instance of Contacts before each test
        self.contacts = Contacts()

    def test_add_contact(self):
        # Test if a contact is added correctly
        self.contacts.add_contact("Alice", "alice@example.com")
        self.assertEqual(len(self.contacts.get_contacts()), 1)  # Verify that one contact is added
        self.assertEqual(self.contacts.get_contacts()[0]['name'], 'Alice')  # Check if the name is correct

    def test_remove_contact(self):
        # Test if a contact is removed correctly
        self.contacts.add_contact("Bob", "bob@example.com")
        self.contacts.remove_contact("Bob")
        self.assertEqual(len(self.contacts.get_contacts()), 0)  # Verify the contact list is empty after removal

    def test_get_contacts(self):
        # Test if contacts can be retrieved correctly
        self.contacts.add_contact("Charlie", "charlie@example.com")
        self.assertEqual(len(self.contacts.get_contacts()), 1)  # Verify that one contact is present


# Test suite for message generation
class TestMessageGenerator(unittest.TestCase):
    def test_generate_message(self):
        # Test if the correct message is generated for a given name
        message = generate_message("Alice")
        self.assertEqual(message, "Good Morning, Alice! Have a great day!")  # Check if the message is as expected


# Test suite for sending messages
class TestMessageSender(unittest.TestCase):
    def test_send_message_success(self):
        # Test if sending a message works without errors
        try:
            send_message("bob@example.com", "Good Morning, Bob!")  # No exception should be raised
        except Exception as e:
            self.fail(f"send_message raised Exception unexpectedly: {e}")  # Fail the test if any exception is raised

    def test_send_message_missing_email(self):
        # Test if sending a message without an email raises a ValueError
        with self.assertRaises(ValueError):
            send_message("", "Good Morning!")  # A ValueError should be raised for missing email


# Test suite for logging messages
class TestLogger(unittest.TestCase):
    def setUp(self):
        # Remove the log file before each test to start with a clean state
        if os.path.exists("message_log.txt"):
            os.remove("message_log.txt")

    def test_log_message(self):
        # Test if a message is logged correctly
        contact = {"name": "Alice", "contact_info": "alice@example.com"}
        log_message(contact, "Good Morning, Alice!")
        
        # Check if the log file is created
        self.assertTrue(os.path.exists("message_log.txt"))  # Verify that the log file exists
        
        # Check if the content of the log file is correct
        with open("message_log.txt", "r") as log_file:
            log_content = log_file.read()
            self.assertIn("Sent to Alice: Good Morning, Alice!", log_content)  # Verify the logged message is correct


# Run all the tests when this script is executed
if __name__ == "__main__":
    unittest.main()
