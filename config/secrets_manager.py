import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class SecretsManager:
    def __init__(self):
        self.spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
        self.spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        self.spotify_redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

    def validate_secrets(self):
        if not all([self.spotify_client_id, self.spotify_client_secret, self.spotify_redirect_uri]):
            raise ValueError("Missing required Spotify credentials in .env file")