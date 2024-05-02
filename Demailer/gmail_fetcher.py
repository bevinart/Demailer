import os.path

# NOTE: This class MUST have a token readily available in order to use this class. If you do not have a token, please refer to function 'get_user_token()'
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
    
def get_user_token(client_id, client_secret, scopes):
    pass