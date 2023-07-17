from pyautogui import screenshot, locateOnScreen, moveTo
from pynput.mouse import Controller, Button
from threading import Thread, Condition
from Damage import Damage
from pynput import mouse
import numpy
import cv2

class PupperFish (Thread):
    def __init__(self, dmg):
        Thread.__init__(self)
        self.__dmg: Damage = dmg
        self.condition = Condition()

    def run(self) -> None:
        mouse = Controller()
        while True:
            screen = screenshot()
            pupperfish = cv2.cvtColor(numpy.array(screen), cv2.COLOR_RGB2BGR)
            cords = locateOnScreen("Pupperfish.png")
            if not cords == None: # se trova il pesce
                with self.condition:
                    self.__dmg.insertAction(self)
                    self.condition.wait()
                moveTo((cords.left + cords.width)//2, (cords.top + cords.heigh)//2)
                mouse.click(Button.left)
                moveTo(1470, 600)
