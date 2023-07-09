from pynput.mouse import Controller, Button
from threading import Thread, Condition
from pyautogui import moveTo
from Damage import Damage
from pynput import mouse
from time import sleep

class Powers (Thread):
    def __init__(self, dmg):
        Thread.__init__(self)
        self.__dmg: Damage = dmg
        self.condition = Condition()

    # activates the power corresponding to the x coordinate
    def activePower (self, y):
        mouse = Controller()
        moveTo(1024, y)
        mouse.click(Button.left)
        sleep(.2)

    def run(self):
        while True:
            # put the program in wait for the possibility to click
            with self.condition:
                self.__dmg.insertAction(self)
                self.condition.wait()

            # activate the 9 powers
            self.activePower(294)
            self.activePower(372)
            self.activePower(444)
            self.activePower(555)
            self.activePower(626)
            self.activePower(721)
            self.activePower(823)
            self.activePower(888)
            self.activePower(999)

            # return the mouse to the damage position and wait 10 minutes to reactivate the powers
            moveTo(1470, 630)
            sleep(630)
