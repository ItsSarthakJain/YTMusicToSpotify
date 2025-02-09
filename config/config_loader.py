import yaml
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config", "config.yaml")

def load_config():
    with open(CONFIG_PATH, "r") as file:
        return yaml.safe_load(file)

config = load_config()