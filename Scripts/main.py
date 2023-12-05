from PupperFish import PupperFish
from pyautogui import FAILSAFE
from Powers import Powers
from Damage import Damage
from Level import Level
from time import sleep
from Hero import Hero
FAILSAFE = False

def main():
    dmg = Damage()
    lvl = Level(dmg)
    pws = Powers(dmg)
    # fish = PupperFish(dmg) # funziona ma non funziona
    hero = Hero(dmg)

    sleep(5)

    dmg.start()
    lvl.start()
    # pws.start()
    # fish.start()
    hero.start()

if __name__ == '__main__':
    main()
