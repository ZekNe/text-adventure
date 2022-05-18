from items import item_list

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
    elif user_class == "Mage":
        inventory["Staff"] = 1
        inventory["Mana Potion"] = 1
    elif user_class == "Rogue":
        inventory["Dagger"] = 1
        inventory["Poison Potion"] = 1
    else:
        print("Try again.\n")

def CheckInventory():
    print("inventory:")
    print("----------")
    for key, value in inventory.items():
        print("%s : %s" %(key, value))

CheckInventory()