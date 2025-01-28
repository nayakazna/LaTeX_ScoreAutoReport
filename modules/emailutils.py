import smtplib
from email.message import EmailMessage

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment=None):
    # Sends an email with attachment
    ## Setup the MIME
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content(body)
    msg.add_attachment(attachment)
    
    ## Send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
    except Exception as e:
        print(e)