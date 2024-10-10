import unittest
from morning_greetings.contacts import Contacts
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message
from morning_greetings.logger import log_message
import os


class TestContacts(unittest.TestCase):
    def setUp(self):
        self.contacts = Contacts()

    def test_add_contact(self):
        self.contacts.add_contact("Alice", "alice@example.com")
        self.assertEqual(len(self.contacts.get_contacts()), 1)
        self.assertEqual(self.contacts.get_contacts()[0]['name'], 'Alice')

    def test_remove_contact(self):
        self.contacts.add_contact("Bob", "bob@example.com")
        self.contacts.remove_contact("Bob")
        self.assertEqual(len(self.contacts.get_contacts()), 0)

    def test_get_contacts(self):
        self.contacts.add_contact("Charlie", "charlie@example.com")
        self.assertEqual(len(self.contacts.get_contacts()), 1)


class TestMessageGenerator(unittest.TestCase):
    def test_generate_message(self):
        message = generate_message("Alice")
        self.assertEqual(message, "Good Morning, Alice! Have a great day!")


class TestMessageSender(unittest.TestCase):
    def test_send_message_success(self):
        try:
            send_message("bob@example.com", "Good Morning, Bob!")
        except Exception as e:
            self.fail(f"send_message raised Exception unexpectedly: {e}")

    def test_send_message_missing_email(self):
        with self.assertRaises(ValueError):
            send_message("", "Good Morning!")


class TestLogger(unittest.TestCase):
    def setUp(self):
        # Remove the log file before testing
        if os.path.exists("message_log.txt"):
            os.remove("message_log.txt")

    def test_log_message(self):
        contact = {"name": "Alice", "contact_info": "alice@example.com"}
        log_message(contact, "Good Morning, Alice!")
        # Verify the log file is created
        self.assertTrue(os.path.exists("message_log.txt"))
        
        # Verify the content of the log file
        with open("message_log.txt", "r") as log_file:
            log_content = log_file.read()
            self.assertIn("Sent to Alice: Good Morning, Alice!", log_content)


if __name__ == "__main__":
    unittest.main()
