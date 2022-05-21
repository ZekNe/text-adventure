from random import randrange
from items import item_list, itemHPotion
import classes
import adventures
import items


# Asks for users name
user_name = input("What is your name?\nName: ") or "User"
print("Hello, %s!" %user_name)
print("--------------------")

# Ask the user to pick a Class.
class_list = ["Warrior", "Mage", "Rogue"]
user_class = ''
inventory = {"HP Potion" : 1}

# Class Selection
while user_class not in class_list:
    user_class = input("Choose your class:\n1.%s\n2.%s\n3.%s\n\nClass: " % (class_list[0], class_list[1], class_list[2]))
    if user_class == "Warrior":
        inventory["HP Potion"] += 1
        inventory["Sword"] = 1
        user_weapon = items.weaponSword
        user_stats = classes.Warrior
    elif user_class == "Mage":
        inventory["Staff"] = 1
        inventory["Mana Potion"] = 1
        user_weapon = items.weaponStaff
        user_stats = classes.Mage
    elif user_class == "Rogue":
        inventory["Dagger"] = 1
        inventory["Poison Potion"] = 1
        user_weapon = items.weaponDagger
        user_stats = classes.Rogue
    else:
        print("Try again.\n")

# Basic user stats
user_info = {
    "Name" : user_name,
    "Class" : user_class,
    "Weapon" : user_weapon["Name"],
    "WeaponDMG" : user_weapon["DMG"]
}

# Check Stats command
def CheckStats():
    print("----------------------")
    print("%s stats:\n" %user_name)
    print(user_info)
    print("----------------------")

CheckStats()

# Check inventory command
def CheckInventory():
    print("----------------------")
    print("inventory:\n")
    for key, value in inventory.items():
        print("%s : %s" %(key, value))
    print("----------------------")

CheckInventory()

encounterEnemy = {}

# Adventure Selection
adventure_list = ["Wolf Cave, Random Encounter, Custom Encounter"]
def AdventureSelect():
    print("Choose your Adventure:\n")
    print(*adventure_list, sep=",")
    print("----------------------")
    selectedAdventure = ''
    while selectedAdventure not in adventure_list:
        selectedAdventure = input(">")
        if selectedAdventure == "Wolf Cave": # Wolf Cave           
            encounterEnemy = adventures.WolfCave()
            Combat(encounterEnemy)
            print("You leave the cave and continue your journey.")
            break
        elif selectedAdventure == "Random Encounter": # Random Encounter       
            encounterEnemy = adventures.RandomEcnounter()
            Combat(encounterEnemy)
            break
        elif selectedAdventure == "Custom Encounter": # Custom Encounter         
            encounterEnemy = adventures.CustomEncounter()
            Combat(encounterEnemy)
            break
        else:
            print("Try again.\n")

# Combat 
def Combat(enemy):
    if enemy == "": # Cancels combat if there is not enemy
        return

    print("\nCombat begins!\n")   
    combatEnemy = enemy

    while user_stats["HP"] > 0 and combatEnemy["HP"] > 0: # Combat end if user or enemy reach 0 HP
        user_action = input("Attack - Defend - Item - Run\n>")
        defend = False

        # Attack action
        if user_action == "Attack":
            combatEnemy["HP"] -= user_stats["STR"] * user_info["WeaponDMG"]
            print("----------Combat Window------------")
            print("%s attacks!" %user_info["Name"])

        # Defend action
        elif user_action == "Defend":
            defend = True
            print("----------Combat Window------------")
            print("%s defends!" %user_info["Name"])

        # Item action
        elif user_action == "Item":
            CheckInventory()
            useItem = input("What do you want to use?\nUse: ")
            if useItem not in inventory or inventory[useItem] < 1 or useItem not in items.usableItems: # Makes sure you have the item you want to use
                print("Try Again!")
                continue

            use = items.usableItems[useItem]
            if useItem == "HP Potion":   
                user_stats["HP"] = use(user_stats["HP"])
            elif useItem == "Mana Potion":   
                user_stats["MP"] = use(user_stats["MP"])
            elif useItem == "Poison Potion":   
                combatEnemy["HP"] = use(combatEnemy["HP"])

            inventory[useItem] -= 1 # Removes the used item
            print("----------Combat Window------------")   
            print("You use a %s" %useItem)

        # Run action
        elif user_action == "Run":
            return print("You escaped!")

        # Invalid action
        else:
            print("Try again!")
            continue

        # Enemy action
        EnemyAction = randrange(10) # Enemy action randomizer
        if EnemyAction < 6:
            print("%s attacks!" %enemy["Name"])
            if defend == True:
                user_stats["HP"] -= combatEnemy["STR"] * 0.5
                defend = False
            elif defend == False:
                user_stats["HP"] -= combatEnemy["STR"]

        elif EnemyAction > 5:
            print("%s defends!" %enemy["Name"])
            if user_action == "Attack":
                combatEnemy["HP"] += (user_stats["STR"] * user_info["WeaponDMG"]) / 2

        # Combat stats
        print("-----------------------------------")
        print("%s | HP - %s ----- %s - HP | %s" % (user_info["Name"], user_stats["HP"], combatEnemy["HP"], combatEnemy["Name"]))
        print("----| MP - %s ----- %s - MP |----" %(user_stats["MP"], combatEnemy["MP"]))
        print("-----------------------------------")

    if user_stats["HP"] > 0:
        print("You win!")

    elif combatEnemy["HP"] > 0:
        print("Game Over")

AdventureSelect()
    
