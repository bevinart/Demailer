# NOTE: This file will be used for anything related to the functionality of Demailer
import os
import base64
from pathlib import Path

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build

SCOPES = [
    # SCOPE according to Google API: Read, compose, send, and permanently delete all your email from Gmail 
    "https://mail.google.com/" 
]

class Demailer_Backend():
    def __init__(self, cred_json_path=None):
        self.creds = None # What the Google API uses to give you access
        self.service = None # This is what we use to call the GmailAPI once gaining the credentials
        
        if cred_json_path == None:
            self.cred_json_path = None
        else:
            formatted_path = Path(cred_json_path)
            if not os.path.exists(formatted_path):
                return 1
            self.cred_json_path = formatted_path

    # This function will return a JSON used for grabbing anything from the Google APIs
    def get_user_token(cred_json_path=None, token_json_path=os.getcwd()+"/token.json"):
        # Using pathlib in order to turn the string into a path that the system can read
        if cred_json_path != None:
            self.cred_json_path = Path(cred_json_path)
        if not os.path.exists(self.cred_json_path):
            return 1
        
        # token.json is used in order to prevent logging in everytime you run the application. It is made during this function, so if first time running, it will make one. 
        token_json_path = Path(token_json_path)
        if not os.path.exists(token_json_path):
            return 2
        
        # This is used to grab any valid tokens from the JSON file if there is any
        self.creds = Credentials.from_authorized_user_file(token_json_path, SCOPES)
        
        # If there are no creds available that are valid, Refresh or Login
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.cred_json_path, SCOPES)
                self.creds = flow.run_local_server(port=0)

        # Save the creds for the next time the application is ran
        with open(token_json_path, "w") as token_file:
            token_file.write(self.creds.to_json())

        # Getting access to the Gmail API with out credentials
        # We put this here because we will be accessing it throughout many different functions
        self.service = build("gmail", "v1", credentials=self.creds)

        return

    def get_message(self, message_id):
        pass

    def _get_inbox(self, num_of_emails=25, offset=0):
        pass




