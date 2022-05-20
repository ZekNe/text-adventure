from ast import arg


item_list = ["HP Potion", "Mana Potion", "Poison Potion", "Sword", "Staff", "Dagger"]

weaponSword = {
    "Name" : "Sword",
    "DMG" : 3,
    "Type" : "Slash",
    "Element" : "None" 
}

weaponStaff = {
    "Name" : "Staff",
    "DMG" : 1.5,
    "Type" : "Magic",
    "Element" : "Fire" 
}

weaponDagger = {
    "Name" : "Dagger",
    "DMG" : 2,
    "Type" : "Slash",
    "Element" : "Poison" 
}

def itemHPotion(HP):
    user_hp = HP + 50
    return user_hp

def itemManaPotion(Mana):
    user_mana = Mana + 30
    return user_mana

def itemPoisonPotion(HP):
    user_hp = HP - 50
    return user_hp

usableItems = {
    "HP Potion" : itemHPotion,
    "Mana Potion" : itemManaPotion,
    "Poison Potion" : itemPoisonPotion
}
