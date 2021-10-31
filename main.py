from __future__ import print_function
import requests
import schedule
import time
import subprocess
import util
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
    message['from'] = util.email_address
    message['subject'] = subject

    aMessage = MIMEText(message)
    message.attach(aMessage)

    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def send_email(provider, message):
    try: 
        message = service.users().messages().send(userId=util.email_address, body=message).execute()
        print('Message ID: %s' % message['id'])
        print("Message has been successfully sent!")
        return message
    except Exception as e:
        print("An error has occurred: %s" % e)
        return None