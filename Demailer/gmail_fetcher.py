import os.path
from pathlib import Path

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

# NOTE: This class MUST have a token readily available in order to use this class. If you do not have a token, please refer to function 'get_user_token()' in class 'GoogleAPI'
class GmailFetcher():
    def __init__(self, token):
        if self._is_token(token) == False:
            return (1, "Token is incorrect")
        self.token = token
    
    # This class will return a specified number of emails from the token's inbox, starting at the offset
    def get_inbox(self, num_of_emails, offset):
        pass
    
    
    def _is_token(token):
        return True

# This function will return a JSON variable
def get_user_token(cred_json_path, scopes):
    # Using pathlib in order to turn the string into a path that the system can read
    cred_json_path = Path(cred_json_path)
    
    # token.json is used in order to prevent logging in everytime you run the application. It is made during this function, so if first time running, it will make one. 
    token_json_path = Path("./token.json")
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
    with open(cred_json_path, "w") as cred_file:
        cred_file.write(creds.to_json())

    return creds