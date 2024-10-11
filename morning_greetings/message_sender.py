#message_sender.py 
def send_message(email, message): 
    #Simulates sending a message to an email with a message
    if not email:
        raise ValueError("Email address is missing")
    print(f'Sending message to {email}: {message}')

