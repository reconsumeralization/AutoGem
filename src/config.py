import json
import os


class Config:
    def __init__(self):
        self.configurations = {}
        self.config_file_path = "config.json"
        self.load_configurations()

    def load_configurations(self):
        if os.path.exists(self.config_file_path):
            with open(self.config_file_path, 'r') as config_file:
                self.configurations = json.load(config_file)
        else:
            print("Configuration file not found. Falling back to environment variables.")

    def get_config(self, key):
        return self.configurations.get(key, os.getenv(key))

    def get_api_key(self):
        api_key = self.get_config('API_KEY')
        if not api_key:
            raise ValueError("API key not found in configurations or environment variables.")
        return api_key
