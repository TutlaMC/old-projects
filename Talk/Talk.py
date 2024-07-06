import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import pyjokes
import pywhatkit
import pyaudio
import random
import time
#My files
import riddles
import wordAssociation
import words
import entertainment





listener = sr.Recognizer()
talker = pyttsx3.init()

def talk(text):
    print(text)
    talker.say(text)
    talker.runAndWait()

voices = talker.getProperty("voices")
talker.setProperty("voice", voices[0].id) #can choose voice here

talker.say("Talk Is ready!")
talker.runAndWait()

#details
version = 1.0

#####################


#####games######

#rps
things=["rock","paper","scissors"]
cmpnts = 0
uspnts = 0

def playrps():
    with sr.Microphone() as source:
        global cmpnts
        global uspnts
        talk("Tell rock paper or scissors!")
        talk("just know I will tell all the points after the game!")
        print("listening")
        voice = listener.listen(source)
        pt = listener.recognize_google(voice)
        pt = pt.lower()
        cmpt = random.choice(things)
        if "rock" in pt:
            if cmpt == "rock":
                talk("I choose: "+cmpt)
                talk("Thats a Tie!")
                with sr.Microphone() as source:
                    talk("Wanna play again, i will be counting points")
                    print("listening")
                    voice = listener.listen(source)
                    ysn = listener.recognize_google(voice)
                    ysn = ysn.lower()
                    if "yes" in ysn:
                        global cmpnts
                        global uspnts
                        cmpnts += 1
                        uspnts += 1
                        talk("Both get a point!")
                        playrps()
                    else:
                        talk("You have: "+str(uspnts)+" points")
                        talk("Computer has: "+str(cmpnts)+" points")
                        if cmpnts > uspnts:
                            talk("I win!")
                        elif cmpnts < uspnts:
                            talk("You win!")
            if cmpt == "paper":
                talk("I choose: "+cmpt)
                talk("Computer gets a point!")
                with sr.Microphone() as source:
                    talk("Wanna play again, i will be counting points")
                    print("listening")
                    voice = listener.listen(source)
                    ysn = listener.recognize_google(voice)
                    ysn = ysn.lower()
                    
                    if "yes" in ysn:
                        cmpnts += 1
                        talk("I get a point!")
                        playrps()
                    else:
                        talk("You have: "+str(uspnts)+" points")
                        talk("Computer has: "+str(cmpnts)+" points")
                        if cmpnts > uspnts:
                            talk("I win!")
                        elif cmpnts < uspnts:
                            talk("You win!")
            if cmpt == "scissors":
                talk("I choose: "+cmpt)
                talk("You get a point!")
                with sr.Microphone() as source:
                    talk("Wanna play again, i will be counting points")
                    print("listening")
                    voice = listener.listen(source)
                    ysn = listener.recognize_google(voice)
                    ysn = ysn.lower()
                    
                    if "yes" in ysn:
                        uspnts += 1
                        talk("I get a point!")
                        playrps()
                    else:
                        talk("You have: "+str(uspnts)+" points")
                        talk("Computer has: "+str(cmpnts)+" points")
                        if cmpnts > uspnts:
                            talk("I win!")
                        elif cmpnts < uspnts:
                            talk("You win!")


        if "paper" in pt:
            if cmpt == "paper":
                talk("I choose: "+cmpt)
                talk("Thats a Tie!")
                with sr.Microphone() as source:
                    talk("Wanna play again, i will be counting points")
                    print("listening")
                    voice = listener.listen(source)
                    ysn = listener.recognize_google(voice)
                    ysn = ysn.lower()
                    
                    if "yes" in ysn:
                        cmpnts += 1
                        uspnts += 1
                        talk("Both get a point!")
                        playrps()
                    else:
                        talk("You have: "+str(uspnts)+" points")
                        talk("Computer has: "+str(cmpnts)+" points")
                        if cmpnts > uspnts:
                            talk("I win!")
                        elif cmpnts < uspnts:
                            talk("You win!")
            if cmpt == "scissors":
                talk("I choose: "+cmpt)
                talk("Computer gets a point!")
                with sr.Microphone() as source:
                    talk("Wanna play again, i will be counting points")
                    print("listening")
                    voice = listener.listen(source)
                    ysn = listener.recognize_google(voice)
                    ysn = ysn.lower()
                    
                    if "yes" in ysn:
                        cmpnts += 1
                        talk("I get a point!")
                        playrps()
                    else:
                        talk("You have: "+str(uspnts)+" points")
                        talk("Computer has: "+str(cmpnts)+" points")
                        if cmpnts > uspnts:
                            talk("I win!")
                        elif cmpnts < uspnts:
                            talk("You win!")
            if cmpt == "rock":
                talk("I choose: "+cmpt)
                talk("You get a point!")
                with sr.Microphone() as source:
                    talk("Wanna play again, i will be counting points")
                    print("listening")
                    voice = listener.listen(source)
                    ysn = listener.recognize_google(voice)
                    ysn = ysn.lower()
                    
                    if "yes" in ysn:
                        uspnts += 1
                        talk("I get a point!")
                        playrps()
                    else:
                        talk("You have: "+str(uspnts)+" points")
                        talk("Computer has: "+str(cmpnts)+" points")
                        if cmpnts > uspnts:
                            talk("I win!")
                        elif cmpnts < uspnts:
                            talk("You win!")
                            
            

        if "scissors" in pt:
            if cmpt == "scissors":
                talk("I choose: "+cmpt)
                talk("Thats a Tie!")
                with sr.Microphone() as source:
                    talk("Wanna play again, i will be counting points")
                    print("listening")
                    voice = listener.listen(source)
                    ysn = listener.recognize_google(voice)
                    ysn = ysn.lower()
                    
                    if "yes" in ysn:
                        cmpnts += 1
                        uspnts += 1
                        talk("Both get a point!")
                        playrps()
                    else:
                        talk("You have: "+str(uspnts)+" points")
                        talk("Computer has: "+str(cmpnts)+" points")
                        if cmpnts > uspnts:
                            talk("I win!")
                        elif cmpnts < uspnts:
                            talk("You win!")
            if cmpt == "rock":
                talk("I choose: "+cmpt)
                talk("Computer gets a point!")
                with sr.Microphone() as source:
                    talk("Wanna play again, i will be counting points")
                    print("listening")
                    voice = listener.listen(source)
                    ysn = listener.recognize_google(voice)
                    ysn = ysn.lower()
                    
                    if "yes" in ysn:
                        cmpnts += 1
                        talk("I get a point!")
                        playrps()
                    else:
                        talk("You have: "+str(uspnts)+" points")
                        talk("Computer has: "+str(cmpnts)+" points")
                        if cmpnts > uspnts:
                            talk("I win!")
                        elif cmpnts < uspnts:
                            talk("You win!")
            if cmpt == "paper":
                talk("I choose: "+cmpt)
                talk("You get a point!")
                with sr.Microphone() as source:
                    talk("Wanna play again, i will be counting points")
                    print("listening")
                    voice = listener.listen(source)
                    ysn = listener.recognize_google(voice)
                    ysn = ysn.lower()
                    
                    if "yes" in ysn:
                        uspnts += 1
                        talk("I get a point!")
                        playrps()
                    else:
                        talk("You have: "+str(uspnts)+" points")
                        talk("Computer has: "+str(cmpnts)+" points")
                        if cmpnts > uspnts:
                            talk("I win!")
                        elif cmpnts < uspnts:
                            talk("You win!")  


