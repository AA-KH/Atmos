from src.clients.base_client import BaseClient

class AirQualityClient(BaseClient):
    BASE_URL = ("https://air-quality-api.open-meteo.com/v1/air-quality")

    def get_air_quality(self,latitude,longitude):
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": [
                "pm10",
                "pm2_5",
                "nitrogen_dioxide",
                "ozone"
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
            "pm25":
                current["pm2_5"],
            "pm10":
                current["pm10"],
            "o3":
                current["ozone"],
            "no2":
                current["nitrogen_dioxide"]
        }