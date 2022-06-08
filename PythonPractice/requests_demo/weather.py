import requests

# url = "https://www.google.com"

open_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q=Hyattsville&appid=8575b64a4b987ea15158f3581b784926'

def get_city_info():
    response = requests.get(open_weather_url)
    print(response.text)
    print(type(response))

if __name__ == "__main__":
    get_city_info()
