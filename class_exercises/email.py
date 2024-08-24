class Email:
    def __init__(self, sender, recipients, subject, body):
        self.sender = sender
        self.recipients = recipients  # This should be a list of recipients
        self.subject = subject
        self.body = body

    def send_email(self):
        # For demonstration, we'll just print the email details
        print("Sending Email:")
        print(f"From: {self.sender}")
        print(f"To: {', '.join(self.recipients)}")
        print(f"Subject: {self.subject}")
        print("Body:")
        print(self.body)


# Example usage:
email = Email(
    sender="example@example.com",
    recipients=["recipient1@example.com", "recipient2@example.com"],
    subject="Hello!",
    body="This is a test email. wish a good day for you!"
)

email.send_email()
