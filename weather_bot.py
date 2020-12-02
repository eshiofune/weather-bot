import spacy
import requests

nlp = spacy.load("en_core_web_md")

def get_weather(city_name):
  response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" +
    city_name + "&APPID=API_KEY").json()
  weather = response["weather"][0]["description"]

  return weather

def chatbot(statement):
  weather = nlp("Current weather in a city")
  statement = nlp(statement)
  min_similarity = 0.75

  if weather.similarity(statement) >= min_similarity:
    for ent in statement.ents:
      if ent.label_ == "GPE": # GeoPolitical Entity
        city = ent.text
        break
    else:
      return "You need to tell me a city to check."

    city_weather = get_weather(city)
    return "In " + city + ", the current weather is: " + city_weather
  else:
    return "Sorry I don't understand that. Please rephrase your statement."

response = chatbot("What is the weather in Lagos today?")
print(response)
