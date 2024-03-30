import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests
from geopy.geocoders import Nominatim
import random
import openai

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

openai.api_key = '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'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Archana, I am Genie, your AI-powered virtual companion. Please tell me how may I help you")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com', 'your_email_password')
    server.sendmail('your_email@gmail.com', to, content)
    server.close()

def get_coordinates(city):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

def get_weather_forecast(api_key, latitude, longitude):
    url = f"https://api.tomorrow.io/v4/timelines?location={latitude},{longitude}&fields=temperature&timesteps=1h&units=metric&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if 'data' in data and 'timelines' in data['data']:
        timeline = data['data']['timelines'][0]
        if 'intervals' in timeline and len(timeline['intervals']) > 0:
            return timeline['intervals'][0]['values']['temperature']
    return "No weather data available"

def play_random_music(music_dir):
    songs = [os.path.join(music_dir, file) for file in os.listdir(music_dir) if file.endswith(".mp3")]
    if songs:
        random_song = random.choice(songs)
        os.startfile(random_song)
    else:
        speak("No MP3 files found in the specified directory.")

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()
        if query == "None":
            continue
        print("Query:", query)

        try:
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            elif 'open google' in query:
                webbrowser.open("google.com")
            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")
            elif 'play music' in query:
                music_dir = 'C:\\Users\\aarch\\Downloads\\TV SONGS'  # Change this to your music directory
                play_random_music(music_dir)
            elif 'the time' in query:
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {str_time}")
            elif 'open code' in query:
                code_path = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code_path)
            elif 'send email' in query:
                try:
                    speak("What should I say?")
                    content = take_command()
                    to = "aarchananichani12@gmail.com"
                    send_email(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend Archana. I am not able to send this email")
            elif 'weather' in query:
                speak("Please wait, fetching the weather forecast.")
                city_name = query.split("weather in ")[-1].strip()
                latitude, longitude = get_coordinates(city_name)
                if latitude is not None and longitude is not None:
                    api_key = "CZxZvceQJ7u1xJc1YARl4Nh3Q4Bj5mBO"
                    weather_forecast = get_weather_forecast(api_key, latitude, longitude)
                    speak(f"The weather forecast for {city_name} is {weather_forecast} degrees Celsius.")
                else:
                    speak("Could not find coordinates for the specified city.")
            elif 'ask genie' in query:
                speak("Sure, what would you like to ask?")
                user_query = take_command()  # Get the user's query
                response = openai.Completion.create(
                    engine="tts-1",
                    prompt=user_query,
                    max_tokens=100
                )
                speak(response.choices[0].text.strip())
            else:
                # Handle other queries here...
                pass
        except Exception as ex:
            print("An error occurred:", ex)
            speak("Sorry, I encountered an error while processing your request.")


