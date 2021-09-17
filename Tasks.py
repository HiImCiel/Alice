import speech_recognition as sr
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from gtts import gTTS
import AI
import os
from playsound import playsound
import time


class Tasks:

    def __init__(self, name, v):
        self.name = name
        self.v = v
        print(name)


def conversation():
    print("as")


def question(text):

    if text == "weather":
        print("asdf")


def command(name, v):

    # volume commands (up or donw)
    if name == "volume":
        if v[len(v) - 1] == "down":
            print("Down")
            AI.reply("Sure, how much lower do you want it?", "VolumeOption.mp3")

            v = AI.listen()
            vs = v[:2]
            value = float(vs)
            AI.reply(("Sure, I'll turn it down" + v), "volumereply.mp3")

            # magic shit for actual volume control
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                print("Current Volume: " + str(volume.GetMasterVolume()))
                vol = (float(volume.GetMasterVolume()))
                newvol = vol * (1 - (value/100))
                print("New Volume: " + str(newvol))
                volume.SetMasterVolume(newvol, None)
            time.sleep(1)

        if v[len(v) - 1] == "up":
            print("Up")
            AI.reply("Sure, how much higher do you want it?", "VolumeOption.mp3")

            v = AI.listen()
            vs = v[:2]
            value = float(vs)
            AI.reply(("Sure, I'll turn it up" + v), "volumereply.mp3")

            # magic shit for actual volume control
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                print("Current Volume: " + str(volume.GetMasterVolume()))
                vol = (float(volume.GetMasterVolume()))
                newvol = vol * (1 + (value / 100))
                print("New Volume: " + str(newvol))
                volume.SetMasterVolume(newvol, None)
            time.sleep(1)


