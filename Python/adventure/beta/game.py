import os
import random
import sys
import time
import game_object  # player
from static import clear, screen_width, speech_manipulation
# from map import zonemap
import player
from npc import NPC, Bandit, Orc, Giant

myPlayer = player.Player()




##### Title #####
def title_screen_selections():
    option = input("> ")
    if option.lower() == "play":
        setup_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()

    while option.lower() not in ["play", "help", "quit"]:
        print("Invalid command. Type 'play', 'help', 'quit'")
        title_screen_selections()


def title_screen():
    clear()
    print("#" * screen_width)
    print("#" + (" " * int((screen_width - len("Welcome to the Text RPG")) / 2)) + "Welcome to the Text RPG" + (
            " " * int((screen_width - 2 - len("Welcome to the Text RPG")) / 2)) + "#")
    print("#" + "=" * (screen_width - 2) + "#")
    print("#" + (" " * int((screen_width - 6) / 2)) + "-play-" + (" " * int((screen_width - 9) / 2)) + "#")
    print("#" + (" " * int((screen_width - 6) / 2)) + "-help-" + (" " * int((screen_width - 9) / 2)) + "#")
    print("#" + (" " * int((screen_width - 6) / 2)) + "-quit-" + (" " * int((screen_width - 9) / 2)) + "#")
    print("#" * screen_width + "\n")
    title_screen_selections()


def help_menu():
    clear()
    print("#" * screen_width)
    print(("=" * int((screen_width - len("HELP MENU")) / 2)) + "HELP MENU" + (
            "=" * int((screen_width - len("HELP MENU")) / 2)))
    print("#" * screen_width)
    print("")
    print(" -- You can always decide to 'examine' a location or 'move' to another.")
    print(" -- You can always see your inventory with 'show inventory' and show your stats with 'show stats'")
    print(" -- If you examine a location you may trigger a random encounter and you can 'fish', 'hunt' or 'get corn'")
    print(" -- If you move, you can decide to move 'up', 'down', 'left' or 'right'")
    print("")
    print("Press ENTER to continue.")
    input()
    title_screen()
    title_screen_selections()


### MAP ###
solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False, 'b1': False, 'b2': False, 'b3': False, 'b4': False, 'c1': False, 'c2': False, 'c3': False, 'c4': False, 'd1': False, 'd2': False, 'd3': False, 'd4': False}

##### MAP PRE #####
# ""ZONENAME"" = ""
# ""DESCRIPTION"" = ""DESCRIPTION""
# ""EXAMINATION"" = "examine"
# ""SOLVED"" = False
# ""UP"" = ""UP""
# ""DOWN"" = ""DOWN""
# ""LEFT"" = ""LEFT""
# ""RIGHT"" = ""RIGHT""
# ""SOLVED"_ENCOUNTER_COUNT" = 0
# ""ENCOUNTERS"" = 0
POSSIBILITIES = myPlayer.pos

