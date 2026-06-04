from src.clients.base_client import BaseClient

class WeatherClient(BaseClient):

    BASE_URL = ("https://api.open-meteo.com/v1/forecast")

    def get_weather(self, latitude,longitude):

        params = {
            "latitude": latitude,
            "longitude": longitude,

            "current": [
                "temperature_2m",
                "relative_humidity_2m",
                "precipitation",
                "wind_speed_10m"
            ]
        }

        data = self.get(
            self.BASE_URL,
            params=params
        )

        if not data:
            return None

        current = data["current"]

        return {
            "temperature":
                current["temperature_2m"],

            "humidity":
                current["relative_humidity_2m"],

            "wind_speed":
                current["wind_speed_10m"],

            "precipitation":
                current["precipitation"]
        }