class Song:
    def __init__(self, title, artist, album=None):
        self.title = title
        self.artist = artist
        self.album = album

    def __repr__(self):
        return f"Song(title={self.title}, artist={self.artist}, album={self.album})"


class Playlist:
    def __init__(self, name, songs=None):
        self.name = name
        self.songs = songs if songs else []

    def add_song(self, song):
        self.songs.append(song)

    def __repr__(self):
        return f"Playlist(name={self.name}, songs={len(self.songs)})"