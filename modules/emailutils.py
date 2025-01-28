import smtplib
from email.message import EmailMessage

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path=None, attachment_filename=None):
    # Sends an email with attachment
    ## Setup the MIME
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content(body)

    ## Attach the attachment if exists
    if (attachment_path != None):
        with open(attachment_path, 'rb') as f:  # Open in binary read mode
            msg.add_attachment(
                f.read(),                   # Content of the attachment
                maintype='application',     # MIME type category
                subtype='pdf',              # MIME type subtype
                filename=attachment_filename# Attachment name
            )
    
    ## Send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print(f'Email sent to {receiver_email}')
    except Exception as e:
        print(e)