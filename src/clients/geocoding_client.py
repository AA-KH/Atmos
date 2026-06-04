from src.clients.base_client import BaseClient

class GeocodingClient(BaseClient):
    BASE_URL = ("https://geocoding-api.open-meteo.com/v1/search")

    def get_city_info(self, city_name):
        params = {
            "name": city_name,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        data = self.get(
            self.BASE_URL,
            params=params
        )

        if not data:
            return None

        if "results" not in data:
            return None

        city = data["results"][0]

        return {
            "city_name": city["name"],
            "country": city["country_code"],
            "latitude": city["latitude"],
            "longitude": city["longitude"],
            "timezone": city.get("timezone")
        }