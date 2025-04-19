import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)
EMAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

def send_email(recipient_email, subject, body, attachments=None):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USERNAME
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    if attachments:
        for filename, filepath in attachments.items():
            with open(filepath, 'rb') as f:
                part = MIMEApplication(f.read(), Name=filename)
            part['Content-Disposition'] = f'attachment; filename="{filename}"'
            msg.attach(part)

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USERNAME, recipient_email, msg.as_string())
        print(f"Email envoyé à {recipient_email}")
        return True
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email: {e}")
        return False
      
