from threading import Thread, Condition
from Damage import Damage

class Hero (Thread):
    def __init__(self, dmg):
        Thread.__init__(self)
        self.__dmg: Damage = dmg

    def run(self) -> None:
        pass