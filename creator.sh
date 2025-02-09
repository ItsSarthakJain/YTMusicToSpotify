#!/bin/bash

# Create subdirectories
mkdir -p "config"
mkdir -p "data"
mkdir -p "src/yt_music"
mkdir -p "src/spotify"
mkdir -p "src/utils"

# Create placeholder files
touch "config/config.yaml"
touch "config/secrets_manager.py"

touch "data/extracted_data.json"

touch "src/yt_music/extractor.py"
touch "src/yt_music/models.py"

touch "src/spotify/spotify_client.py"
touch "src/spotify/syncer.py"

touch "src/utils/logger.py"
touch "src/utils/helpers.py"

# Create main script and additional files
touch "main.py"
touch "requirements.txt"
touch "README.md"
touch ".env"

# Print completion message
echo "Project folder and file structure created successfully in "