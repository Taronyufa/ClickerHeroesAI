from Damage import Damage
from Level import Level
from Hero import Hero
from Powers import Powers

def main():
    dmg = Damage()
    lvl = Level(dmg)
    pws = Powers(dmg)
    # hero = Hero(dmg)

    dmg.start()
    lvl.start()
    pws.start()
    # hero.start()

if __name__ == '__main__':
    main()
