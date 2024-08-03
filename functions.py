import requests
from utils import format_person_data, format_planet_data, format_starship_data

def get_swapi_data(category, query):
    url = f'https://swapi.dev/api/{category}/?search={query}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return data['results'][0]  # Retorna o primeiro resultado encontrado
    return None

def get_formatted_data(category, query):
    data = get_swapi_data(category, query)
    if data:
        if category == 'people':
            return format_person_data(data)
        elif category == 'planets':
            return format_planet_data(data)
        elif category == 'starships':
            return format_starship_data(data)
    return "I couldn't find any information on that."

def get_help_message():
    return ("I'm here to help! You can ask me about people, planets, or starships from the Star Wars universe.\n"
            "To use, just type a message with the name you're looking for, e.g., 'Tell me about Luke Skywalker'.\n"
            "Available categories: people, planets, starships.\n"
            "Commands: \n"
            "!hi - Greet the bot.\n"
            "!help - Show this help message.")
