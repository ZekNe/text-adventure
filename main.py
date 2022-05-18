from items import item_list
import classes
import adventures
import items

# Asks for users name
user_name = input("What is your name?\nName: ")
print("Hello, %s!" %user_name)

# Ask the user to pick a Class.
class_list = ["Warrior", "Mage", "Rogue"]
user_class = ''
inventory = {"HP Potion" : 1}

# Class Selection
while user_class not in class_list:
    user_class = input("Choose your class:\n%s\n%s\n%s\nClass: " % (class_list[0], class_list[1], class_list[2]))
    if user_class == "Warrior":
        inventory["HP Potion"] += 1
        inventory["Sword"] = 1
        user_weapon = "Sword"
        user_stats = classes.Warrior
    elif user_class == "Mage":
        inventory["Staff"] = 1
        inventory["Mana Potion"] = 1
        user_weapon = "Staff"
        user_stats = classes.Mage
    elif user_class == "Rogue":
        inventory["Dagger"] = 1
        inventory["Poison Potion"] = 1
        user_weapon = "Dagger"
        user_stats = classes.Rogue
    else:
        print("Try again.\n")

user_info = {
    "Name" : user_name,
    "Class" : user_class,
    "Weapon" : user_weapon,
    "WeaponDMG" : items.weaponSword["DMG"]
}

def CheckStats():
    print("%s stats:" %user_name)
    print("----------")
    print(user_info)

CheckStats()

def CheckInventory():
    print("inventory:")
    print("----------")
    for key, value in inventory.items():
        print("%s : %s" %(key, value))

CheckInventory()

encounterEnemy = {}

adventure_list = ["Wolf Cave"]
def AdventureSelect():
    print("Choose your Adventure:")
    print(*adventure_list, sep=",")
    selectedAdventure = ''
    while selectedAdventure not in adventure_list:
        selectedAdventure = input(">")
        if selectedAdventure == "Wolf Cave":           
            encounterEnemy = adventures.WolfCave()
            Combat(encounterEnemy)
        else:
            print("Try again.\n")

def Combat(enemy):
    print("Combat begins!")
    combatEnemy = enemy

    while user_stats["HP"] > 0 and combatEnemy["HP"] > 0:
        user_action = input("Attack - Defend - Run\n>")
        if user_action == "Attack":
            combatEnemy["HP"] -= user_stats["STR"] * user_info["WeaponDMG"]
        user_stats["HP"] -= combatEnemy["STR"]
        print("Your HP %s ----- %s Enemy HP" % (user_stats["HP"], combatEnemy["HP"]))

    if user_stats["HP"] > 0:
        print("You win!")

    elif combatEnemy["HP"] > 0:
        print("Game Over")

AdventureSelect()
    
