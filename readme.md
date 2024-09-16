# Python Voice Assistant

A Python-based voice assistant designed to perform a variety of tasks such as telling the time, fetching the weather, telling jokes, and more. This assistant is built using Python 3.9.10 and is developed in Visual Studio Code.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Interconnected Code](#interconnected-code)
- [Setup and Installation](#setup-and-installation)
- [Running the Project](#running-the-project)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project is a simple yet powerful voice assistant that can respond to voice commands, perform tasks such as fetching the current weather, telling jokes, performing calculations, and more. The assistant listens to your voice, processes the command, and then provides a response using text-to-speech synthesis.

## Features

- **Time Reporting**: Get the current time.
- **Weather Updates**: Fetch the current weather for any specified location.
- **Jokes**: Get a random joke.
- **News Headlines**: Fetch the top 5 news headlines.
- **System Commands**: Perform basic system commands such as shutting down the computer.
- **Web Commands**: Open websites and perform web searches.
- **Calculations**: Perform basic arithmetic calculations.
- **Greetings**: Greet the user based on the time of day.

## Project Structure

```
voice-assistant/
│
├── app/
│   ├── __init__.py
│   ├── assistant.py
│   ├── speech_recognition.py
│   ├── speech_synthesis.py
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── basic.py
│   │   ├── system.py
│   │   ├── web.py
│   │   ├── weather.py
│   │   ├── joke.py
│   │   ├── news.py
│   │   ├── calculator.py
│   │   ├── greeting.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── logger.py
│   │   ├── helper.py
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── nlp.py
│   │   ├── intent_recognition.py
│   │   ├── response_generation.py
│
└── main.py
```

## How It Works

### Logical Flow

1. **Initialization**: The assistant is initialized and starts in an active state.
2. **Listening**: The assistant continuously listens for voice commands using the microphone.
3. **Processing**: Once a command is detected, it is passed through the `process_command` function to determine the correct action.
4. **Response Generation**: Based on the command, the appropriate module is called to perform the task (e.g., fetching the weather, performing a calculation).
5. **Speaking**: The result of the task is spoken back to the user using text-to-speech synthesis.

### Example Workflow

1. **User Command**: The user says, "What is the weather in New York?"
2. **Recognition**: The assistant uses speech recognition to convert the command to text.
3. **Processing**: The command is recognized as a weather query.
4. **Action**: The assistant fetches the weather data for New York.
5. **Response**: The assistant replies, "The weather in New York is currently cloudy with a temperature of 15°C."

## Interconnected Code

- **`main.py`**: The entry point of the application. It initializes the `Assistant` class and starts the assistant.
- **`app/assistant.py`**: Contains the main logic for the assistant, including listening for commands, processing them, and triggering responses.
- **`app/speech_recognition.py`**: Handles converting spoken commands into text using the `speech_recognition` library.
- **`app/speech_synthesis.py`**: Handles converting text responses into speech using the `pyttsx3` library.
- **`app/commands/`**: Contains individual modules for handling specific commands (e.g., `weather.py`, `joke.py`, etc.).
- **`app/utils/`**: Provides utility functions and configurations that support the main logic.
- **`app/ai/`**: Contains modules for natural language processing and intent recognition, which help the assistant understand and respond to more complex queries.

## Setup and Installation

### Prerequisites

- Python 3.9.10
- Visual Studio Code (or any other Python IDE)
- An internet connection for fetching weather data, news, etc.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/voice-assistant.git
   cd voice-assistant
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Add API keys**:
   - Replace placeholders in `weather.py` and `news.py` with your actual API keys.

## Running the Project

1. **Start the assistant**:
   ```bash
   python main.py
   ```

2. **Give voice commands**:
   - Speak commands like "What is the time?", "Tell me a joke", "Search for Python tutorials", etc.
   - The assistant will listen to your command, process it, and respond accordingly.

## Dependencies

The following Python libraries are used in this project:

- `speech_recognition`: For converting spoken commands into text.
- `pyttsx3`: For text-to-speech synthesis.
- `requests`: For making HTTP requests to APIs (e.g., weather, news).
- `logging`: For logging information, errors, and debugging.

These dependencies can be installed using:

```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
