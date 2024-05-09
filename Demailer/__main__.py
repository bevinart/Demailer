# NOTE: This file will be the one that grabs the token from the Google API

import os
import demailer_gui as dgui
import demailer_backend as dback

SCOPES = [
    # SCOPE according to Google API: Read, compose, send, and permanently delete all your email from Gmail 
    "https://mail.google.com/" 
]

# Right now, we are going to test the backend of everything before we make a GUI
if __name__ == "__main__":
    # Grab the token we need to access the Gmail API
    cred_path = os.getcwd() + "/credentials.json"

    pass