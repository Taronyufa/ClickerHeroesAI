from pynput.mouse import Controller, Button
from threading import Thread, Condition
from pyautogui import moveTo, FAILSAFE
from Damage import Damage
from pynput import mouse
from time import sleep
FAILSAFE = False

class Powers (Thread):
    def __init__(self, dmg):
        Thread.__init__(self)
        self.__dmg: Damage = dmg
        self.condition = Condition()

    # activates the power corresponding to the x coordinate
    def activePower (self, y):
        mouse = Controller()
        with self.condition:
            self.__dmg.insertAction(self)
            self.condition.wait()
        moveTo(1024, y)
        mouse.click(Button.left)
        sleep(.1)

    def run(self) -> None:
        while True:

            # activate the 9 powers
            self.activePower(888)
            self.activePower(294)
            self.activePower(372)
            self.activePower(444)
            self.activePower(555)
            self.activePower(626)
            self.activePower(721)
            self.activePower(999)
            self.activePower(823)

            sleep(630)
