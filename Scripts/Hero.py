from pyautogui import screenshot, locateOnScreen, moveTo
from pynput.mouse import Controller, Button
from threading import Thread, Condition
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

    # chech if the red color that the program found is actually red
    def colorInRange(self, clr1):
        num1 = abs(clr1[0] - 245)
        num2 = abs(clr1[1] - 50)
        num3 = abs(clr1[2] - 1)
        return (num1 + num2 + num3) < 30

    # check if in a pic there's at least a pixel with the given color
    def anyColor(self, pic, color):
        for i in range (47):
            for j in range (47):
                if pic.getpixel((i, j)) == color:
                    return True
        return False

    # completely max out an hero
    def maxHero(self):
        mouse = Controller()
        pic = ImageGrab.grab()
        button = screenshot()
        button = locateOnScreen('Pictures/lvlButton.png', confidence = .65)
        i, x, y = 0, button.left + (button.width // 2), button.top + (button.height // 2)

        # keep trying to buy the first level of an hero
        while pic.getpixel((x + 150, y + 84)) == (245, 233, 170):
            moveTo(x, y)
            with self.condition:
                self.__dmg.insertAction(self)
                self.condition.wait()
            mouse.click(Button.left)
            pic = ImageGrab.grab()
            moveTo(1470, 630)
            sleep(10)

        # keep going until there's no power ups to buy
        while self.anyColor(ImageGrab.grab(bbox=(x + 150 + (61 * i), y + 37, x + 197 + (61 * i), y + 84)), (10, 10, 10)):
            moveTo(x + 150 + (61 * i), y + 84)
            pic = ImageGrab.grab()

            # if the power up need a major level keep levelling up
            while self.colorInRange(pic.getpixel((x + 232 + (61 * i), y + 111))):
                moveTo(x, y)
                with self.condition:
                    self.__dmg.insertAction(self)
                    self.condition.wait()
                mouse.click(Button.left)
                moveTo(x + 150 + (61 * i), y + 84)
                pic = ImageGrab.grab()
                moveTo(1470, 630)
                sleep(10)

            # keep trying to buy the new power up
            while self.anyColor(ImageGrab.grab(bbox=(x + 150 + (61 * i), y + 37, x + 197 + (61 * i), y + 84)), (10, 10, 10)):
                moveTo(x + 150 + (61 * i), y + 84)
                with self.condition:
                    self.__dmg.insertAction(self)
                    self.condition.wait()
                mouse.click(Button.left)
                pic = ImageGrab.grab()
                moveTo(1470, 630)
                sleep(10)

            i += 1

    # scroll down to the next hero
    def scrollHero(self):
        mouse = Controller()
        moveTo(930, 1045)
        for i in range (2):
            sleep(.7)
            mouse.click(Button.left)
        moveTo(1470, 630)

    def run(self) -> None:
        while True:
            sleep(.6)
            self.maxHero()
            self.scrollHero()
