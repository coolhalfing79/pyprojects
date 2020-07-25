import requests
from tkinter import *


url = "https://community-open-weather-map.p.rapidapi.com/weather"
headers = {
	'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
	'x-rapidapi-key': "dbba92ddbamshd2d6626e8f21f35p180636jsn3a18989f58e6"
}

def get_weather():
	city = entry.get()

	querystring = {"units": "%22metric%22", "q": city}
	response = requests.request("GET", url, headers=headers, params=querystring)
	resp_test = response.json()
	try:
		weather = resp_test['weather']
		details = resp_test['main']
	except KeyError as ke:
		print(resp_test['cod'], resp_test['message'])
	except requests.exceptions.ConnectionError as err:
		label = Label(root, text=err)
		label.pack()
	else:
		label1 = Label(root, text=weather[0]['main'] +
			'-' * len(weather[0]['main']) +
			'\ntemperature: ' + str(details['temp'] - 273.15) +
			'\nfeels like: ' + str(details['feels_like'] - 273.15))
		label1.pack()

root = Tk()

entry = Entry(root, width=50, borderwidth=1)
button = Button(root, width=50, command=get_weather)

entry.pack()
button.pack()

root.mainloop()