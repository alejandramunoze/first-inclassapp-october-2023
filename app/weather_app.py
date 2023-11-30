


import requests
import json
import pgeocode

from pgeocode import Nominatim
from datetime import datetime
from IPython.display import Image, display, HTML
from pandas import DataFrame



degree_sign = u"\N{DEGREE SIGN}"


def to_image(url):
    return '<img src="'+ url + '" width="32" >'


def chopped_date(start_time):
    return start_time[5:10]



def get_forecast(zip_code):

    nomi = pgeocode.Nominatim("us")
    location_info = nomi.query_postal_code(zip_code)

    city = location_info["place_name"]
    state = location_info["state_name"]
    latitude = location_info["latitude"]
    longitude = location_info["longitude"]

    print("ZIP CODE:", zip_code)
    print("LOCATION:", f"{city}, {state}")
    print("LAT:", latitude)
    print("LON:", longitude)

    request_url = f"https://api.weather.gov/points/{latitude},{longitude}"
    # print(request_url)
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    
    forecast_url = parsed_response["properties"]["forecast"]
    # print(forecast_url)
    forecast_response = requests.get(forecast_url)

    parsed_forecast_response = json.loads(forecast_response.text)
    
    periods = parsed_forecast_response["properties"]["periods"]
    daytime_periods = [period for period in periods if period.get("isDaytime")]

    # for period in daytime_periods:
    #    print("-------------")
    #    print("Day of Week:", period.get("name"))
    #    print("Date:", period.get("startTime")[:10])
    #    print("Temperature:", f"{period.get('temperature', '')} {DEGREE_SIGN}{period.get('temperatureUnit', '')}")
    #    print("Weather Condition:", period.get("shortForecast", ''))
    #    display(Image(url=period.get("icon", '')))

    df = DataFrame(daytime_periods)

    df["date"] = df["startTime"].apply(chopped_date)

    # df["img"] = df["icon"].apply(to_image)

    # combined column for temp display
    # ... h/t: https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-pandas-dataframe
    df["temp"] = df["temperature"].astype(str) + " " + degree_sign + df["temperatureUnit"]

    # rename cols:
    df.rename(columns={
        "name":"day",
        "shortForecast": "forecast"
    }, inplace=True)

    # drop unused cols:
    df.drop(columns=[
        "temperature", "temperatureUnit", "temperatureTrend",
        "windSpeed", "windDirection",
        "startTime", "endTime",
        "number", "isDaytime", "detailedForecast"
    ], inplace=True)

    # re-order columns:
    df = df.reindex(columns=['day', 'date', 'temp', 'forecast', 'icon'])

    # return df
    print("---")
    print("SEVEN DAY FORECAST")
    print("LOCATION:", f"{geo.place_name}, {geo.state_code}".upper())
    print("---")
    return HTML(df.to_html(escape=False, formatters=dict(icon=to_image)))



if __name__ == "__main__":

    print("WEATHER FORECAST...")

    zip_code = input("Please input a zip code (default: '20057'): ") or "20057"
    print("ZIP CODE:", symbol)

    forecast = get_forecast(zip_code)
