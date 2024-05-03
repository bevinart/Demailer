# NOTE: This file will be the one that grabs the token from the Google API

import demailer_gui as dgui
import gmail_fetcher as gfetch


SCOPES = [
    # SCOPE according to Google API: Read, compose, send, and permanently delete all your email from Gmail 
    "https://mail.google.com/" 
]

if __name__ == "__main__":
    pass