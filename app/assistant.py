import time
from app.speech_recognition import listen
from app.speech_synthesis import speak
from app.commands import basic, system, web, weather, joke, news, calculator,greetings

class Assistant:
    def __init__(self):
        self.active = True

    def start(self):
        speak("Hello! How can I assist you today?")
        while self.active:
            command = listen()
            if command:
                response = self.process_command(command)
                speak(response)
            time.sleep(1)

    def process_command(self, command):
        response = "I'm sorry, I don't understand that command."  # Default response

        if "time" in command:
            response = basic.get_time()
        elif "shutdown" in command:
            response = system.shutdown()
        elif "open" in command and "website" in command:
            website = command.split()[-1]
            response = web.open_website(website)
        elif "search" in command:
            search_query = command.replace("search", "").strip()
            response = web.search_web(search_query)
        elif "weather" in command:
            location = command.replace("weather in", "").strip()
            response = weather.get_weather(location)
        elif "joke" in command:
            response = joke.tell_joke()
        elif "news" in command:
            response = news.get_news()
        elif "calculate" in command:
            expression = command.replace("calculate", "").strip()
            response = calculator.calculate(expression)
        elif "hello" in command or "hi" in command:
            response = greetings.greet()
        elif "exit" in command:
            speak("Goodbye!")
            self.active = False
            response = "Goodbye!"

        return response