zonemap = {
    "a1": {
        "ZONENAME": "Town Marketplace",
        "DESCRIPTION": "This is the marketplace of your hometown.",
        "EXAMINATION": "You can see some stalls selling different things.",
        "SOLVED": False,
        "UP": "",
        "DOWN": "b1",
        "LEFT": "",
        "RIGHT": "a2",
        "ENCOUNTERS": 0,
        "POSSIBILITIES": POSSIBILITIES
    },
    "a2": {
        "ZONENAME": "Towngate",
        "DESCRIPTION": "This is the gate of your hometown.",
        "EXAMINATION": "The gate is locked at night. You have to be nice to the guardsmen, if you try to enter at "
                       "night.",
        "SOLVED": False,
        "UP": "",
        "DOWN": "b2",
        "LEFT": "a1",
        "RIGHT": "a3",
        "ENCOUNTERS": 0,
        "POSSIBILITIES": POSSIBILITIES
    },
    "a3": {
        "ZONENAME": "Grassland",
        "DESCRIPTION": "Nothing but green grass.",
        "EXAMINATION": "I'm serious. It's nothing but grass.",
        "SOLVED": False,
        "UP": "",
        "DOWN": "b3",
        "LEFT": "a2",
        "RIGHT": "a4",
        "ENCOUNTERS": 2,
        "POSSIBILITIES": POSSIBILITIES
    },
    "a4": {
        "ZONENAME": "Little Pond",
        "DESCRIPTION": "This is a cute little pond.",
        "EXAMINATION": "With a fishingrot you could get some fish out of it.",
        "SOLVED": False,
        "UP": "",
        "DOWN": "b4",
        "LEFT": "a3",
        "RIGHT": "",
        "ENCOUNTERS": 2,
        "POSSIBILITIES": POSSIBILITIES
    },
    "b1": {
        "ZONENAME": "Blacksmith",
        "DESCRIPTION": "This is your local blacksmith.",
        "EXAMINATION": "Here you can buy/sell some weapons or protections",
        "SOLVED": False,
        "UP": "a1",
        "DOWN": "c1",
        "LEFT": "",
        "RIGHT": "b2",
        "ENCOUNTERS": 0,
        "POSSIBILITIES": POSSIBILITIES
    },
    "b2": {
        "ZONENAME": "Home",
        "DESCRIPTION": "This is your home!",
        "EXAMINATION": "Your home looks cosy.",
        "SOLVED": False,
        "UP": "a2",
        "DOWN": "c2",
        "LEFT": "b1",
        "RIGHT": "b3",
        "ENCOUNTERS": 0,
        "POSSIBILITIES": POSSIBILITIES
    },
    "b3": {
        "ZONENAME": "Small Forest",
        "DESCRIPTION": "A small forest next to your home.",
        "EXAMINATION": "You could hunt in this forest to get some food. But some bandits were seen in there, too.",
        "SOLVED": False,
        "UP": "a3",
        "DOWN": "c3",
        "LEFT": "b2",
        "RIGHT": "b4",
        "ENCOUNTERS": 3,
        "POSSIBILITIES": POSSIBILITIES
    },
    "b4": {
        "ZONENAME": "Small Forest",
        "DESCRIPTION": "A small forest next to your home.",
        "EXAMINATION": "You could hunt in this forest to get some food. But some bandits were seen in there, too.",
        "SOLVED": False,
        "UP": "a4",
        "DOWN": "c4",
        "LEFT": "b3",
        "RIGHT": "",
        "ENCOUNTERS": 3,
        "POSSIBILITIES": POSSIBILITIES
    },
    "c1": {
        "ZONENAME": "Little River",
        "DESCRIPTION": "This river comes out of the forest in the east.",
        "EXAMINATION": "Further to the forest you can see a bridge over the river.",
        "SOLVED": False,
        "UP": "b1",
        "DOWN": "d1",
        "LEFT": "",
        "RIGHT": "c2",
        "ENCOUNTERS": 2,
        "POSSIBILITIES": POSSIBILITIES
    },
    "c2": {
        "ZONENAME": "Little River (Bridge)",
        "DESCRIPTION": "This river comes out of the forest in the east.",
        "EXAMINATION": "You see a bridge leading over the river to get to the other side.",
        "SOLVED": False,
        "UP": "b2",
        "DOWN": "d2",
        "LEFT": "c1",
        "RIGHT": "c3",
        "ENCOUNTERS": 2,
        "POSSIBILITIES": POSSIBILITIES
    },
    "c3": {
        "ZONENAME": "Small Forest",
        "DESCRIPTION": "A small forest next to your home.",
        "EXAMINATION": "You could hunt in this forest to get some food. But some bandits were seen in there, too.",
        "SOLVED": False,
        "UP": "b3",
        "DOWN": "d3",
        "LEFT": "c2",
        "RIGHT": "c4",
        "ENCOUNTERS": 3,
        "POSSIBILITIES": POSSIBILITIES
    },
    "c4": {
        "ZONENAME": "Small Forest",
        "DESCRIPTION": "A small forest next to your home.",
        "EXAMINATION": "You could hunt in this forest to get some food. But some bandits were seen in there, too.",
        "SOLVED": False,
        "UP": "b4",
        "DOWN": "d4",
        "LEFT": "c3",
        "RIGHT": "",
        "ENCOUNTERS": 3,
        "POSSIBILITIES": POSSIBILITIES
    },
    "d1": {
        "ZONENAME": "Cave",
        "DESCRIPTION": "Down in the south is a small Trollcave.",
        "EXAMINATION": "You see some skelletons of deer and horses. Is it really a good idea to go into the cave?",
        "SOLVED": False,
        "UP": "c1",
        "DOWN": "",
        "LEFT": "",
        "RIGHT": "d2",
        "ENCOUNTERS": 5,
        "POSSIBILITIES": [0.7, 0.3, 1]
    },
    "d2": {
        "ZONENAME": "Cornfield",
        "DESCRIPTION": "This cornfield belongs to the farm in the east. Maybe you can get some corn from it?",
        "EXAMINATION": "Looks like this corn is better than what you have ever seen.",
        "SOLVED": False,
        "UP": "c2",
        "DOWN": "",
        "LEFT": "d1",
        "RIGHT": "d3",
        "ENCOUNTERS": 2,
        "POSSIBILITIES": POSSIBILITIES
    },
    "d3": {
        "ZONENAME": "Farm",
        "DESCRIPTION": "This farm is owned by an old farmer.",
        "EXAMINATION": "You have heard some scary stories about this farmer. Maybe he is not very nice?",
        "SOLVED": False,
        "UP": "c3",
        "DOWN": "",
        "LEFT": "d2",
        "RIGHT": "d4",
        "ENCOUNTERS": 3,
        "POSSIBILITIES": POSSIBILITIES
    },
    "d4": {
        "ZONENAME": "Bandit Hideout",
        "DESCRIPTION": "This looks like some bandit hideout, which was not here the last time you were here.",
        "EXAMINATION": "You cannot see any other human being. But you feel that you better move away.",
        "SOLVED": False,
        "UP": "c4",
        "DOWN": "",
        "LEFT": "d3",
        "RIGHT": "",
        "ENCOUNTERS": 7,
        "POSSIBILITIES": [0.5, 1, 0]
    }
}

