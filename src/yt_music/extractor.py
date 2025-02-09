import json
from src.yt_music.models import Song, Playlist

class YTMusicExtractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_songs(self):
        with open(self.file_path, "r") as file:
            data = json.load(file)

        liked_songs = []
        downloaded_songs = []

        for entry in data.get("tracks", []):
            song = Song(title=entry.get("title"), artist=entry.get("artist"), album=entry.get("album"))
            if entry.get("liked"):
                liked_songs.append(song)
            if entry.get("downloaded"):
                downloaded_songs.append(song)

        return Playlist(name="Liked Songs", songs=liked_songs), Playlist(name="Downloaded Songs", songs=downloaded_songs)