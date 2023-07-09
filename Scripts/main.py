from Damage import Damage
from Level import Level
from Hero import Hero

def main():
    dmg = Damage()
    lvl = Level(dmg)
    # hero = Hero(dmg)

    dmg.start()
    lvl.start()
    # hero.start()

if __name__ == '__main__':
    main()
