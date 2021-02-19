import smtplib
from email.message import EmailMessage


def sendAnEmail():
    friend = input("Whom to Send >> ")

    subject = input("What is the subject >> ")

    message = input("What is the message >> ")

    # Initialize your emails dictionary
    emails = {"person": 'atharva.r.bhagat@gmail.com',
              "many_people": 'email_id1, email_id2, so on'}

    receiver = emails[friend]

    print(f'Successfully sent your email to {receiver}')

    send(subject, receiver, message)


def send(subject, friend, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('intelligent.mini.search@gmail.com', 'Ramnathi@23')
    email = EmailMessage()
    email['From'] = 'intelligent.mini.search@gmail.com'
    email['To'] = friend
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


sendAnEmail()
