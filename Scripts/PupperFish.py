from threading import Thread, Condition
from Damage import Damage

class PupperFish (Thread):
    def __init__(self, dmg):
        Thread.__init__(self)
        self.__dmg: Damage = dmg
        self.condition = Condition()

    def run(self) -> None:
        pass