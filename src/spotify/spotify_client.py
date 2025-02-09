import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyClient:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope="playlist-modify-private user-library-modify"
        ))

    def create_playlist(self, name):
        user_id = self.sp.me()["id"]
        playlist = self.sp.user_playlist_create(user_id, name, public=False)
        return playlist["id"]

    def search_and_add_songs(self, playlist_id, songs):
        track_ids = []
        for song in songs:
            query = f"{song.title} {song.artist}"
            result = self.sp.search(q=query, type="track", limit=1)
            if result["tracks"]["items"]:
                track_ids.append(result["tracks"]["items"][0]["id"])

        for i in range(0, len(track_ids), 50):
            self.sp.playlist_add_items(playlist_id, track_ids[i:i+50])