def fight_setup(player, poss):
    clear()
    print("#" * screen_width)
    print(" " * int((screen_width - len("FIGHT")) / 2) + "FIGHT")
    print("#" * screen_width)
    enemy = ""
    x = random.random()
    if x < poss[0]:
        enemy = Bandit()
    elif poss[0] < x < poss[0] + poss[1]:
        enemy = Orc()
    else:
        enemy = Giant()  # else, solange nur 3 mögliche Gegner
    fight(player, enemy)

def fight(player, enemy):
    flee = 0
    dead = 0
    while dead == 0:  
        while enemy.health > 0 and flee == 0:
            print("                 ")
            print("You fight against: " + enemy.name)
            enemy.health_print()
            player.health()
#Auswahl für Kampf --------------------------------------------------
            a = fight_options().lower()  # das geht sicher eleganter
            valid_options = ["attack", "heal", "flee", "show stats", "quit"] #In den fight_options() immer ergänzen
            while a not in valid_options:
                print("Please use a valid answer.")
                a = fight_options().lower()
#Spieler-Angriff --------------------------------------------------
            if a == "attack":
                if not player.weapon.broken:
                    print("You attack with your weapon and do " + str(player.weapon.damage) + " damage.")
                    player.weapon.durability[0] -= 1
                    print("Weapon durability: " + str((player.weapon.durability[0]/player.weapon.durability[1])*100) + "%")
                    if player.weapon.durability[0] == 0:
                        player.weapon.broken = True
                        print("Your weapon broke! Repair it at a Blacksmith's.")
                    enemy.health -= player.weapon.damage
                else:
                    print("Your weapon is broken. You only do 2 damage.")
                    enemy.health -= 2
                print("enemy: " + random.choice(enemy.quip))
                if enemy.health <= 0:
                    print("       ")
                    print("**** You won!!! ****")
                    print("       ")
                    zonemap[myPlayer.location]["ENCOUNTERS"] -= 1
                    break
#Spieler-Andere Optionen --------------------------------------------------
            elif a == "heal":
                player.use_potion() 
            elif a == "flee":
                if random.random() < 0.6:  # 60% Fluchtchance (fix? Future-Feature)
                    flee = 1
                    break
                else:
                    print("Your enemy won't let you go!")
            elif a == "show stats":
                player.show_stats()
            elif a == "quit": #ganz Spiel aus im Kampf?
                sys.exit()

