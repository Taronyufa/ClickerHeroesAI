from pynput.mouse import Controller, Button
from threading import Thread, Condition
from pyautogui import moveTo, FAILSAFE
from pynput import mouse
from time import sleep
FAILSAFE = False

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
        moveTo(1470, 629)

        while True:
            # while there's no other actions to do, it does damage
            while len(self.__actions) == 0:
                # mouse.click(Button.left)
                pass

            # wake up the thread that have to do an action
            currentAction = self.getAction()

            with currentAction.condition:
                currentAction.condition.notifyAll()

            sleep(1)
            moveTo(1146, 680)
