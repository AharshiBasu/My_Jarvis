import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import os
import subprocess
import requests
from datetime import datetime


recognizer = sr.Recognizer()
engine = pyttsx3.init()

response = requests.get("https://ipinfo.io/json")
data = response.json()

latitude, longitude = map(float, data["loc"].split(","))

# for weather
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
)

response = requests.get(url)
data = response.json()

current = data["current"]
now = datetime.now()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
     if "date" in c.lower():
           speak(f"Date       : {now.strftime("%m-%d-%Y")}")
     elif "time" in c.lower():
           speak(f"Time       : {now.strftime("%I:%M:%S %p")}")
     elif "weather report" in c.lower():
           speak(f"Temperature: {current["temperature_2m"], "°C"}")
           speak(f"Humidity   : {current["relative_humidity_2m"], "%"}")
           speak(f"Wind Speed : {current["wind_speed_10m"], "kilometer per hour"}")
     elif "open google" in c.lower():
          webbrowser.open("https://google.com")
          speak("opening google")
     elif "open facebook" in c.lower():
          webbrowser.open("https://facebook.com")
          speak("opening facebook")
     elif "open youtube" in c.lower():
            webbrowser.open("https://youtube.com")
            speak("opening you tube")
     elif "open linkedin" in c.lower():
            webbrowser.open("https://linkedin.com")
            speak("opening linkedin")
     elif "open github" in c.lower():
            webbrowser.open("https://github.com")
            speak("opening github")
     elif "open instagram" in c.lower():
            webbrowser.open("https://instagram.com")
            speak("opening instagram")
     elif "open spotify" in c.lower():
            webbrowser.open("https://spotify.com")
            speak("opening spotify")
     elif "open amazon" in c.lower():
            webbrowser.open("https://www.amazon.in/?ref=icp_country_us_t1")
            speak("opening amazon")
     elif "open classroom" in c.lower():
            webbrowser.open("https://classroom.google.com/h")
            speak("opening google classroom")
     elif "open e mail" in c.lower():
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            speak("opening G mail")
     elif c.lower().startswith("play"):
          Song = c.lower().split(" ")[1]
          link = musicLibrary.Music[Song]
          webbrowser.open(link)
          speak("plaing...")
     elif "open arduino ide" in c.lower():
              os.startfile("C:\\Users\\amitb\\AppData\\Local\\Programs\\Arduino IDE\\Arduino IDE.exe")
              speak("opening Arduino I D E")
     elif "open blue j" in c.lower():
              os.startfile("C:\\Users\\amitb\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\BlueJ\\BlueJ.lnk")
              speak("opening blue J")
     elif "open calculator" in c.lower():
              os.startfile("Calc.exe")
              speak("opening calculator")
     elif "open powerpoint" in c.lower():
              os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk")
              speak("opening power point")
     elif "open notepad" in c.lower():
               os.startfile("NotePad.exe")
               speak("opening note pad")
     elif "open excel" in c.lower():
              os.startfile("Excel.exe")
              speak("opening excel")
     elif "open word" in c.lower():
              os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
              speak("opening microsoft word")
     elif "open whatsapp" in c.lower():
              os.startfile("whatsapp:")
              speak("opening whatsapp")
     elif "open powershell" in c.lower():
           os.system("start cmd")
           speak("opening c m d")
     elif "shutdown" in c.lower():
           speak("shutting down...")
           os.system("shutdown /s /t 0")
     elif "restart" in c.lower():
           speak("restarting...")
           os.system("shutdown /r /t 0")
     elif "sleep" in c.lower():
           speak("sleeping")
           os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
     elif "lock" in c.lower():
           speak("locking...")
           os.system("rundll32.exe user32.dll,LockWorkStation")
     elif "close all" in c.lower():
              speak("closing everything except V S code")
              powershell = r'''
        Get-Process | Where-Object {
              $_.MainWindowHandle -ne 0 -and
              $_.ProcessName -notin @("Code", "python", "pythonw")
              } | ForEach-Object {
              $_.CloseMainWindow() | Out-Null
              }
              '''
              subprocess.run(["powershell", "-NoProfile", "-Command", powershell])
     else:
           speak("sorry could not get your command!!")



if __name__ == "__main__":
    speak("Initializing Jarvis....")

    while True:
        # listen for the wake word jarvis
        # obtain audio from microphone
        r = sr.Recognizer()
        
        print("recognising...")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower() == "good morining" ):
                  speak("Good morning sir!! How may I help you")
                  
            elif(word.lower() == "jarvis"):
                 speak("Ya")
                 # Listen for command
                 with sr.Microphone() as source:
                     print("Jarvis Active...")
                     audio = r.listen(source, timeout=2, phrase_time_limit=3)
                     command = r.recognize_google(audio)

                     processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
    


