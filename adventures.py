from random import randrange
import enemy

def WolfCave():
    print("You encounter a wolf in the cave!")
    encounterEnemy = enemy.Wolf
    return encounterEnemy

def CustomEncounter():
    x = 0  
    for i in enemy.enemies:
        print("%s.%s" %( x + 1, enemy.enemies[x]["Name"]))
        x += 1

    x = 0
    chosen = input("Choose Enemy: ")
    for i in enemy.enemies:
        if chosen == enemy.enemies[x]["Name"]:
            encounterEnemy = enemy.enemies[x]
            return encounterEnemy
        x += 1

def RandomEcnounter():
    random = randrange(len(enemy.enemies))
    encounterEnemy = enemy.enemies[random]
    return encounterEnemy