#Gegner-Angriff --------------------------------------------------
            #Spieler nimmt Schaden
            if random.random() < enemy.accuracy:
                if player.armor == 0: #Wenn keine Rüstung anliegt
                    print("Your enemy attacks and does " + str(enemy.strength) + " damage.")
                    player.health_cur -= enemy.strength
                else: #Es gibt Rüstung
                    print("Your enemy attacks and does " + str(enemy.strength-player.armor) + " damage.")
                    player.health_cur -= enemy.strength-player.armor
                    #Es wird ein Index eines zufälligen aber angelegten Rüstungsteils gewählt
                    x = player.inventory["armor"][random.choice([a for a,b in list(enumerate(player.inventory["armor"])) if b.equipped == True])]
                    x.durability[0] -= 1
                    print("Your " + x.slot + " armor was hit.")
                    print("Durability: " + str((x.durability[0]/x.durability[0])*100) + "%")
                #Falls Spieler zu viel Schaden genommen hat --> Spielende
                if player.health_cur <= 0:
                    speech_manipulation("You are dead . . .", 0.03)
                    print(" ")
                    time.sleep(2)
                    player.game_over = True 
                    dead = 1
                    game_over() #Textanzeige
                    break #Löst ersten loop der fight, anschließend automatisch zweiten

            #Spieler nimmt keinen Schaden
            else:
                print("Your enemy attacks.")
                time.sleep(0.7) #dramatic pause :D
                print("Missed!")

#Kampf ist vorbei --------------------------------------------------
        time.sleep(2)
        clear()
        if flee == 1 and dead == 0: #Lebendig aber geflohen? -> keine Belohnung
            print("You ran away. You don't get a reward.")
            break # Bricht while enemy.health > 0 and flee == 0: loop, anschließend while dead loop.
        elif dead == 1: #Gestorben? 
            break # Bricht while enemy.health > 0 and flee == 0: loop, anschließend while dead loop.
        else:
            if random.random() < enemy.loot_chance:  # Chance ob Loot-Drop oder nicht (abhängig von Gegner)
                loot(enemy, player) # Spieler erhält Trank(30%) oder Gegenstand(70%)
            else:
                print("Looks like you found nothing interesting...")
            #Garantierte Belohnungen: Gold und Erfahrung
            player.get_ep(enemy.ep_drop)
            player.get_gold(random.randrange(10,20)*enemy.loot_level)
            time.sleep(2) #Notwendig?

#Kampf-Loop wird aufgelöst --------------------------------------------------
        time.sleep(2)
        clear()
        break #Bricht while dead == 0: loop


def loot(enemy, player):
    if random.random() < 0.70: #Chance auf Gegenstand: 70%, sonst Trank
        g = random.choice([game_object.Weapon(enemy.loot_level), game_object.Armor(enemy.loot_level)])
        if g.obj_type == "weapon":
            print("You find: " + g.name)
            print("Damage: " + str(g.damage))
            print("Would you like to swap your weapon? (y/n)\n")
            ant = input("> ")
            print(" ")
            if ant.lower()[0] in ["y", ""]:
                player.equip_weapon(g) # neue Waffe angelegt und alte Waffe equipped = False
            player.get_weapon(g,p=False)  # Waffe (zusätzlich) ins Inventar
        elif g.obj_type == "armor":
            print("You find: " + g.name)
            print("Protection: " + str(g.protection))
            print("Slot: " + g.slot)
            print("Would you like to swap your armor? (y/n)\n")
            ant = input("> ")
            print("")
            if ant.lower()[0] in ["y", ""]:
                player.equip_armor(g) #Rüstung angelegt und alte Rüstung equipped = False
                print("You equip your new armor.")
            player.get_armor(g,p=False)  # Waffe (zusätzlich) ins Inventar
    else:
        player.get_potion()

def fight_options():
    print("Choose: attack, heal, flee, show stats, quit\n")
    ant = input("> ")
    clear()
    return ant

