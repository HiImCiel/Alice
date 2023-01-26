#! python3
import sys
# sys.path.append(r"C:\Users\Chris Pollard\.PyCharmCE2019.1\system\python_stubs\-1329721781")
# sys.path.append(r"C:\Users\Chris Pollard\PycharmProjects\Leila\venv\Lib\site-packages\win32")
# sys.path.append(r"C:\Users\Chris Pollard\PycharmProjects\Leila\venv\Lib\site-packages\win32\lib")
# sys.path.append(r"C:\Users\Chris Pollard\PycharmProjects\Leila\venv\Lib\site-packages\pywin32_system32")
# sys.path.append(r"C:\Users\Chris Pollard\PycharmProjects\Leila\venv\Lib\site-packages\win32\lib")
import win32api
import pyautogui
import time

from clicker import Clicker


pyautogui.FAILSAFE = True
locations = []

state_left = win32api.GetKeyState(0x01)
while True:
    print("1. Add new button location\n"
          "2. Start program")
    response = input()

    if response == "1":
        print("Click on button location")
        while True:
            a = win32api.GetKeyState(0x01)
            if a < 0:
                positionx, positiony = pyautogui.position()
                break

        print("Enter ms delay to click this button again")
        delay = int(input())

        locations.append(Clicker(positionx, positiony, delay))

    if response == "2":
        print("Program Running.... ")

        while True:
            a = win32api.GetKeyState(0x70)
            if a < 0:
                pyautogui.moveTo(0, 0)
            sleepFor = 1000
            ticks = time.time_ns() // 1000000
            for i in locations:
                if i.getNextExecution() < ticks:
                    pyautogui.click(i.locationx, i.locationy)
                    i.lastexecutedticks = ticks
                if i.getTicksUntilNextExecution(ticks) < sleepFor:
                    sleepFor = i.getTicksUntilNextExecution(ticks)

            time.sleep(sleepFor / 1000)


