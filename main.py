from config.secrets_manager import SecretsManager
from config.config import config
from src.yt_music.extractor import YTMusicExtractor
from src.spotify.spotify_client import SpotifyClient
from src.spotify.syncer import SpotifySyncer
from src.utils.logger import setup_logger

logger = setup_logger("YT-to-Spotify Migrator")

def main():
    logger.info("Starting migration process...")

    # Load credentials
    secrets = SecretsManager()
    secrets.validate_secrets()

    # Load YouTube Music data
    yt_extractor = YTMusicExtractor(config["yt_music"]["takeout_file_path"])
    liked_playlist, downloaded_playlist = yt_extractor.extract_songs()

    # Spotify client and sync
    spotify_client = SpotifyClient(secrets.spotify_client_id, secrets.spotify_client_secret, secrets.spotify_redirect_uri)
    syncer = SpotifySyncer(spotify_client)

    if config["spotify"]["sync_liked_songs"]:
        logger.info("Syncing liked songs...")
        syncer.sync_playlist("Liked Songs", liked_playlist)

    logger.info("Syncing downloaded songs...")
    syncer.sync_playlist(config["spotify"]["playlist_name_downloaded"], downloaded_playlist)

if __name__ == "__main__":
    main()