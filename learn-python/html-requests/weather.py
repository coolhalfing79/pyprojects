import requests
import sys

url = "https://community-open-weather-map.p.rapidapi.com/weather"
headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}


def main(city):
    querystring = {
        "units": "%22metric%22",
        "q": city}
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    resp_test = response.json()
    try:
        weather = resp_test['weather']
        details = resp_test['main']
    except KeyError as ke:
        print(resp_test['cod'], resp_test['message'])
    else:
        print(weather[0]['main'])
        print('-' * len(weather[0]['main']))
        print('temperature: ', details['temp'] - 273.15)
        print('feels like: ', details['feels_like'] - 273.15)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        city = input('enter city: ')
        main(city)

'''
{
"coord":{"lon":72.85,"lat":19.01},
"weather":[{"id":721,"main":"Haze","description":"haze","icon":"50d"}],
"base":"stations",
"main":{"temp":303.15,"feels_like":308.35,"temp_min":303.15,"temp_max":303.15,"pressure":1003,"humidity":84},
"visibility":2500,
"wind":{"speed":3.6,"deg":230,"gust":8.7},
"clouds":{"all":75},
"dt":1594205212,
"sys":{"type":1,"id":9052,"country":"IN","sunrise":1594168615,"sunset":1594216204},
"timezone":19800,
"id":1275339,
"name":"Mumbai",
"cod":200
}
'''
