import yaml


class AppConfig:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        try:
            import os
            with open(self.config_file, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Config file {self.config_file} not found. Creating a new one.")
            raise FileNotFoundError

    def save_config(self):
        with open(self.config_file, 'w') as file:
            yaml.dump(self.config, file, default_flow_style=False, encoding='UTF-8', allow_unicode=True)

    def __getitem__(self, key):
        self.config = self.load_config()
        return self.config.get(key, None)

    def __setitem__(self, key, value):
        self.config[key] = value
        self.save_config()
