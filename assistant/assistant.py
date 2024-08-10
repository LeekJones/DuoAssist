import speech_recognition as sr
import pyttsx3

def listen_command():
    """
    Listens for a voice command from the user and converts it to text.

    Returns:
        str: The recognized command in lowercase, or an empty string if not recognized.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}\n")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not get that")
        return ""
    except sr.RequestError:
        print("Sorry, my speech service is down")
        return ""

def speak(text):
    """
    Converts the given text to speech and plays it back to the user.

    Args:
        text (str): The text to be converted to speech.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
