from pynput.mouse import Controller, Button
from threading import Thread, Condition
from pyautogui import moveTo
from Damage import Damage
from PIL import ImageGrab
from pynput import mouse
from time import sleep
import pyscreenshot

class Hero (Thread):
    def __init__(self, dmg):
        Thread.__init__(self)
        self.__dmg: Damage = dmg
        self.condition = Condition()

    def maxHero(self):
        x = 306
        mouse = Controller()
        moveTo(239, 442)
        pic = ImageGrab.grab()

        # keep trying to buy the first level of an hero
        while pic.getpixel((239, 442)) != (230, 167, 9):
            with self.condition:
                self.__dmg.insertAction(self)
                self.condition.wait()
            mouse.click(Button.left)
            pic = ImageGrab.grab()
            sleep(10)

        # keep going until there's no power ups to buy
        while pic.getpixel((x, 442)) != (246, 237, 175):
            moveTo(x, 442)
            pic = ImageGrab.grab()

            # if the power up need a major level keep levelling up
            while pic.getpixel((x + 36, 481)) == (): # add level up red scale
                moveTo(239,442)
                with self.condition:
                    self.__dmg.insertAction(self)
                    self.condition.wait()
                mouse.click(Button.left)
                moveTo(x, 442)
                pic = ImageGrab.grab()
                sleep(10)

            # keep trying to buy the new power up
            while pic.getpixel((x, 442)) == ():  # add unacquired power up color scale
                with self.condition:
                    self.__dmg.insertAction(self)
                    self.condition.wait()
                mouse.click(Button.left)
                pic = ImageGrab.grab()
                sleep(10)

            x += 63

    def scrollHero(self):
        pass

    def run(self) -> None:
        while True:
            self.maxHero()
            self.scrollHero()
