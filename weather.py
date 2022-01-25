# tutorial: https://www.youtube.com/watch?v=Oz3W-LKfafE&list=WL&index=19
# documentation on how to use the API: https://openweathermap.org/current

import requests

API_KEY = "f885a8fb722e68f6b48f79ef11ea8c44"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    # print(data)
    weather = data['weather'][0]['description']
    #print(weather)
    temperature = round(data['main']['temp'] - 273.15, 2)
    #print(temperature)
    display = "The weather is {} and the temperature is {}."
    print(display.format(weather, temperature))
    
else:
    print("didn't work")

