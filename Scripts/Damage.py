from pynput.mouse import Controller, Button
from threading import Thread, Condition
from pyautogui import moveTo
from pynput import mouse


class Damage (Thread):
    def __init__(self):
        Thread.__init__(self)
        self.__actions = []

    def insertAction (self, obj) -> None:
        self.__actions.append(obj)

    def getAction (self) -> object:
        return self.__actions.pop()

    def run(self) -> None:
        moveTo(1470, 630)
        mouse = Controller()

        while True:
            while len(self.__actions) == 0:
                # mouse.click(Button.left)
                pass

            currentAction = self.getAction()

            with currentAction.condition:
                currentAction.condition.notifyAll()
