from pyautogui import screenshot, locateOnScreen, moveTo
from pynput.mouse import Controller, Button
from threading import Thread, Condition
from Damage import Damage
from pynput import mouse
import numpy

class PupperFish (Thread):
    def __init__(self, dmg):
        Thread.__init__(self)
        self.__dmg: Damage = dmg
        self.condition = Condition()

    def run(self) -> None:
        mouse = Controller()
        while True:
            # takes a screenshot and locate the pupperfish with a confidence of 65%
            screen = screenshot()
            cords = locateOnScreen("Pictures/Pupperfish.png", confidence=.65)

            # if pupperfish is found then click its center
            if not cords == None:
                with self.condition:
                    self.__dmg.insertAction(self)
                    self.condition.wait()
                moveTo(cords.left + (cords.width // 2), cords.top + (cords.height // 2))
                mouse.click(Button.left)
                moveTo(1470, 600)
