import cmd, textwrap, sys, os, time, random
import weapon

screen_width = 60

class Player:
    def __init__(self, name: str):
        self.name = name
        self.play_class = ""
        self.hp = 0
        self.mp = 0
        self.ep = 0
        self.level = 1
        self.status_effects = []
        self.location = "b2"
        self.game_over = False
        self.weapon = weapon.getWeapon(self.level)

    def levelUp(self):
        self.level += 1
        self.health_max += 20
        self.ep = 0

    def getEP(self,amount):
        self.ep += amount
        if self.ep > 100:
            self.levelUp()

    def getWeapon(self,weapon):
        self.weapon = weapon

    def getGold(self,amount):
        self.gold += amount

    def getPotion(self,amount):
        self.potion += amount

    def usePotion(self):
        self.health_cur += 25
        if self.health_cur > self.health_max:
            self.health_cur = self.health_max

    def getProtect(self,amount):
        self.protect += amount

myPlayer = Player("Testname")

##### Title #####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()

    while option.lower() not in ["play","help","quit"]:
        print("Invalid command. Type 'play', 'help', 'quit'")
        title_screen_selections()

def title_screen():
    print("#"*(4+len("Welcome to the Text RPG")))
    print("# Welcome to the Text RPG #")
    print("#"*(4+len("Welcome to the Text RPG")))
    print("# " + (" "*int((len("Welcome to the Text RPG")-6)/2)) + "-play-" + (" "*int((len("Welcome to the Text RPG")-6)/2)) + " #")
    print("# " + (" "*int((len("Welcome to the Text RPG")-6)/2)) + "-help-" + (" "*int((len("Welcome to the Text RPG")-6)/2)) + " #")
    print("# " + (" "*int((len("Welcome to the Text RPG")-6)/2)) + "-quit-" + (" "*int((len("Welcome to the Text RPG")-6)/2)) + " #")
    print("#"*(4+len("Welcome to the Text RPG"))+"\n")
    title_screen_selections()

def help_menu():
    print("#"*27)
    print("# Welcome to the Text RPG #")
    print("#"*27)
    print(" -- Use up, down, left, right to move")
    print(" -- Type your commands to do them")
    print(" -- Good luck and have fun!")
    title_screen()
    title_screen_selections()

### MAP ###
ZONENAME = ""
DESCRIPTION = "description"
EXAMINATION = "examine"
SOLVED = False
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

solved_places = {'a1': True, 'a2': True, 'a3': True, 'a4': True, 'b1': True, 'b2': False, 'b3': True, 'b4': True, 'c1': True, 'c2': True, 'c3': True, 'c4': True, 'd1': True, 'd2': True, 'd3': True, 'd4': True}

