import os
from gtts import gTTS
import time

docpath = os.path.expanduser('~/Documents')
os.chdir(docpath)
obj = gTTS(text="Hello, this is your friendly AI setup. What would you like my name to be?", lang='en', tld='ca')
obj.save("asdf.mp3")

time.sleep(5)
os.unlink("asdf.mp3")

# import speech_recognition as sr
# from gtts import gTTS
# import AI
# import os
# from playsound import playsound
# import time
# import Tasks

# # Taken from AI name setup
# os.unlink("C:\\Users/Chris Pollard/PycharmProjects/Leila/welcome.mp3")



# try:
#     taskListenArray = taskListen.split()
# except AttributeError:
#     print("You suck Sadge")
#     for i in taskListenArray:
#         print(taskListenArray[i])

# for i in taskListenArray:
#                 print("taskListenArray at " + i + " value: " + taskListenArray[i])


# os.unlink(os.path.join("C:\\Users/Chris Pollard/Documents/", filename))



# AIname = " "
    # readfile = open('settings.txt')
    # contents = readfile.read()
    # for k in contents:
    #     contents.lower()
    # contentlist = contents.split()
    # AIname = contentlist[1]


# USname = " "
#     readfile = open('settings.txt')
#     contents = readfile.read()
#     for k in contents:
#         contents.lower()
#     contentlist = contents.split()
#     print(contentlist)
#     USname = contentlist[3]


# obj = gTTS(text="Hello, this is your friendly AI setup. What would you like my name to be?", lang='en', tld='ca')
#     obj.save("welcome.mp3")
#     playsound('welcome.mp3')
#     time.sleep(1)
#     try:
#         os.unlink("welcome.mp3")
#     except(FileNotFoundError):
#         pass

# obj = gTTS(text="Welcome back " + USname, lang='en', tld='ca')
#     obj.save("welcome.mp3")
#     playsound('welcome.mp3')
#     time.sleep(1)
#     try:
#         os.unlink("welcome.mp3")
#     except FileNotFoundError:
#         pass

# print("plain taskListen: " + taskListen)

# print(taskListenArray)