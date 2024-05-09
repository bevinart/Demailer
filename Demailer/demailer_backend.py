# NOTE: This file will be used for anything related to the functionality of Demailer
import os
import base64
from pathlib import Path

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build

service = None

# This function will return a JSON used for grabbing anything from the Google APIs
def get_user_token(cred_json_path, scopes):
    # Using pathlib in order to turn the string into a path that the system can read
    cred_json_path = Path(cred_json_path)
    
    # token.json is used in order to prevent logging in everytime you run the application. It is made during this function, so if first time running, it will make one. 
    token_json_path = Path(os.getcwd() + "/token.json")
    creds = None
    
    # This is used to grab any valid tokens from the JSON file if there is any
    if os.path.exists(token_json_path):
        creds = Credentials.from_authorized_user_file(token_json_path, scopes)
    
    # If there are no creds available that are valid, Refresh or Login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(cred_json_path, scopes)
            creds = flow.run_local_server(port=0)

    # Save the creds for the next time the application is ran
    with open(token_json_path, "w") as token_file:
        token_file.write(creds.to_json())

    # Getting access to the Gmail API with out credentials
    # We put this here because we will be accessing it throughout many different functions
    service = build("gmail", "v1", credentials=creds)

    return creds


def get_message(message_id):
    pass


# NOTE: This function REQUIRES a token in order to be used. To get a token, refer to the 'get_user_token()' function
def _get_inbox(creds, num_of_emails, offset):
    # This is used to make a the API call v1.users.labels with the 'list' method, the userId being the current user's email address
    inbox_results = service.users().messages().list(userId="me").execute()

    # This is a JSON, the 'get()' function is used to get a certain key from it. If nothing is returned, the default value will be an empty array
    emails = inbox_results.get("messages", [])
    if not emails:
        print("No emails found")
        return None

    return emails

    # print("Emails:")
    # for email in emails:
    #     message_json = service.users().messages().get(userId="me", id=email["id"]).execute()

    #     if message_json["payload"]["body"].get("data") is None:
    #         continue

    #     print(base64.urlsafe_b64decode(message_json["payload"]["body"]["data"]))

