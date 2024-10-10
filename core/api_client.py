from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from config import UID, SECRET, TOKEN_URL

class APIClient:
    def __init__(self):
        self.client = BackendApplicationClient(client_id=UID)
        self.oauth = OAuth2Session(client=self.client)
        self.token = self.fetch_token()

    def fetch_token(self):
        return self.oauth.fetch_token(token_url=TOKEN_URL,
                                      client_id=UID,
                                      client_secret=SECRET)

    def get_token(self):
        return self.token["access_token"]

    def get(self, url):
        return self.oauth.get(url).json()