zonemap = {
    "a1": {
        ZONENAME: "Town Marketplace",
        DESCRIPTION: "This is the marketplace of your hometown.",
        EXAMINATION: "You can see some stalls selling different things.",
        SOLVED: False,
        UP: "",
        DOWN: "b1",
        LEFT: "",
        RIGHT: "a2"
    },
    "a2": {
        ZONENAME: "Towngate",
        DESCRIPTION: "This is the gate of your hometown.",
        EXAMINATION: "The gate is locked at night. You have to be nice to the guardsmen, if you try to enter at night.",
        SOLVED: False,
        UP: "",
        DOWN: "b2",
        LEFT: "a1",
        RIGHT: "a3"
    },
    "a3": {
        ZONENAME: "Grassland",
        DESCRIPTION: "Nothing but green grass.",
        EXAMINATION: "I'm serious. It's nothing but grass.",
        SOLVED: False,
        UP: "",
        DOWN: "b3",
        LEFT: "a2",
        RIGHT: "a4"
    },
    "a4": {
        ZONENAME: "Little Pond",
        DESCRIPTION: "This is a cute little pond.",
        EXAMINATION: "With a fishingrot you could get some fish out of it.",
        SOLVED: False,
        UP: "",
        DOWN: "b4",
        LEFT: "a3",
        RIGHT: ""
    },
    "b1": {
        ZONENAME: "Blacksmith",
        DESCRIPTION: "This is your local blacksmith.",
        EXAMINATION: "Here you can buy/sell some weapons or protections",
        SOLVED: False,
        UP: "a1",
        DOWN: "c1",
        LEFT: "",
        RIGHT: "b2"
    },
    "b2": {
        ZONENAME: "Home",
        DESCRIPTION: "This is your home!",
        EXAMINATION: "Your home looks cosy.",
        SOLVED: False,
        UP: "a2",
        DOWN: "c2",
        LEFT: "b1",
        RIGHT: "b3"
    },
    "b3": {
        ZONENAME: "Small Forest",
        DESCRIPTION: "A small forest next to your home.",
        EXAMINATION: "You could hunt in this forest to get some food. But some bandits were seen in there, too.",
        SOLVED: False,
        UP: "a3",
        DOWN: "c3",
        LEFT: "b2",
        RIGHT: "b4"
    },
    "b4": {
        ZONENAME: "Small Forest",
        DESCRIPTION: "A small forest next to your home.",
        EXAMINATION: "You could hunt in this forest to get some food. But some bandits were seen in there, too.",
        SOLVED: False,
        UP: "a4",
        DOWN: "c4",
        LEFT: "b3",
        RIGHT: ""
    },
    "c1": {
        ZONENAME: "Little River",
        DESCRIPTION: "This river comes out of the forest in the east.",
        EXAMINATION: "Further to the forest you can see a bridge over the river.",
        SOLVED: False,
        UP: "b1",
        DOWN: "d1",
        LEFT: "",
        RIGHT: "c2"
    },
    "c2": {
        ZONENAME: "Little River (Bridge)",
        DESCRIPTION: "This river comes out of the forest in the east.",
        EXAMINATION: "You see a bridge leading over the river to get to the other side.",
        SOLVED: False,
        UP: "b2",
        DOWN: "d2",
        LEFT: "c1",
        RIGHT: "c3"
    },
    "c3": {
        ZONENAME: "Small Forest",
        DESCRIPTION: "A small forest next to your home.",
        EXAMINATION: "You could hunt in this forest to get some food. But some bandits were seen in there, too.",
        SOLVED: False,
        UP: "b3",
        DOWN: "d3",
        LEFT: "c2",
        RIGHT: "c4"
    },
    "c4": {
        ZONENAME: "Small Forest",
        DESCRIPTION: "A small forest next to your home.",
        EXAMINATION: "You could hunt in this forest to get some food. But some bandits were seen in there, too.",
        SOLVED: False,
        UP: "b4",
        DOWN: "d4",
        LEFT: "c3",
        RIGHT: ""
    },
    "d1": {
        ZONENAME: "Cave",
        DESCRIPTION: "Down in the south is a small Trollcave.",
        EXAMINATION: "You see some skelletons of deer and horses. Is it really a good idea to go into the cave?",
        SOLVED: False,
        UP: "c1",
        DOWN: "",
        LEFT: "",
        RIGHT: "d2"
    },
    "d2": {
        ZONENAME: "Cornfield",
        DESCRIPTION: "This cornfield belongs to the farm in the east. Maybe you can get some corn from it?",
        EXAMINATION: "Looks like this corn is better than what you have ever seen.",
        SOLVED: False,
        UP: "c2",
        DOWN: "",
        LEFT: "d1",
        RIGHT: "d3"
    },
    "d3": {
        ZONENAME: "Farm",
        DESCRIPTION: "This farm is owned by an old farmer.",
        EXAMINATION: "You have heard some scary stories about this farmer. Maybe he is not very nice?",
        SOLVED: False,
        UP: "c3",
        DOWN: "",
        LEFT: "d2",
        RIGHT: "d4"
    },
    "d4": {
        ZONENAME: "Bandit Hideout",
        DESCRIPTION: "This looks like some bandit hideout, which was not here the last time you were here.",
        EXAMINATION: "You cannot see any other human being. But you feel that you better move away.",
        SOLVED: False,
        UP: "c4",
        DOWN: "",
        LEFT: "d3",
        RIGHT: ""
    }
}

def print_location():
    print("#"*screen_width)
    print((" " * int((screen_width-len(myPlayer.location))/2)) + myPlayer.location.upper() + (" " * int((screen_width-len(myPlayer.location))/2)))
    print((" " * int((screen_width-len(zonemap[myPlayer.location][DESCRIPTION]))/2)) + zonemap[myPlayer.location][DESCRIPTION] + (" " * int((screen_width-len(zonemap[myPlayer.location][DESCRIPTION]))/2)))
    if zonemap[myPlayer.location][SOLVED]:
        print((" " * int((screen_width-len(zonemap[myPlayer.location][EXAMINATION]+"Examination"))/2)) + "Examination: " + zonemap[myPlayer.location][EXAMINATION] + (" " * int((screen_width-len(zonemap[myPlayer.location][EXAMINATION]+"Examination"))/2)))
    print("#"*screen_width)

def promt():
    print("You are here:")
    print_location()
    print("\n"+"="*len("What would you like to do?"))
    print("What would you like to do?\n")
    print("-"*len("What would you like to do?"))
    print(" "*(int((len("What would you like to do?")-len("examine or move?"))/2))+"examine or move?")
    print("-"*len("What would you like to do?")+"\n")

    action = input("> ")
    acceptable_locations = ["move","go","travel","walk","quit","examine","inspect","interact","look"]

    while action.lower() not in acceptable_locations:
        print("Unknown action. Try again. (move, quit, examine)")
        action = input("> ")

    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in ["move","go","travel","walk"]:
        player_move(action.lower())
    elif action.lower() in ["examine","inspect","interact","look"]:
        player_examine(action.lower())


