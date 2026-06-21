# get a refresh token from spotify

import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = "http://127.0.0.1:8080/callback"
SCOPE = "user-top-read"

if not CLIENT_ID or not CLIENT_SECRET:
    print("Error: no credentials. Check the .env file")
    exit()

sp_oauth = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
)

auth_url = sp_oauth.get_authorize_url()
print("Open this link:\n", auth_url)
response_url = input("Click 'Agree' & COPY the full URL and paste it here: \n")

try:
    code = sp_oauth.parse_response_code(response_url)
    token_info = sp_oauth.get_access_token(code)
    print("SUCCESS")

except Exception as e:
    print(f"ERROR with token: {str(e)}")