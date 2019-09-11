import requests
from pprint import pprint
from datetime import datetime
from geopy.geocoders import Nominatim
from collections import OrderedDict


def forecast(place, time=None, date=None, forecast=None):

    try:
        date_time = datetime.now()
        if time == None:
            time = date_time.strftime("%H:%M:%S")
        if date == None:
            date = date_time.strftime("%Y-%m-%d")
        if forecast == None:
            forecast == "daily"
    except Exception as e:
        return("Exception occured with parameters format")

    try:
        # convert place to lat and long
        geolocator = Nominatim(user_agent="forecast")
        location = geolocator.geocode(place)
        latitude = round(location.latitude, 2)
        longitude = round(location.longitude, 2)
    except Exception as e:
        print("Exception while fetching lat,long")

    try:
        # api endpoint to fetch 10 days data
        api_endpoint = f"https://api.weather.com/v2/turbo/vt1dailyForecast?apiKey=d522aa97197fd864d36b418f39ebb323&format=json&geocode={latitude}%2C{longitude}&language=en-IN&units=m"
        response = requests.get(api_endpoint)
        response_data = response.json()
    except Exception as e:
        print("Exception while accessing the API")

    try:
        # data wise data
        dates_time_list = response_data["vt1dailyForecast"]["validDate"]
        dates_list = [_.split("T0")[0] for _ in dates_time_list]
        # today's date index
        date_index = dates_list.index(date)
        # day
        temperature_day = response_data["vt1dailyForecast"][
            "day"]["temperature"][date_index]
        precipitate_day = response_data["vt1dailyForecast"][
            "day"]["precipPct"][date_index]
        uv_description_day = response_data["vt1dailyForecast"][
            "day"]["uvDescription"][date_index]
        wind_speed_day = response_data["vt1dailyForecast"][
            "day"]["windSpeed"][date_index]
        humidity_day = response_data["vt1dailyForecast"][
            "day"]["humidityPct"][date_index]
        # night
        temperature_night = response_data["vt1dailyForecast"][
            "night"]["temperature"][date_index]
        precipitate_night = response_data["vt1dailyForecast"][
            "night"]["precipPct"][date_index]
        uv_description_night = response_data["vt1dailyForecast"][
            "night"]["uvDescription"][date_index]
        wind_speed_night = response_data["vt1dailyForecast"][
            "night"]["windSpeed"][date_index]
        humidity_night = response_data["vt1dailyForecast"][
            "night"]["humidityPct"][date_index]

        forecast_output = OrderedDict()
        forecast_output["place"] = place
        forecast_output["time"] = time
        forecast_output["date"] = date
        forecast_output["day"] = {"temperature": temperature_day,
                                  "precipitate": precipitate_day,
                                  "uv_description": uv_description_day,
                                  "wind_speed": wind_speed_day,
                                  "humidity": humidity_day
                                  }

        forecast_output["night"] = {	"temperature": temperature_night,
                                     "precipitate": precipitate_night,
                                     "uv_description": uv_description_night,
                                     "wind_speed": wind_speed_night,
                                     "humidity": humidity_night
                                     }

    except Exception as e:
        print("Exception while fetching data")
        return None

    return pprint(forecast_output)
