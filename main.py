import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "7ec0aa5350ec43c0bf0be752c0c319fc"
# Initialize the speech recognition engine
def speak(text):
  engine.say(text)
  engine.runAndWait()

def aiprocess(command):
  client = OpenAI(
  api_key="sk-proj-xd1XrVXuZ6PzWCHTgrab8fclNWJY6i3Xs9phpbFrDhi6MWoPO98KX2cVHQxwo-8w_SZCKkyXm8T3BlbkFJppVLSSZj_DUR8ppgN6- sijcF6ziKFOJjl0Sq0jMvxDd2YLRcGoO2NkHCMd5mVWAdJxq2b0Q0wA")
  completion = client.chat.completions.create(
  model="o1-preview-2024-09-12",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like alexa and google cloud."},
    {"role": "user", "content": command}
  ]
)
  return(completion.choices[0].message.content)

def processcommand(c):
  print(c)
  if "open google" in c.lower():
    webbrowser.open("https://www.google.com")
  elif "open youtube" in c.lower():
    webbrowser.open("https://www.youtube.com")
  elif "open stack overflow" in c.lower():
    webbrowser.open("https://stackoverflow.com")
  elif "open wikipedia" in c.lower():
    webbrowser.open("https://www.wikipedia.org")
  elif "play music" in c.lower():
    webbrowser.open("https://open.spotify.com")
  elif "play video" in c.lower():
    webbrowser.open("https://www.youtube.com")
  elif "open calculator" in c.lower():
    webbrowser.open("https://www.google.com/search?q=calculator")
  elif "open chrome" in c.lower():
    webbrowser.open("https://www.google.com/chrome/")
  elif "open edge" in c.lower():
    webbrowser.open("https://www.microsoft.com/en-us/edge")
  elif "open notepad" in c.lower():
    webbrowser.open("https://www.microsoft.com/en-us/p/notepad/9msz6")
  elif "open word" in c.lower():
    webbrowser.open("https://www.microsoft.com/en-us/microsoft-365/word")
  elif c.lower().startswith("play"):
    song = c.lower().split(" ")[1]
    link = musiclibrary.music[song]
    webbrowser.open(link)
  elif "news" in c.lower():
    response = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=7ec0aa5350ec43c0bf0be752c0c319fc")
    if response.status_code == 200:
        data = response.json()
        # Extract and display headlines
        articles = data.get('articles', [])
        for article in articles:
          speak(article['title'])
  else:
    # output = aiprocess(c)
    # speak(output)
    speak("Sorry, I didn't understand that. Please try again.")



if __name__ == "__main__":
  # speak(" Heyyy Sir, You are doing great. Just Be consistent and Don't get distracted. Have a Nice Day.")
  speak("Initalizing Jarvis.....  ")
    # obtain audio from the microphone
  while True:
    r = sr.Recognizer()
    # recognize speech using Google
    print("Recognising")
    try:
      with sr.Microphone() as source:
        audio = r.listen(source,timeout=2,phrase_time_limit=1)
        print("Jarvis thinks you said " + r.recognize_google(audio))
        word = r.recognize_google(audio)
        if word.lower() == "ok google": 
           speak("Yes Sir")
           with sr.Microphone() as source:
            print("Jarvis active...")
            audio = r.listen(source)
            word = r.recognize_google(audio)
            processcommand(word)

    except Exception as e:
        print("Google error: {0}".format(e))