from pyautogui import screenshot, locateOnScreen, moveTo
from pynput.mouse import Controller, Button
from pyautogui import moveTo
from PIL import ImageGrab
from pynput import mouse
from time import sleep

# sleep(3)
# pic = ImageGrab.grab()
# print(pic.getpixel((297, 347)))

# sleep(3)
# mouse = Controller()
# moveTo(930, 1045)
# for i in range (20):
    # sleep(1)
    # mouse.click(Button.left)

screen = screenshot()
screen.show()