from __future__ import print_function
import requests
import schedule
import time
import subprocess
import info
import pickle
import base64
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def create_message(to, subject, message):
    """Create a message for an email.

    Args:
      to: Email address of the receiver.
      subject: The subject of the email message.
      message_text: The text of the email message.

    Returns:
      An object containing a base64url encoded email object.
    """
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = info.email_address
    message['subject'] = subject

    aMessage = MIMEText(message)
    message.attach(aMessage)

    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def send_email(provider, message):
    try: 
        message = provider.users().messages().send(userId=info.email_address, body=message).execute()
        print('Message ID: %s' % message['id'])
        print("Message has been successfully sent!")
        return message
    except Exception as e:
        print("An error has occurred: %s" % e)
        return None

def send_message(message):
    subprocess.call("osascript sendMessage.applescript '%s' '%s'" % (f'{info.phone}', f'{message}'), shell=True)

def get_affirmation():
    return requests.get('https://www.affirmations.dev/random').text

def email_message(message):
    credits = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credits = pickle.load(token)
    if not credits or not credits.valid:
        if credits and credits.expired and credits.refresh_token:
            credits.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            credits = flow.run_local_server(port=5000)
        with open('token.pickle', 'wb') as token:
            pickle.dump(credits, token)

    service = build('gmail', 'v1', credentials=credits)

    message = create_message(f'{info.phone}{info.carrier}', 'Affirmation', message)
    send_email(service, message)

def job():
    try:
        affirmation = get_affirmation()
        if affirmation != '':
            if info.mac:
                send_message(affirmation)
            else:
                email_message(affirmation)
        else:
            print("Error has occurred, please try again.")
    except Exception as e:
        print("An error has occurred: %s" % e)

if __name__ == "__main__":
    schedule.every().day.at(info.time).do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)