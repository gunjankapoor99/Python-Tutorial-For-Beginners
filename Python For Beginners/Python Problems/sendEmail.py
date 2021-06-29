import smtplib
import config

def send_email(subject, msg):
    try:
        server = smtplib.SMTP("your_emailAddress_here")
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS,config.PASSWORD)