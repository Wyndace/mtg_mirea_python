from .main import AppConfig

try:
    config = AppConfig("../config/config.yaml")
except FileNotFoundError:
    config = AppConfig("src/config/config.yaml")

__all__ = [
    "config",
]
