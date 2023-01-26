#! python3
import win32api
import pyautogui
import time


class Clicker:

    def __init__(self, locationx, locationy, delay):
        self.locationx = locationx
        self.locationy = locationy
        self.delay = delay
        self.lastexecutedticks = 0

    def getNextExecution(self):
        return self.lastexecutedticks + self.delay

    def getTicksUntilNextExecution(self, ticks):
        return self.getNextExecution() - ticks

