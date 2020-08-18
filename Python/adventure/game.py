import cmd, textwrap, sys, os, time, random

class Player:
    def __init__(self, name: str):
        self.name = name
        self.play_class = ""
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = "b2"
        self.game_over = False

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
    print("#"*27)
    print("# Welcome to the Text RPG #")
    print("#"*27)
    print("          -play-           ")
    print("          -help-           ")
    print("          -quit-           ")
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
EXAMINATION = "examin"
SOLVED = False
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False, 'b1': False, 'b2': False, 'b3': False, 'b4': False, 'c1': False, 'c2': False, 'c3': False, 'c4': False, 'd1': False, 'd2': False, 'd3': False, 'd4': False}

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
        EXAMINATION: "You see some skelletons of deer and horses. Is it realy a good idea to go into the cave?",
        SOLVED: False,
        UP: "c1",
        DOWN: "",
        LEFT: "",
        RIGHT: "d2"
    },
    "d2": {
        ZONENAME: "Cornfield",
        DESCRIPTION: "This cornfield belongs to the farm in the east. Maybe you can get some corn from it?",
        EXAMINATION: "Looks like this corn is better then what you have ever seen.",
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
        DESCRIPTION: "This looks like some bandit hideout, which was not here the last time you were. here",
        EXAMINATION: "You cannot see any other human beeing. But you feel that you better move away.",
        SOLVED: False,
        UP: "c4",
        DOWN: "",
        LEFT: "d3",
        RIGHT: ""
    }
}

def print_location():
    print("\n" + ("#"*(4+len(myPlayer.location))))
    print("# " + myPlayer.location.upper() + " #")
    print("# " + zonemap[myPlayer.location][DESCRIPTION] + " #")
    print("\n" + ("#"*(4+len(myPlayer.location))))

def promt():
    print("\n"+"="*20)
    print("What would you like to do?")

    action = input("> ")
    acceptable_locations = ["move","go","travel","walk","quit","examine","inspect","interact","look"]

    while action.lower() not in acceptable_locations:
        print("Unknown action. Try again. (move, quit, examine, interact)")
        action = input("> ")

    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in ["move","go","travel","walk"]:
        player_move(action.lower())
    elif action.lower() in ["examine","inspect","interact","look"]:
        player_examin(action.lower())

def player_move(myAction):
    dest = input("Where do you like to move to?\n> ")

    if dest == "up":
        if zonemap[myPlayer.location][UP] != "":
            destination = zonemap[myPlayer.location][UP]
            movement(destination)
        else:
            print("You cannot move further north.")
    elif dest == "down":
        if zonemap[myPlayer.location][DOWN] != "":
            destination = zonemap[myPlayer.location][DOWN]
            movement(destination)
        else:
            print("You cannot move further south.")
    elif dest == "right":
        if zonemap[myPlayer.location][RIGHT] != "":
            destination = zonemap[myPlayer.location][RIGHT]
            movement(destination)
        else:
            print("You cannot move further west.")
    elif dest == "left":
        if zonemap[myPlayer.location][LEFT] != "":
            destination = zonemap[myPlayer.location][LEFT]
            movement(destination)
        else:
            print("You cannot move further east.")

def movement(destination):
    myPlayer.location = destination
    print("You have moved to the " + destination + ".")
    print_location()

def player_examin(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("You have already been here.")
        print(zonemap[myPlayer.location][EXAMINATION])
    else:
        print(zonemap[myPlayer.location][EXAMINATION])
        zonemap[myPlayer.location][SOLVED]=True

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
    myPlayer.name = input("> ").lower()

    classes = ["warrior","mage","rogue"]
    question2 = "What Class do you want to play? (Warrior, Mage, Rogue)\n"
    speach_manipulation(question2,0.01)
    player_class = input("> ").lower()
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

    ##### Intro #####
    question3 = "Welcome, " + myPlayer.name + " the " + myPlayer.play_class + ".\n"
    speach_manipulation(question3,0.05)
    speach_manipulation("Welcome to this fantasy world I created for you. ;)\n",0.05)
    speach_manipulation("I hope you will have some fun\n ... \n ... \n ...\n",0.15)
    speach_manipulation("Well, you are not the first adventurer here. There have been many before you. And to be honest, there will be many after you have ... ",0.05)
    speach_manipulation("passed away ... \n", 0.25)
    speach_manipulation("Now have some fun exploring the world. We will see each other when it's time to.\n",0.05)
    time.sleep(2)
    os.system("clear")

    print("#"*(4+len("Let's start now"))+"\n")
    print("# Let's start now #\n")
    print("#"*(4+len("Let's start now"))+"\n")

    game_loop()

title_screen()
