from pynput.mouse import Controller, Button
from threading import Thread, Condition
from pyautogui import moveTo
from pynput import mouse
from time import sleep

class Damage (Thread):
    def __init__(self):
        Thread.__init__(self)
        self.__actions = []

    def insertAction (self, obj) -> None:
        self.__actions.append(obj)

    def getAction (self) -> object:
        return self.__actions.pop()

    def run(self) -> None:
        mouse = Controller()

        while True:
            # while there's no other actions to do, it does damage
            while len(self.__actions) == 0:
                moveTo(1470, 630)
                mouse.click(Button.left)

            # wake up the thread that have to do an action
            currentAction = self.getAction()

            with currentAction.condition:
                currentAction.condition.notifyAll()

            sleep(.5)
