import requests
import json
import pyttsx3
engine = pyttsx3.init()
city = input("Enter the name of the City: ")

url = f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"

r = requests.get(url)
w_dic = json.loads(r.text)
print(w_dic)
temp = w_dic["current"]["temp_c"]

engine.say(f"The current temperature in {city} is {temp} degree Celcius.")
engine.runAndWait()
