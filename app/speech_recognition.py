import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not catch that.")
        except sr.RequestError:
            print("Sorry, the speech service is down.")
    return None
