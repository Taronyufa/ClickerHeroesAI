from threading import Thread, Condition
from Damage import Damage

class Hero (Thread):
    def __init__(self):
        Thread.__init__(self)
        __dmg = damage()

    def run(self) -> None:
        pass