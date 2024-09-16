import pyttsx3

engine = pyttsx3.init()


def speak(text):
    """
    This function uses the pyttsx3 library to convert the input text into speech.

    Parameters:
    text (str): The text to be converted into speech.

    Returns:
    None. The function does not return any value. It uses the pyttsx3 engine to speak the input text.
    """
    engine.say(text)
    engine.runAndWait()
