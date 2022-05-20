from random import randrange
import enemy

def WolfCave():
    
    while True:
        action = input("You find yourself at a cave entrance.\n What do you want to do?\n1.Enter\n2.Leave\n>")
        if action == "Enter":
            print("You enter the cave.")
            break
        elif action == "Leave":
            print("You leave the cave and continue your journey.")
            return ""
        else:
            print("Try Again!")
    
    while True:
        action = input("There is two paths, one leads left the other right.\n What path do you take?\n1.Left\n2.Right\n>")
        if action == "Left":
            print("The path you took leads to a dead end. \nYou go back to the entrance.")
            action = input("Do you Leave the cave or take the Right path?\n1.Leave\n2.Right\n>")
            if action == "Leave":
                print("You leave the cave and continue your journey.")
                return ""
            elif action == "Right":
                break
            elif action != "Leave" or "Right":
                print("Try Again!")
        break

    print("You decide to take the right path. \nAfter a bit of walking you find a large open space. \nThere is something moving in the shadows!")    
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