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
            # while there's no other actions to do, it does damage
            while len(self.__actions) == 0:
                # mouse.click(Button.left)
                pass

            # wake up the thread that have to do an action
            currentAction = self.getAction()

            with currentAction.condition:
                currentAction.condition.notifyAll()
