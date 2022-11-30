import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendmail(mail_content):
    # The mail addresses and password
    sender_address = ''
    sender_pass = ''
    receiver_address = ''
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'rappel pour charger la nouvelle fichier des frais'  # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 25)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
