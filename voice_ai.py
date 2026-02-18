import ollama
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(f"Сакен: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Тыңдап тұрмын...")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio, language="kk-KZ")
        except:
            return ""

user_input = listen()
if user_input:
    print(f"Сен: {user_input}")
    response = ollama.chat(model='saken_ai', messages=[{'role': 'user', 'content': user_input}])
    speak(response['message']['content'])
