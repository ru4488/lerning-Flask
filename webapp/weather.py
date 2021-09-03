import requests 
from flask import current_app


def weather_by_city(city_name , number_of_days):
    weather_url = current_app.config["WEATHER_URL"]
    params = {
        "key" :  current_app.config["WEATHER_API_KEY"] , 
        "q" : city_name , 
        "days" : number_of_days
        }
    try:
        result = requests.get(weather_url , params = params)
        result.raise_for_status()
        weather = result.json()
        if 'current' in weather:
            try:
                return weather['current']
            except(IndexError , TypeError):
                return False
    except(requests.RequestException , ValueError):
        print("Сетевая ошибка")
        return False   
    return False

if __name__ == "__main__":
    print(weather_by_city("Paris" , 1))