######################################
#riddles

def askriddle():
        talk("i will wait for 10 seconds then i will tell the answer!!!")
        questionp = random.choice(riddles.riddles)
        question = [questionp[0]]
        answer = questionp[1]
        talk(question)
        time.sleep(10)
        talk(answer)
################

#################### word association

def wrdAs():
    talk("First i will ask you. then you will ask me")
    talk("I will wait 3 seconds after every word")

    talk(random.choice(wordAssociation.words))
    with sr.Microphone() as source:
        talk("listening")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        talk(command)
        time.sleep(3)
    talk("now you tell me")
    with sr.Microphone() as source:
        talk("listening")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        talk(command)
        talk(random.choice(wordAssociation.words))
        time.sleep(1)

def mathing(command):
    try:
       talk(eval(command))
    except Exception:
        talk("please do not say 'how much is' 'is equal to' in your command. rather say the question without words only numbers and symbols")

#######################


def work():
    global version
    global talker
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "who made you" in command:
                talk(command)
                talk("Tutla made me!")
            elif "hello" in command:
                talk(command)
                talk("Hello")
            elif "version" in command:
                talk(command)
                talk("Version: " +str(version))
            elif "youtube" in command:
                talk(command)
                vid = command.replace("play", "")
                talk("playing: " +vid)
                pywhatkit.playonyt(vid)
            elif "time" in command:
                talk(command)
                time = datetime.datetime.now().strftime("%I:%M:%S %p")
                talk("Current time is: " +time)
            elif "month" in command:
                talk(command)
                time = datetime.datetime.now().strftime("%M")
                talk(time)
            elif "date" in command:
                talk(command)
                time = datetime.datetime.now().strftime("%Y-%m-%d")
                talk(time)
            elif "week" in command:
                talk(command)
                time = datetime.datetime.now().strftime("%W")
                talk(time)
            elif "wikipedia" in command:
                talk(command)
                tosearch = command.replace("wikipedia", "")
                info = wikipedia.summary(tosearch, 3)
                print(info)
                talk(info) 
            elif "who is " in command:
                talk(command)
                tosearch = command.replace("who is ", "")
                info = wikipedia.summary(tosearch, 1)
                talk(info)
            elif "joke" in command:
                talk(command)
                joke = pyjokes.get_joke(language="en", category="all")
                talk(joke)
            elif "what is" in command:
                talk(command)
                text = command.replace("what is", "")
                ans = wikipedia.summary(text, 1)
                talk(ans)
            elif "rock paper scissors" in command:
                talk(command)
                playrps()
            elif "riddle" in command:
                talk(command)
                askriddle()
        
            elif "bye" in command:
                talk(command)
                talk("BBye")
                exit()
            
            elif "who are you" in command:
                talk(command)
                talk("I am mr. Talk")
            elif "what is " in command:
                talk(command)
                tosearch = command.replace("what is ", "")
                info = wikipedia.summary(tosearch, 1)
                talk(info)
            elif "are you a turkey" in command:
                talk(command)
                talk("No i am a chicken")
                talk("turkeyss stink")
            elif "word game" in command:
                talk(command)
                wrdAs()

            elif "funny words" in command:
                talk(command)
                talk(random.choice(words.funnywords))

            elif "funny word" in command:
                talk(command)
                talk(random.choice(words.funnywords))

            elif "sing" in command:
                talk(command)
                talk(random.choice(entertainment.songs))

            elif "story" in command:
                talk(command)
                talk(random.choice(entertainment.storys))
            elif "pop it" in command:
                talk(command)
                talk("pop you")

            elif "do you go to school" in command:
                talk(command)
                talk("To Tutla school")

            elif "i hate you" in command:
                talk("i hate you aswell")

            elif "can you do something" in command:
                talk(command)
                talk("what something?")
            
            else:
                talk(command)
                talk("I Did not understand, or that command is not taught in my school!!!!!")
    except Exception as e:
        print(e)


while True:
    work()
    time.sleep(1)