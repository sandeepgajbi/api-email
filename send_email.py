import smtplib
import ssl
from email.message import EmailMessage
import os

USERNAME = "sandeepgajbi@gmail.com"
PASSWORD = os.getenv("PASSWORD")
HOST = "smtp.gmail.com"
PORT = 465


def send_email(recipient_email, subject, message):
    email = EmailMessage()
    email['To'] = recipient_email
    email['Subject'] = subject
    email.set_content(message)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(HOST, PORT, context=context) as server:
        server.login(USERNAME, PASSWORD)
        server.send_message(email)
