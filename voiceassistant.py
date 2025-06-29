import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listner =aa.Recognizer()

machine = pyttsx3.init()
def talk(text):

    machine.say(text)
    machine.runAndWait()


def input_instruction():

    global instruction
    try:

        with aa.Microphone() as origin:

            print("listening....")
            speech= listner.listen(origin)
            instruction = listner.recognize_google(speech)
            instruction= instruction.lower()
            if 'bolt' in instruction:
                instruction = instruction.replace('bolt',' ')
                print(instruction)
            
        
           
    except:
        pass
    return instruction

def play_bolt():
    instruction= input_instruction()
    print(instruction)
    if "play" in instruction:

        song=instruction.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk("current time is"+time)
    elif 'date' in instruction:
        date= datetime.datetime.now().strftime('%d /%m /%y')
        talk("Today is"+ date)
    elif "how" in instruction:
        talk("i am fine ,how are you sir")

    elif "what is your name" in instruction:
         talk("i am bolt,what can i do for you sir")
    elif " better assistant" in instruction:
         talk("it is up to you")
    elif "who made you" in instruction or "who created you" in instruction: 
        talk("I have been created by Aritra.")
    elif 'joke' in instruction:
        talk(pyjokes.get_joke())
    elif 'who' in instruction:
        human = instruction.replace("who is"," ")
        info=wikipedia.summary(human,1)
        print(info)
        talk(info)
    
        
    else:
        talk("please repeat")
play_bolt()