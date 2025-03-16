#imports
import pyfiglet
import os 
import platform 
import time
#variables 

version = 1.1
font = "standard"

level = 1
attack = 9 + level
defense = 9 + level
maxhealth = 100 + (level * 10) + defense
health = 100 + (level * 10) + defense

money = 0.0
# costs for each item in the shop

shopitems = {"potion": 10.0, "sword": 10.0, "shield": 10.0}

enemies = ["\U0001F479 goblin", "\U0001F47A orc", "\U0001F981 lion", "\U0001F409 dragon"]

enemy_health = {"\U0001F479 goblin": 10.0, "\U0001F47A orc": 20.0, "\U0001F981 lion": 50.0, "\U0001F409 dragon": 100.0}
enemy_attack = {"\U0001F479 goblin": 5.0, "\U0001F47A orc": 10.0, "\U0001F981 lion": 25.0, "\U0001F409 dragon": 50.0}

#starting text
print(pyfiglet.figlet_format("PYTHON RPG", font=font))
print("Version: " + str(version))

Startgame = input("Do you want to start the game? (y/n)").lower()

# clear the terminal
def clearterminal():
    if platform.system() == "Windows": os.system('cls')
    else: os.system('clear')

#calculating the shopping
def shopping_calc(money, item_cost):
    if money >= item_cost:
        return True
    else: return False

#choices
def choices():
    global money
    global health
    global maxhealth
    global attack
    global defense
    clearterminal()
    print(pyfiglet.figlet_format("CHOICES", font=font))
    choice = input(
        "Please select one of the choices below: "
        "\n \U00002694 Enter Dungeon (e) "
        "\n \U0001F4CA Stats (s) "
        "\n \U0001F4B0 Shop (sh) "
        "\n \U0000274C Exit (ex)").lower()
    #exiting 
    if choice == "ex":
        exit()
    #Stats 
    elif choice == "s":
        print(pyfiglet.figlet_format("STATS", font=font))
        print(
            " \U0001F31F Level: " + str(level) +
            "\n \U0001F496 Health: " + str(health) + "/" + str(maxhealth) +
            "\n \U0001F5E1 Attack: " + str(attack) +
            "\n \U0001F6E1 Defense: " + str(defense) +
            "\n \U0001F4B0 Money: " + str(money)
            )
        exit = input("\n\nTo exit type any character")
        if exit:
            choices()
    #shop
    elif choice == "sh":
        purchaseable = None
        item_purchased = ""
        print(pyfiglet.figlet_format("SHOP", font=font))
        print("Your amount of money: $" + str(round(money, 1)))
        print("\n \U0001F377 Potion (p): $" + str(shopitems["potion"]))
        print(" \U0001F5E1 Sword Upgrade (s): $" + str(shopitems["sword"]))
        print(" \U0001F6E1 Shield Upgrade (d): $" + str(shopitems["shield"]))
        print("\n The potion: +10\U0001F496 \n Sword Upgrade: +5\U0001F5E1 \n Sheild Upgrade: +5\U0001F6E1")
       
        # buying the items and changing cost
        while True:  # Keep looping until a valid item is chosen
            buying = input("What would you like to purchase? (p/s/d), to exit please type (ex): ").lower()

            if buying == "p":
                purchaseable = shopping_calc(money, shopitems["potion"])
                item_purchased = "potion"
                break  # Valid input, exit the loop
            elif buying == "s":
                purchaseable = shopping_calc(money, shopitems["sword"])
                item_purchased = "sword"
                break  # Valid input, exit the loop
            elif buying == "d":
                purchaseable = shopping_calc(money, shopitems["shield"])
                item_purchased = "shield"
                break  # Valid input, exit the loop
            elif buying == "ex":
                choices()
                break
            else:
                print("Please enter one of the shop items (p/s/d).")
                
        if purchaseable == True:
            money-= shopitems[item_purchased]
            print("You have purchased the " + item_purchased + " for $" + str(shopitems[item_purchased]))
            shopitems[item_purchased] = round(shopitems[item_purchased] * 1.5, 1)
            if item_purchased == "potion":
                health += 10
                maxhealth += 10
            elif item_purchased == "sword":
                attack += 5
            elif item_purchased == "shield":
                defense += 5
            choices()
        else: 
            print("\U0001F6AB Not enough funds \U0001F6AB")
            time.sleep(1)
            choices()
    #dungeon
    elif choice == "e":
        print(pyfiglet.figlet_format("DUNGEON", font=font))
        dungeon()

    else:
        choices()

#dungeon function
def dungeon():
    global health
    global maxhealth
    global level
    global money
    global attack
    print("You have entered the dungeon")
    if level < 10:
        enemy = enemies[0]
    elif level < 20:
        enemy = enemies[1]
    elif level < 30:
        enemy = enemies[2]
    else:
        enemy = enemies[3]
    enemy_health_points = enemy_health[enemy] * (1 + level/10)
    enemy_attack_points = enemy_attack[enemy] * (1 + level/10)
    print("You have encountered a " + enemy)
    print("Your health: " + str(health))
    print(enemy + " health: " + str(enemy_health_points))
    print("Your attack: " + str(attack))
    print(enemy + " attack: " + str(enemy_attack_points))
    battle = input("What would you like to do fight(f) or run(r)?").lower()

    if battle == "f":
        health_lost = 0
        while enemy_health_points > 0:
            enemy_health_points -= attack
            health -= enemy_attack_points
            health_lost+= enemy_attack_points
            if health <= 0:
                print(pyfiglet.figlet_format("GAME OVER", font=font))
                print(
            " \U0001F31F Level: " + str(level) +
            "\n \U0001F5E1 Attack: " + str(attack) +
            "\n \U0001F6E1 Defense: " + str(defense) +
            "\n \U0001F4B0 Money: " + str(money)
            )
                time.sleep(2)
                exit()
        print("You have defeated the " + enemy)
        level += 1
        health = 100 + (level * 10) + defense - health_lost
        maxhealth = 100 + (level * 10) + defense
        money += 10 + enemy_health[enemy] * (level/2)
        money = round(money , 1)
        print("You have leveled up to level " + str(level))
        time.sleep(1)
        choices()
    elif battle == "r":
        print("You have run away")
        time.sleep(2)
        choices()
    else:
        choices()
        


#start the game
if Startgame == "y":
    choices()
elif Startgame == "n":
    exit()
else:
    Startgame = input("Do you want to start the game? (y/n)")
    if Startgame == "y":
        choices()
    elif Startgame == "n":
        exit()