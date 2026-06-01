import requests
import os
from dotenv import load_dotenv
load_dotenv()
weather_api_key=os.getenv("WEATHER_API_KEY")
#def get_weather(city):
def get_weather(city:str)->dict:

    url="https://api.openweathermap.org/data/2.5/weather"
    params={
            "q":city,
             "appid":weather_api_key,
              "units":"metric"
    }
    response=requests.get(
                        url,
                        params=params
                        )
    return response.json()

# result=get_weather("London")
# print(result)
    