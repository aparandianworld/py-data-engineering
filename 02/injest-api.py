import requests
import pandas as pd

latitude = 40.7128
longitude = -74.0060
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        weather_data = {
            "Latitude": latitude,
            "Longitude": longitude,
            "Temperature": data["current_weather"]["temperature"],
            "Wind Speed": data["current_weather"]["windspeed"],
            "Wind Direction": data["current_weather"]["winddirection"],
            "Time": data["current_weather"]["time"],
        }

        df = pd.DataFrame([weather_data])
        print(df.info())
        print(df.describe())
        print(df.head())

    else:
        print(f"Error with HTTP response code: {response.status_code}")

except Exception as e:
    print(f"Error fetching the data: {e}")
