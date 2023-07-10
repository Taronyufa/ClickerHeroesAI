from pynput.mouse import Controller, Button
from threading import Thread, Condition
from pyautogui import moveTo
from Damage import Damage
from PIL import ImageGrab
from pynput import mouse
from time import sleep
import pyscreenshot
import pytesseract

class Level (Thread):
    # constructor function
    def __init__(self, dmg):
        Thread.__init__(self)
        self.__dmg: Damage = dmg
        self.condition = Condition()

    # make the program to increase the level
    def levelUp(self) -> None:
        mouse = Controller()
        moveTo(1544, 74)
        mouse.click(Button.left)
        moveTo(1470, 630)

    # make the program to decrease the level
    def levelDown(self) -> None:
        mouse = Controller()
        moveTo(1316, 80)
        mouse.click(Button.left)
        moveTo(1470, 630)

    def run(self) -> None:
        while True:
            # take the picture of the clock and the next level
            pic = ImageGrab.grab(bbox=(1390, 170, 1570, 300))
            img = ImageGrab.grab(bbox=(1518, 96, 1520, 98))

            # if the next level is unlocked, then go there
            if img.getpixel((1, 1)) == (72, 122, 198):
                with self.condition:
                    self.__dmg.insertAction(self)
                    self.condition.wait()
                    self.levelUp()

            # if its in a boss battle wait 32 seconds
            elif pic.getpixel((30, 115)) == (204, 102, 0):
                sleep(32)
                img = ImageGrab.grab(bbox=(1518, 96, 1520, 98))

                with self.condition:
                    self.__dmg.insertAction(self)
                    self.condition.wait()

                # if after the boss battle there's a new level, then go there
                if img.getpixel((1, 1)) == (72, 122, 198):
                    self.levelUp()

                # if theres not a new nevel then u failed the boss battle and u go back to the previous level to increase ur power
                else:
                    self.levelDown()
                    sleep(300)
