import speech_recognition as sr
import pyttsx3

def speak(text):
    """Convert text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for audio and convert it to text."""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return ""

def main():
    speak("Hello, I am your voice assistant.")
    
    while True:
        command = listen()
        
        if "exit" in command:
            speak("Goodbye!")
            break
        elif "hello" in command:
            speak("Hello! How can I assist you today?")
        elif "your name" in command:
            speak("I am a simple voice assistant created using Python.")
        elif "how are you" in command:
            speak("I'm just a program, but thank you for asking!")

if __name__ == "__main__":
    main()
