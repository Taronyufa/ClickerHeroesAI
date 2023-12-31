from pyautogui import screenshot, locateOnScreen, moveTo, FAILSAFE
from pynput.mouse import Controller, Button
from threading import Thread, Condition
from Damage import Damage
from PIL import ImageGrab
from pynput import mouse
from time import sleep
import pyscreenshot
FAILSAFE = False

class Hero (Thread):
    def __init__(self, dmg):
        Thread.__init__(self)
        self.__dmg: Damage = dmg
        self.condition = Condition()

    # chech if the red color that the program found is in a given range
    def colorInRange(self, clr1, clr2):
        num1 = abs(clr1[0] - clr2[0])
        num2 = abs(clr1[1] - clr2[1])
        num3 = abs(clr1[2] - clr2[2])
        return (num1 + num2 + num3) < 30

    # check if in a pic there's at least a pixel with the given color
    def anyColor(self, pic, color):
        for i in range (47):
            for j in range (47):
                if pic.getpixel((i, j)) == color:
                    return True
        return False

    def anyColorInRange(self, pic, color):
        for i in range (47):
            for j in range (47):
                if self.colorInRange(pic.getpixel((i,j)), color):
                    return True
        return False

    # completely max out an hero
    def maxHero(self):
        mouse = Controller()
        pic = ImageGrab.grab()
        button = None

        # keep trying to find the lvl up button
        while button == None:
            button = screenshot()
            button = locateOnScreen('Pictures/lvlButton.png', confidence = .50)

        i, x, y = 0, button.left + (button.width // 2), button.top + (button.height // 2)

        # keep trying to buy the first level of an hero
        while self.colorInRange(pic.getpixel((x + 150, y + 84)), (200, 233, 170)) or self.colorInRange(pic.getpixel((x + 150, y + 84)), (255, 255, 89)):
            with self.condition:
                self.__dmg.insertAction(self)
                self.condition.wait()
            moveTo(x, y)
            mouse.click(Button.left)
            pic = ImageGrab.grab()
            sleep(1)

        # keep going until there's no power ups to buy
        while self.anyColor(ImageGrab.grab(bbox=(x + 150 + (61 * i), y + 37, x + 197 + (61 * i), y + 84)), (10, 10, 10)):
            with self.condition:
                self.__dmg.insertAction(self)
                self.condition.wait()
            moveTo(x + 150 + (61 * i), y + 84)
            pic = ImageGrab.grab()

            # if the power up need a major level keep leveling up
            while self.anyColorInRange(ImageGrab.grab(bbox=(x + 232 - 20 + (61 * i), y + 111 - 20, x + 232 + 27 + (61 * i), y + 111 + 27)), (250, 51, 1)):
                with self.condition:
                    self.__dmg.insertAction(self)
                    self.condition.wait()
                moveTo(x, y)
                mouse.click(Button.left)
                moveTo(x + 150 + (61 * i), y + 84)
                pic = ImageGrab.grab()
                sleep(1)

            # keep trying to buy the new power up
            while not self.anyColor(ImageGrab.grab(bbox=(x + 150 + (61 * i), y + 37, x + 197 + (61 * i), y + 84)), (71, 198, 17)):
                with self.condition:
                    self.__dmg.insertAction(self)
                    self.condition.wait()
                moveTo(x + 150 + (61 * i), y + 84)
                mouse.click(Button.left)
                pic = ImageGrab.grab()
                sleep(1)

            i += 1

        # keep leveling up the current hero until it can afford the next hero
        pic = ImageGrab.grab()
        while self.colorInRange(pic.getpixel((x, y + 170)), (84, 110, 127)):
            with self.condition:
                self.__dmg.insertAction(self)
                self.condition.wait()
            moveTo(x, y)
            mouse.click(Button.left)
            sleep(1)

    # scroll down to the next hero
    def scrollHero(self):
        mouse = Controller()
        with self.condition:
            self.__dmg.insertAction(self)
            self.condition.wait()
        moveTo(930, 1045)
        for i in range (2):
            sleep(.1)
            mouse.click(Button.left)


    def run(self) -> None:
        while True:
            sleep(.6)
            self.maxHero()
            self.scrollHero()
