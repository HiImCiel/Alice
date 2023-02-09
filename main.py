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

    # name setup
    AI.reply("Hello, this is your friendly AI setup. What would you like my name to be?", "welcome.mp3")
    
    # writes AI name to text file
    while True:
        AIname = AI.initialsetup()
        try:
            print("Ok, my name will be " + AIname)
            settings = open('settings.txt', 'w')
            settings.write("Name: " + AIname + '\n')
            settings.close()
            break

        except TypeError:
            print("Could you repeat that?\n")

    print("What is your name?")

    while True:
        userName = AI.initialsetup()
        try:
            print("Nice to meet you  " + userName)
            AI = open('settings.txt', 'a')
            AI.write("User: " + userName + '\n')
            AI.write("Address: unknown")
            break

        except TypeError:
            print("Could you repeat that?\n")

# not a first time user, begins normally
elif 'settings.txt' in os.listdir("./"):

    # looks in text file for name of user
    USname = AI.settings("username")
    
    # greets user by name
    AI.reply("Welcome back " + USname, "welcome.mp3")

# main infinite listening loop, listens for AI name
while True:

    # defines AI name
    AIname = AI.settings("AIname")
    
    # background listening - has phrase time limit of 2s to check for name quicker
    soundSlice = AI.listenbackground()
    soundSliceArray = []
    try:
        soundSliceArray = soundSlice.split()
    except AttributeError:
        pass

    # detects if user says AI's name
    try:
        if AIname in soundSliceArray:
            AI.reply("I hear you", "Ihearyou.mp3")
            print("asdfasdf")
            # active listen for Tasks
            taskListen = AI.listen()
            taskListenArray = []
            taskListenArray = taskListen.split()

            # if second to last word is volume, calls command and sends list to Tasks
            # if len(taskListenArray) != 0 and taskListenArray[len(taskListenArray) - 2] == "volume":
            #     Tasks.command("volume", taskListenArray)
            
            if len(taskListenArray) != 0:
                if "volume" in taskListenArray and "up" or "down" in taskListenArray:
                    Tasks.command("volume", taskListenArray)
                elif "weather" in taskListenArray:
                    # todo
                    Tasks.question("weather")
                else:
                    pass
            else:
                pass
  
    except AttributeError:
        pass
    except TypeError:
        pass

