import json
import os

class YTMusicExtractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_songs(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        with open(self.file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()

            if not content:
                raise ValueError(f"Takeout JSON file is empty: {self.file_path}")

            try:
                data = json.loads(content)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON file: {self.file_path}. Error: {e}")

        # Process data
        liked_songs = []  # Extract liked songs
        downloaded_songs = []  # Extract downloaded songs

        return liked_songs, downloaded_songs