def print_location():
    print("#" * screen_width)
    print((" " * int((screen_width - len(zonemap[myPlayer.location]["ZONENAME"])) / 2)) + zonemap[myPlayer.location][
        "ZONENAME"] + (" " * int((screen_width - len(zonemap[myPlayer.location]["ZONENAME"])) / 2)))
    print((" " * int((screen_width - len(zonemap[myPlayer.location]["DESCRIPTION"])) / 2)) + zonemap[myPlayer.location][
        "DESCRIPTION"] + (" " * int((screen_width - len(zonemap[myPlayer.location]["DESCRIPTION"])) / 2)))
    if zonemap[myPlayer.location]["SOLVED"] == True:
        print((" " * int(
            (screen_width - len(zonemap[myPlayer.location]["EXAMINATION"] + "EXAMINATION")) / 2)) + "EXAMINATION: " +
              zonemap[myPlayer.location]["EXAMINATION"] + (" " * int(
            (screen_width - len(zonemap[myPlayer.location]["EXAMINATION"] + "EXAMINATION")) / 2)))
    print("#" * screen_width)


def promt():
    print("You are here:")
    print_location()
    print("\n" + "=" * len("What would you like to do?"))
    print("What would you like to do?\n")
    print("-" * len("What would you like to do?"))
    print(" " * (int((len("What would you like to do?") - len("examine or move?")) / 2)) + "examine or move?")
    print("-" * len("What would you like to do?") + "\n")

    action = input("> ")
    acceptable_locations = ["move", "go", "travel", "walk", "quit", "examine", "inspect", "interact", "look", "hunting",
                            "hunt", "fishing", "fish", "corn", "get corn", "harvest", "heal", "healing", "potion",
                            "use potion", "show inventory", "inventory", "show stats", "stats", "buy", "sell", "blacksmith"]

    while action.lower() not in acceptable_locations:
        print("Unknown action. Try again. (move, examine, quit)")
        action = input("> ")

    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in ["move", "go", "travel", "walk"]:
        player_move()
    elif action.lower() in ["examine", "inspect", "interact", "look"]:
        player_examine()
    elif action.lower() in ["fishing", "fish"]:
        myPlayer.fishing()
    elif action.lower() in ["hunting", "hunt"]:
        myPlayer.hunting()
    elif action.lower() in ["corn", "get corn", "harvest"]:
        myPlayer.getCorn()
    elif action.lower() in ["heal", "healing", "potion", "use potion"]:
        myPlayer.use_potion()
    elif action.lower() in ["show inventory", "inventory"]:
        myPlayer.print_inventory()
    elif action.lower() in ["show stats", "stats"]:
        myPlayer.show_stats()
    elif action.lower() in ["buy", "sell", "blacksmith"]:
        myPlayer.buy_equipment()


def player_move():
    dest = input("Where do you like to move to? ('up', 'down', 'left', 'right')\n> ")

    while dest not in ['up', 'down', 'left', 'right']:
        print("Invalid entry!")
        dest = input("Where do you like to move to? ('up', 'down', 'left', 'right')\n> ")

    if dest.lower() == "up":
        if zonemap[myPlayer.location]["UP"] != "":
            destination = zonemap[myPlayer.location]["UP"]
            movement(destination)
        else:
            stay(dest)
    elif dest.lower() == "down":
        if zonemap[myPlayer.location]["DOWN"] != "":
            destination = zonemap[myPlayer.location]["DOWN"]
            movement(destination)
        else:
            stay(dest)
    elif dest.lower() == "right":
        if zonemap[myPlayer.location]["RIGHT"] != "":
            destination = zonemap[myPlayer.location]["RIGHT"]
            movement(destination)
        else:
            stay(dest)
    elif dest.lower() == "left":
        if zonemap[myPlayer.location]["LEFT"] != "":
            destination = zonemap[myPlayer.location]["LEFT"]
            movement(destination)
        else:
            stay(dest)


def movement(destination):
    myPlayer.location = destination
    print("You have moved to the " + zonemap[myPlayer.location]["ZONENAME"] + ".")
    time.sleep(3)
    clear()



