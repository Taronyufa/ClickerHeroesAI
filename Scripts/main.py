from PupperFish import PupperFish
from Powers import Powers
from Damage import Damage
from Level import Level
from Hero import Hero

def main():
    dmg = Damage()
    lvl = Level(dmg)
    pws = Powers(dmg)
    # fish = PupperFish(dmg)
    # hero = Hero(dmg)

    dmg.start()
    lvl.start()
    pws.start()
    # fish.start()
    # hero.start()

if __name__ == '__main__':
    main()
