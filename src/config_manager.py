import json
import os

DEFAULT_CONFIG_FILE_PATH = "config.json"

def load_config_from_file(file_path=DEFAULT_CONFIG_FILE_PATH):
    try:
        with open(file_path, 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        print(f"Configuration file not found at {file_path}.")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the configuration file at {file_path}.")
        return {}

def get_config_value(key, default_config_file_path=DEFAULT_CONFIG_FILE_PATH):
    value = os.getenv(key)
    if value is not None:
        return value
    config = load_config_from_file(default_config_file_path)
    return config.get(key)
