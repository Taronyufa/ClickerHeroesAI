from Damage import Damage

class Click:
    def __init__(self):
        self.__dmg = Damage()

    def insertAction(self, obj):
        self.__dmg.insertAction(obj)
