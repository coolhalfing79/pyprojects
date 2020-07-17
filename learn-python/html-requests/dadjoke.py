import requests
import random


print('initiating dad_joke_69420')
term = input('enter a topic for your joke: ')
url = 'https://icanhazdadjoke.com/search?'
response = requests.get(url,
						headers={'Accept':'application/json'},
						params={'term':term})
data = response.json()
num_results = len(data['results'])
if num_results > 0:
	print(f'I found {num_results} joke(s) for {term}')
	if num_results == 1:
		print(data['results'][0]['joke'])
	else:
		print(data['results'][random.randint(0,num_results)]['joke'])
else:
	print("uwu I'm sowwy I couldn't find any jokes")
