import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import time, os


# obtain audio from the microphone
r = sr.Recognizer()
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


def initialsetup():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        voice = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        v = r.recognize_google(voice)
        return v
    except sr.UnknownValueError:
        print("Pardon?")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        voice = r.listen(source, phrase_time_limit=6)
    # recognize speech using Google Speech Recognition
    try:
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        v = r.recognize_google(voice)
        return v
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def listenbackground():
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        voice = r.listen(source, phrase_time_limit=2)

    # recognize speech using Google Speech Recognition
    try:
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        v = r.recognize_google(voice)
        return v
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def reply(message, filename):
    obj = gTTS(text= message, lang='en', tld='ca')
    obj.save(filename)
    playsound(filename)

    try:
        os.unlink(os.path.join("C:\\Users/Chris Pollard/Documents/", filename))
    except FileNotFoundError:
        print("error in unlinking file")
