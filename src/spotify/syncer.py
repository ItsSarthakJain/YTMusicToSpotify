from src.spotify.spotify_client import SpotifyClient

class SpotifySyncer:
    def __init__(self, spotify_client):
        self.spotify_client = spotify_client

    def sync_playlist(self, playlist_name, playlist):
        playlist_id = self.spotify_client.create_playlist(playlist_name)
        self.spotify_client.search_and_add_songs(playlist_id, playlist.songs)