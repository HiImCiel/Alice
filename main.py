import speech_recognition as sr
from gtts import gTTS
import AI
import os
from playsound import playsound
import time
import Tasks

# check for info file saved in documents
docpath = os.path.expanduser('~/Documents')
os.chdir(docpath)

# begins initial name set-up if first time using
if 'settings.txt' not in os.listdir("./"):

    # print("Hello, this is your friendly AI setup. What would you like my name to be?")
    obj = gTTS(text="Hello, this is your friendly AI setup. What would you like my name to be?", lang='en', tld='ca')
    obj.save("welcome.mp3")
    playsound('welcome.mp3')
    time.sleep(1)
    os.unlink("C:\\Users/Chris Pollard/PycharmProjects/Leila/welcome.mp3")

    x = 1
    while x != 2:
        AIname = AI.initialsetup()
        try:
            print("Ok, my name will be " + AIname)
            settings = open('settings.txt', 'w')
            settings.write("Name: " + AIname + '\n')
            settings.close()
            x = 2

        except TypeError:
            print("Could you repeat that?\n")

    print("What is your name?")

    x = 1
    while x != 2:
        userName = AI.initialsetup()
        try:
            print("Nice to meet you  " + userName)
            AI = open('settings.txt', 'a')
            AI.write("User: " + userName + '\n')
            x = 2

        except TypeError:
            print("Could you repeat that?\n")

# not a first time user, begins normally
elif 'settings.txt' in os.listdir("./"):

    # looks in txt file for name of user
    USname = " "
    readfile = open('settings.txt')
    contents = readfile.read()
    for k in contents:
        contents.lower()
    contentlist = contents.split()
    print(contentlist)
    USname = contentlist[3]

    # greets user by name
    obj = gTTS(text="Welcome back " + USname, lang='en', tld='ca')
    obj.save("welcome.mp3")
    playsound('welcome.mp3')
    time.sleep(1)
    try:
        os.unlink("C:\\Users/Chris Pollard/PycharmProjects/Leila/welcome.mp3")
    except FileNotFoundError:
        pass

# main listening loop, listens for AI name
while True:

    # defines AI name
    AIname = " "
    readfile = open('settings.txt')
    contents = readfile.read()
    for k in contents:
        contents.lower()
    contentlist = contents.split()
    AIname = contentlist[1]

    # background listening
    v = AI.listenbackground()
    vw = []
    try:
        vw = v.split()
    except AttributeError:
        pass

    # detects if user says AI's name
    try:
            if AIname in vw:
                AI.reply("I hear you", "Ihearyou.mp3")
            
                # active listen for Tasks
                w = AI.listen()
                ws = []
                try:
                    ws = w.split()
                except AttributeError:
                    print("You suck Sadge")
                    print(w)
                    for i in ws:
                        print(ws[i])

                # if second to last word is volume, calls command and sends list to Tasks
                if len(ws) != 0 and ws[len(ws) - 2] == "volume":
                    Tasks.command("volume", ws)
    except AttributeError:
        pass
    except TypeError:
        pass

