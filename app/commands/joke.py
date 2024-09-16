# app/commands/joke.py

import requests

def tell_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke = response.json()
    return f"Here's a joke: {joke['setup']}... {joke['punchline']}"
