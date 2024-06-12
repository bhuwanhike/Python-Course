import requests
import json
import pyttsx3

engine = pyttsx3.init()

a = input("Enter city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=f65cdc4ef90a4d8c8c2175938240406&q={a}\n"

r = requests.get(url).text
dict = json.loads(r)
need = [dict["location"] ["name"], dict["current"] ["temp_c"]]

print(need)
engine.say(f"the location is {need[0]} and the temperature here is {need[1]}")
engine.runAndWait()
