import ssl
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
EMAIL_TO  = os.getenv("EMAIL_TO")
EMAIL_FROM = os.getenv("EMAIL_FROM") or SMTP_USER

def send_email(subject: str, body: str) -> bool:
    if not all([SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, EMAIL_TO, EMAIL_FROM]):
        print("✖ Email not sent: Missing SMTP/.env config.")
        return False
#   import pdb; pdb.set_trace()
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg.set_content(body)

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as server:
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
        print("✔ Email sent, "+subject)
        return True
    except Exception as e:
        print(f"✖ Email send failed: {e}{subject}")
        return False
