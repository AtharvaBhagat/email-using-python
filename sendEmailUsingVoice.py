# pip install pyttsx3
# pip install SpeechRecognition

import pyttsx3
import speech_recognition as rec
import smtplib
from email.message import EmailMessage
from win10toast import ToastNotifier


notify = ToastNotifier()
listener = rec.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text: str):
    engine.say(text)
    engine.runAndWait()


def hearYou(time=3):
    with rec.Microphone() as source:
        voice = listener.record(source, time)
        command = listener.recognize_google(voice)
        low = command.lower()
    return low


def sendAnEmail():
    talk("Whom to Send")
    friend = hearYou()

    talk("What is the subject")
    subject = hearYou(5)

    talk("What is the message")
    message = hearYou(5)

    # Initialize your emails dictionary
    emails = {"person": 'email-id',
              "many_people": 'email_id1, email_id2, so on'}

    receiver = emails[friend]
    notify.show_toast("Emails by AtharvaBhagat",
                      "Successfully Sent Email to :" + receiver, threaded=True)
    talk(f'Successfully sent your email to {receiver}')

    send(subject, receiver, message)


def send(subject, friend, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your-email-id', 'your-password')
    email = EmailMessage()
    email['From'] = 'your-email-id'
    email['To'] = friend
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


sendAnEmail()