def stay(direct):
    directions = {"up": "north", "down": "south", "left": "west", "right": "east"}
    print("You cannot move further " + directions[direct] + ".")
    time.sleep(3)
    clear()


def player_examine():
    if zonemap[myPlayer.location]["ENCOUNTERS"] > 0:
        fight_setup(myPlayer, zonemap[myPlayer.location]["POSSIBILITIES"])

    if zonemap[myPlayer.location]["SOLVED"] == True:
        print("You have already been here.")
        print(zonemap[myPlayer.location]["EXAMINATION"])
        time.sleep(3)
        clear()
    else:
        print(zonemap[myPlayer.location]["EXAMINATION"])
        zonemap[myPlayer.location]["SOLVED"] = True
        if all(solved_places.values()):
            myPlayer.game_over = True
        time.sleep(3)
        clear()


def intro():
    clear()
    question3 = "Welcome, " + myPlayer.name + " the " + myPlayer.play_class + ".\n"
    speech_manipulation(question3, 0.05)
    speech_manipulation("Welcome to this fantasy world I created for you. ;)\n", 0.05)
    speech_manipulation("I hope you will have some fun\n ... \n ... \n ...\n", 0.15)
    speech_manipulation(
        "Well, you are not the first adventurer here. There have been many before you. And to be honest, there will "
        "be many after you ... when you have ... ",
        0.05)
    speech_manipulation("passed away ... \n", 0.25)
    speech_manipulation("Now have some fun exploring the world. We will see each other when it's time to.\n", 0.05)
    time.sleep(2)


def end_screen():
    speech_manipulation(
        "Congratulations, you have solved the complete game. I never thought you would be able to do this.", 0.05)
    print("")
    speech_manipulation(
        "I will get in touch with you soon. Wait for a sign from me. I think I have a good job for some strong "
        "adventurer like you.",
        0.04)

    time.sleep(5)
    clear()
    # print("Made by laeberkaes")
    # print("Hit me "UP" at: https://github.com/laeberkaes/ or @laeberkaes:uraltemorla.xyz")
    #
    # time.sleep(5)
    sys.exit()


def game_over():
    clear()
    speech_manipulation("Ouh there you are again.\n", 0.05)
    speech_manipulation(
        "Don't get me wrong. This is no surprise for me. Maybe you have more luck in your next reincarnation.\n",
        0.05)
    speech_manipulation("Have a good day. :)", 0.07)
    time.sleep(2)
    sys.exit()


def game_loop():
    while not myPlayer.game_over:
        promt()


def setup_game():
    clear()
    question1 = "Hello what's your name?\n"
    speech_manipulation(question1, 0.05)
    print("")
    myPlayer.name = input("> ").lower()

    clear()

    classes = ["warrior", "mage", "rogue"]
    question2 = "What Class do you want to play? (Warrior, Mage, Rogue)\n"
    speech_manipulation(question2, 0.01)
    print("")
    player_class = input("> ").lower()
    print("")
    if player_class.lower() in classes:
        myPlayer.play_class = player_class
        print("You are now " + player_class)
        time.sleep(1.5)
    else:
        while player_class.lower() not in classes:
            print("No valid class.\n")
            player_class = input("> ").lower()
        if player_class.lower() in classes:
            myPlayer.play_class = player_class
            print("You are now " + player_class)
            time.sleep(1.5)

    if myPlayer.play_class == "warrior":
        myPlayer.health_max = 120
        myPlayer.health_cur = 120
        myPlayer.mp = 20
    elif myPlayer.play_class == "mage":
        myPlayer.health_max = 80
        myPlayer.health_cur = 80
        myPlayer.mp = 80
    elif myPlayer.play_class == "rogue":
        myPlayer.health_max = 100
        myPlayer.health_cur = 100
        myPlayer.mp = 40

    # intro()

    clear()
    print("#" * screen_width + "\n")
    print("#" + (" " * int((screen_width - 2 - len("Let's start now")) / 2)) + "Let's start now" + (
            " " * int((screen_width - 2 - len("Let's start now")) / 2)) + "#\n")
    print("#" * screen_width + "\n")

    game_loop()

    end_screen()


if __name__ == "__main__":
    title_screen()
