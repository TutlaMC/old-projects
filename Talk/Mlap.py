import pyttsx3
import speech_recognition as sr

listener = sr.Recognizer()
talker = pyttsx3.init()









def talk(text):
    print(text)
    talker.say(text)
    talker.runAndWait()

voices = talker.getProperty("voices")
talker.setProperty("voice", voices[0].id) #can choose voice here

talker.say("Initalizing")
talker.runAndWait()

Lenovo1 = [12, "i7"]


wstuff = []

def checkC():
    with sr.Microphone() as source:
        print("listening...")
        talk("Please tell me if you want i7 or i5")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        talk(command)
        if Lenovo1[1] == command:
           wstuff.Lenovo1
        
        ycb = "You can buy: ", str(wstuff)
        talk(ycb)


def run():
    global laptops
    try:
        with sr.Microphone() as source:
            print("listening...")
            talk("Please tell me how much disk space you need! Please tell in GB's")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = int(command)
            talk(command)
            if Lenovo1[0] == command:
                wstuff.append(Lenovo1)
                checkC()
            else:
                talk("no Laptop found with that much GB's/Diskspace")
    except Exception as e:
        talk(e)

run()