def player_move(myAction):
    dest = input("Where do you like to move to? (up, down, left, right)\n> ")

    while dest not in ["up","down","left","right"]:
        print("Invalid entry!")
        dest = input("Where do you like to move to? (up, down, left, right)\n> ")

    if dest == "up":
        if zonemap[myPlayer.location][UP] != "":
            destination = zonemap[myPlayer.location][UP]
            movement(destination)
        else:
            stay(dest)
    elif dest == "down":
        if zonemap[myPlayer.location][DOWN] != "":
            destination = zonemap[myPlayer.location][DOWN]
            movement(destination)
        else:
            stay(dest)
    elif dest == "right":
        if zonemap[myPlayer.location][RIGHT] != "":
            destination = zonemap[myPlayer.location][RIGHT]
            movement(destination)
        else:
            stay(dest)
    elif dest == "left":
        if zonemap[myPlayer.location][LEFT] != "":
            destination = zonemap[myPlayer.location][LEFT]
            movement(destination)
        else:
            stay(dest)

def movement(destination):
    myPlayer.location = destination
    print("You have moved to the " + zonemap[myPlayer.location][ZONENAME] + ".")
    time.sleep(3)
    os.system("clear")

def stay(dir):
    directions = {"up":"north","down":"south","left":"west","right":"east"}
    print("You cannot move further " + directions[dir] + ".")
    time.sleep(3)
    os.system("clear")

def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("You have already been here.")
        print(zonemap[myPlayer.location][EXAMINATION])
        time.sleep(3)
        os.system("clear")
    else:
        print(zonemap[myPlayer.location][EXAMINATION])
        zonemap[myPlayer.location][SOLVED] = True
        solved_places[myPlayer.location] = True
        if all(solved_places.values()):
            myPlayer.game_over = True
        time.sleep(3)
        os.system("clear")


def intro():
    os.system("clear")
    question3 = "Welcome, " + myPlayer.name + " the " + myPlayer.play_class + ".\n"
    speach_manipulation(question3,0.05)
    speach_manipulation("Welcome to this fantasy world I created for you. ;)\n",0.05)
    speach_manipulation("I hope you will have some fun\n ... \n ... \n ...\n",0.15)
    speach_manipulation("Well, you are not the first adventurer here. There have been many before you. And to be honest, there will be many after you have ... ",0.05)
    speach_manipulation("passed away ... \n", 0.25)
    speach_manipulation("Now have some fun exploring the world. We will see each other when it's time to.\n",0.05)
    time.sleep(2)
    os.system("clear")

def end_screen():
    speach_manipulation("Congratulations, you have solved the complete game. I never thought you would be able to do this.",0.05)
    print("")
    speach_manipulation("I will get in touch with you soon. Wait for a sign from me. I think I have a good job for some strong adventurer like you.",0.04)

    time.sleep(5)
    os.system("clear")
    print("Made by laeberkaes")
    print("Hit me up at: https://github.com/laeberkaes/ or @laeberkaes:uraltemorla.xyz")

    time.sleep(5)
    sys.exit()

def game_loop():
    while not myPlayer.game_over:
        promt()

def speach_manipulation(text,speed):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

def setup_game():
    os.system("clear")
    question1 = "Hello what's your name?\n"
    speach_manipulation(question1,0.05)
    print("")
    myPlayer.name = input("> ").lower()

    os.system("clear")

    classes = ["warrior","mage","rogue"]
    question2 = "What Class do you want to play? (Warrior, Mage, Rogue)\n"
    speach_manipulation(question2,0.01)
    print("")
    player_class = input("> ").lower()
    print("")
    if player_class.lower() in classes:
        myPlayer.play_class = player_class
        print("You are now "+player_class)
    else:
        while player_class.lower() not in classes:
            print("No valid race.\n")
            player_race = input("> ").lower()
            if player_class.lower() in classes:
                myPlayer.race = input("> ").lower()
                print("You are now "+player_class)

    if myPlayer.play_class == "warrior":
        myPlayer.hp = 120
        myPlayer.mp = 20
    elif myPlayer.play_class == "mage":
        myPlayer.hp = 80
        myPlayer.mp = 80
    elif myPlayer.play_class == "rogue":
        myPlayer.hp = 100
        myPlayer.mp = 40

    intro()

    print("#"*screen_width+"\n")
    print("#" + (" "*int((screen_width-2-len("Let's start now"))/2))  + "Let's start now" + (" "*int((screen_width-2-len("Let's start now"))/2)) + "#\n")
    print("#"*screen_width+"\n")

    game_loop()

    end_screen()

title_screen()
