import requests
from src.logging_config import logger

class BaseClient:
    def __init__(self):
        self.timeout = 30

    def get(self, url, params=None):
        try:
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            logger.info(f"Request Successful: {url}")
            return response.json()

        except requests.exceptions.RequestException as e:
            logger.error(f"Request Failed: {e}")
            return None