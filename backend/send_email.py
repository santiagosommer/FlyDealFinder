import os
import ssl
import smtplib

# Loads password from .env for security
from dotenv import load_dotenv

from email.message import EmailMessage


load_dotenv()

email_sender = 'sender@gmail.com'
password = os.getenv('PASSWORD')
email_reciever = 'reciever@gmail.com'

subject = 'email subject'

body = """
    email body
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465, context = context) as smtp:
    if password is not None:
        smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())