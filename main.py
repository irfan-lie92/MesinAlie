import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os
from googlesearch import search

print("Alie")
MASTER = "irfan"
mendengarkan = sr.Recognizer()
engine = pyttsx3.init("sapi5")
# kecepatan baca
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
# jenis suara [0] male [1] female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        talk("Wilujeung Enjing" + MASTER)
    elif 12 <= hour < 18:
        talk("Wilujeung Siang" + MASTER)
    else:
        talk("Wilujeung Sonten" + MASTER)

def take_command():
    command = ""  # Inisialisasi variabel command di awal fungsi
    try:
        with sr.Microphone() as source:
            print("mendengarkan")
            voice = mendengarkan.listen(source)
            command = mendengarkan.recognize_google(voice, language='id-ID')
            command = command.lower()
            if "Alie" in command:
                print(command)
                command = command.replace("Alie", "")
                talk(command)
    except:
        pass

    return command

def run_Alie():
    command = take_command()
    if 'play' in command:
        song = command.replace("play", "")
        talk("playing" + song)
        print("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("time now is " + time)
    elif "wikipedia" in command:
        src = command.replace("wikipedia", "")
        info = wikipedia.summary(src, sentences=1)
        talk("searching wikipedia")
        print(info)
        talk(info)
    elif 'cari' in command:
        query = command.replace("cari", "")
        talk("Mohon Tunggu, saya Cari di Google")
        print("Cari di Google:", query)
        pywhatkit.search(query)
    elif 'tutup' in command:
        tutup = 'keluar.mp3'
        os.system(f'start {tutup}')
        print('Sampai jumpa lagi, terimakasih..')
        exit()
    else:
        talk("Instruksi tidak dikenali")
        print(command)

wishMe()

while True:
    MASTER = "irfan"
    mendengarkan = sr.Recognizer()
    engine = pyttsx3.init("sapi5")
    # kecepatan baca
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    # jenis suara [0] male [1] female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    talk("Simkuring Alie, can i help you again?")
    run_Alie()
