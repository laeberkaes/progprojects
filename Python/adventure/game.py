import cmd, textwrap, sys, os, time, random

screen_width = 100

class Player:
    def __init__(self, name: str):
        self.name = name
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = "start"

myPlayer = Player("Testname")

##### Title #####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
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

def help_manu():
    print("#"*27)
    print("# Welcome to the Text RPG #")
    print("#"*27)
    print(" -- Use up, down, left, right to move")
    print(" -- Type your commands to do them")
    print(" -- Good luck and have fun!")
    title_screen()
    title_screen_selections()


##### Game #####
def start_game():


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
        ZONENAME = "Town Marketplace",
        DESCRIPTION = "This is the marketplace of your hometown.",
        EXAMINATION = "You can see some stalls selling different things.",
        SOLVED = False,
        UP = "",
        DOWN = "b1",
        LEFT = "",
        RIGHT = "a2"
    },
    "a2": {
        ZONENAME = "Towngate",
        DESCRIPTION = "This is the gate of your hometown.",
        EXAMINATION = "The gate is locked at night. You have to be nice to the guardsmen, if you try to enter at night.",
        SOLVED = False,
        UP = "",
        DOWN = "b2",
        LEFT = "a1",
        RIGHT = "a3"
    },
    "a3": {
        ZONENAME = "Grassland",
        DESCRIPTION = "Nothing but green grass.",
        EXAMINATION = "I'm serious. It's nothing but grass.",
        SOLVED = False,
        UP = "",
        DOWN = "b3",
        LEFT = "a2",
        RIGHT = "a4"
    },
    "a4": {
        ZONENAME = "Little Pond",
        DESCRIPTION = "This is a cute little pond.",
        EXAMINATION = "With a fishingrot you could get some fish out of it.",
        SOLVED = False,
        UP = "",
        DOWN = "b4",
        LEFT = "a3",
        RIGHT = ""
    },
    "b1": {
        ZONENAME = "Blacksmith",
        DESCRIPTION = "This is your local blacksmith.",
        EXAMINATION = "Here you can buy/sell some weapons or protections",
        SOLVED = False,
        UP = "a1",
        DOWN = "c1",
        LEFT = "",
        RIGHT = "b2"
    },
    "b2": {
        ZONENAME = "Home",
        DESCRIPTION = "This is your home!",
        EXAMINATION = "Your home looks cosy.",
        SOLVED = False,
        UP = "a2",
        DOWN = "c2",
        LEFT = "b1",
        RIGHT = "b3"
    },
    "b3": {
        ZONENAME = "",
        DESCRIPTION = "description",
        EXAMINATION = "examin",
        SOLVED = False,
        UP = "up",
        DOWN = "down",
        LEFT = "left",
        RIGHT = "right"
    },
    "b4": {
        ZONENAME = "",
        DESCRIPTION = "description",
        EXAMINATION = "examin",
        SOLVED = False,
        UP = "up",
        DOWN = "down",
        LEFT = "left",
        RIGHT = "right"
    },
    "c1": {
        ZONENAME = "",
        DESCRIPTION = "description",
        EXAMINATION = "examin",
        SOLVED = False,
        UP = "up",
        DOWN = "down",
        LEFT = "left",
        RIGHT = "right"
    },
    "c2": {
        ZONENAME = "",
        DESCRIPTION = "description",
        EXAMINATION = "examin",
        SOLVED = False,
        UP = "up",
        DOWN = "down",
        LEFT = "left",
        RIGHT = "right"
    },
    "c3": {
        ZONENAME = "",
        DESCRIPTION = "description",
        EXAMINATION = "examin",
        SOLVED = False,
        UP = "up",
        DOWN = "down",
        LEFT = "left",
        RIGHT = "right"
    },
    "c4": {
        ZONENAME = "",
        DESCRIPTION = "description",
        EXAMINATION = "examin",
        SOLVED = False,
        UP = "up",
        DOWN = "down",
        LEFT = "left",
        RIGHT = "right"
    },
    "d1": {
        ZONENAME = "",
        DESCRIPTION = "description",
        EXAMINATION = "examin",
        SOLVED = False,
        UP = "up",
        DOWN = "down",
        LEFT = "left",
        RIGHT = "right"
    },
    "d2": {
        ZONENAME = "",
        DESCRIPTION = "description",
        EXAMINATION = "examin",
        SOLVED = False,
        UP = "up",
        DOWN = "down",
        LEFT = "left",
        RIGHT = "right"
    },
    "d3": {
        ZONENAME = "",
        DESCRIPTION = "description",
        EXAMINATION = "examin",
        SOLVED = False,
        UP = "up",
        DOWN = "down",
        LEFT = "left",
        RIGHT = "right"
    },
    "d4": {
        ZONENAME = "",
        DESCRIPTION = "description",
        EXAMINATION = "examin",
        SOLVED = False,
        UP = "up",
        DOWN = "down",
        LEFT = "left",
        RIGHT = "right"
    }
}
