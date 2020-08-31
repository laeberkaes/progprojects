import random
from static import screen_width, clear
from game_object import Weapon, Armor


class NPC:
    def __init__(self, health, strength):
        self.health = health * random.randrange(10, 21)
        self.strength = strength * random.randrange(5, 11)

    def health_print(self):
        print("Enemy Health " + str(self.health))


class Bandit(NPC):
    def __init__(self):
        super().__init__(1, 1)  # set health + strength
        self.name = "Bandit"
        self.quip = ["Oi!", "Ow!", "Aaargh!", "Hng!"]
        self.accuracy = 0.65
        self.loot_chance = 0.80
        self.loot_level = 2
        self.ep_drop = random.randrange(30, 41)


class Orc(NPC):
    def __init__(self):
        super().__init__(3, 3)
        self.name = "Orc"
        self.quip = ["Uagh!", "Uff!", "Gnar!", "Grrrrr!"]
        self.accuracy = 0.75
        self.loot_chance = 40
        self.loot_level = 3
        self.ep_drop = random.randrange(50, 71)


class Giant(NPC):
    def __init__(self):
        super().__init__(10, 10)
        self.name = "Giant"
        self.quip = ["AAAAAH!", "Fi, Fai, Fo, Fumm!", "Hargh!"]
        self.accuracy = 0.9
        self.loot_chance = 50
        self.loot_level = 5
        self.ep_drop = random.randrange(100, 151)  # bei 100EP cap quasi ein garantiertes level"UP"

class Blacksmith():
    def __init__(self, player):
        self.symbol = " " * int((screen_width - len("@xxxx[{::::::::::::::::::::::::::::::>")) / 2) + "     [" + " " * int((len("::::::::::::::::::::::::::::::") - len("Mr. & Mrs. Smith")) / 2) + "Mr. & Mrs. Smith\n" + " " * int((screen_width - len("@xxxx[{::::::::::::::::::::::::::::::>")) / 2) + "@xxxx[{::::::::::::::::::::::::::::::>\n" + " " * int((screen_width - len("@xxxx[{::::::::::::::::::::::::::::::>")) / 2) + "     ["
        self.greeting = ["Welcome, traveller. How may I help you?", "Hey! You. Get over here. How about a nice new sword for you?", "Oi! You have some coin to spend?"]
        self.inventory = []
        self.set_inventory(player) #Auslage wird erstellt
        self.gold = random.randrange(150,301) #Gold für Ankäufe
        clear()
        print("#" * screen_width)
        print(self.symbol, sep="\n")
        print("#" * screen_width + "\n")
        print(random.choice(self.greeting))
        self.buy_or_sell(player) #Interaktion mit blacksmith wird gestartet

    def buy_or_sell(self, player):
        print("Do you want to buy or sell something?")
        a = input("> ")
        while a.lower() not in ["buy", "sell"]:
            print("What? I didn't catch that.")
            self.buy_or_sell(player)
        if a.lower() == "buy":
            self.buy_inventory(player)
        else:
            self.sell_inventory(player)


    def set_inventory(self, player): #Auslage wird erstellt
        lvl = player.level
        for i in range(3): #blacksmith bekommt 3 Gegenstände
            if random.random() < 0.6: #60% Chance auf Waffe in der Auslage, 50:50 besser?
                self.inventory.append(Weapon(lvl))
            else:
                self.inventory.append(Armor(lvl))

    def buy_inventory(self, player):
        clear()
        print("#" * screen_width)
        for i in range(3):
            o = self.inventory[i]
            if o.obj_type == "weapon":
                m = o.obj_type + ": " + o.name + ", damage: " + str(o.damage) + " " * (screen_width - (11 + len(o.obj_type + ": " + o.name + ", damage: " + str(o.damage)))) + "#\n" + "#" + " " * 10 + ">> Price: " + str(o.value) + " <<" + " " * (screen_width - (12 + len(">> Price: " + str(o.value) + " <<"))) + "#"
            else:
                m = o.obj_type + ": " + o.name + " for your " + o.slot + ", protection: " + str(o.protection) + " " * (screen_width - (11 + len(o.obj_type + ": " + o.name + " for your " + o.slot + ", protection: " + str(o.protection)))) + "#" + "\n" + "#" + " " * 10 + ">> Price: " + str(o.value) + " <<" + " " * (screen_width - (12 + len(">> Price: " + str(o.value) + " <<"))) + "#"
            print("#" + " " * 6 + str(i+1) + ". " + m)
        print("#" * screen_width) #TODO Hannes, mach das schön! :D
        print(" ")
        print("Which one do you want? (1, 2, 3, nothing)")
        valid_input = ["1", "2", "3", "nothing"]
        a_capital = input("> ")
        a = a_capital.lower() #Workaround fürs debuggen
        auswahl = -1 #Hilfsmittel :D
        while a not in valid_input:
            print("Please give me a normal answer, stranger.")
            self.buy_inventory(player)
        if a == "1":
            auswahl = 0
        elif a == "2":
            auswahl = 1
        elif a == "3":
            auswahl = 2
        elif a == "nothing": #oder direkt else, für die Lesbarkeit aber noch so
            print("Well, why do you waste my time then?")

        if auswahl >= 0:
            if self.inventory[auswahl] != " ":
                if player.gold > self.inventory[auswahl].value:
                    print("So you want the " + self.inventory[auswahl].name + ". Are you sure? (y/n)")
                    ax = input()
                    a2 = ax.lower() #debug workaround

                    if a2 == "y": #der eigentliche Kauf
                        if self.inventory[auswahl].obj_type == "weapon":
                            player.get_weapon(self.inventory[auswahl], p=False)
                            player.equip_weapon(self.inventory[auswahl])
                        else:
                            player.get_armor(self.inventory[auswahl], p=False)
                            player.equip_armor(self.inventory[auswahl])

                        player.gold -= self.inventory[auswahl].value #Bezahlvorgang
                        self.inventory[auswahl] = " " #Inventarslot wird geleert. Man könnte auch direkt nen neuen Gegenstand rein, aber weiß nich ob das so cool ist :D
                    else: #Quasi if a2 == "n" oder was anderes
                        (print("Your loss."))
                        self.buy_inventory(player)
                else:
                    print("You don't have the coin for that!")
                    self.buy_inventory(player)
            else:
                print("I got nothing there for you.")
                self.buy_inventory(player)

    def sell_inventory(self, player):
        clear()
        print("Not yet, traveller!") #TODO
        player.print_inventory()
        #Spielerinventar zeigen
        #Spieler wählt aus was verkauft werden soll
        #Wenn Schmied genug Gold hat, wird Gegenstand verkauft (player.drop_weapon oder .drop_armor könnte genutzt werden)
