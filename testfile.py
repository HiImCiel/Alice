import os
import win32api
import win32process
import win32gui
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
import requests
import json

# from gtts import gTTS
# from Tasks import Tasks
# from playsound import playsound

# mytext = 'whale cum back je suis bored'

# obj = gTTS(text=mytext, lang='en', tld='ca')

# obj.save("welcome.mp3")
# os.unlink("./welcome.mp3")
# # os.system("welcome.mp3")

# WM_APPCOMMAND = 0x319

# APPCOMMAND_VOLUME_MAX = 0x0a
# APPCOMMAND_VOLUME_MIN = 0x09

# win32api.SendMessage(win32gui.GetForegroundWindow(), WM_APPCOMMAND, 0x30292, 0x090000)

#
# VK_VOLUME_DOWN = 0xAE
#
# win32api.keybd_event(VK_VOLUME_DOWN, 0, 0, 0)
# win32api.keybd_event(VK_VOLUME_DOWN, 0, 0, 0)
# win32api.keybd_event(VK_VOLUME_DOWN, 0, 0, 0)
# win32api.keybd_event(VK_VOLUME_DOWN, 0, 0, 0)


# sessions = AudioUtilities.GetAllSessions()
# for session in sessions:
#     print(sessions)
#     volume = session._ctl.QueryInterface(ISimpleAudioVolume)
#     print("current volume: " + str(volume.GetMasterVolume()))
#     volume.SetMasterVolume(0.9, None)
#     print("volume.GetMute(): %s" % volume.GetMasterVolume())
url = 'https://api.weather.com/v3/wx/forecast/daily/7day?geocode=33.74,-84.39&format=json&units=e&language=en-US&apiKey=29244201b19a4508a44201b19ad508c1'
headers = {"Accept": "application/json"}

response1 = requests.get(url, headers=headers)

# returns http code
print(response1)

# turns response request into json dict
data = response1.json()
data1 = [data]

# for info in data.items():
#     print(data)
print(list(data.keys()))



# print(data['calendarDayTemperatureMax'])


# let headers = new Headers({
#     "Accept"       : "application/json",
#     "Content-Type" : "application/json",
#     "User-Agent"   : "MY-UA-STRING"
# });

# fetch(url, {
#     method  : 'GET', 
#     headers : headers 
#     // ... etc
# }).then( ...


url1 = 'https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=1523+E+Madison+St+Seattle+WA+98122&benchmark=2020&format=json'
response = requests.get(url1)
print(response)

print(response)