from pynput.mouse import Controller, Button
from threading import Thread, Condition
from Damage import Damage
from PIL import ImageGrab
from pynput import mouse
import pyscreenshot
import pytesseract

class Level (Thread):
    def __init__(self):
        Thread.__init__(self)
        self.__dmg = Damage()
        self.condition = Condition()

    def levelUp(self) -> None:
        mouse = Controller()
        pyautogui.moveTo(1544, 74)
        mouse.click(Button.left)
        pyautogui.moveTo(1470, 630)

    def levelDown(self) -> None:
        mouse = Controller()
        pyautogui.moveTo(1544, 74) # Level down cords
        mouse.click(Button.left)
        pyautogui.moveTo(1470, 630)

    def run(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        while True:
            pic = ImageGrab.grab(bbox=(1424, 187, 1556, 240))
            text = pytesseract.image_to_string(pic)
            if "10/10" in text:
                with self.condition:
                    self.__dmg.insertAction(self)

                    self.condition.wait()

                    self.levelUp()
