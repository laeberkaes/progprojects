import random
#import game.py
import random
screen_width = 60
class Weapon():
    def __init__(self, level):
        adjective = ["Dirty", "Crooked", "Big", "Old", "Shiny", "Bloody", "Sharp"]
        subst = [" Dagger", " Hammer", " Sword", " Bow", " Spear", " Morning Star", " Club", " Axe"]
        self.obj_type = "weapon"
        self.level = level
        self.value = random.randrange(5,15)*self.level #Gold-Wiederverkaufswert
        self.name = random.choice(adjective) + random.choice(subst)
        self.damage = random.randrange(3,6)*level #=> 3-5
        self.durability = [20,20] # used in percent --> multiply with damage
        self.broken = False
        self.equipped = False

    def __repr__(self):
        return "Your weapon: "+self.name+", with "+str(self.damage)+" damage"

class Armor():
    def __init__(self,level):
        self.obj_type = "armor"  
        self.level = level
        self.equipped = False
        self.durability = [10,10] #Übersteht 10 Angriffe
        self.broken = False
        self.value = random.randrange(5,15)*self.level #Gold-Wiederverkaufswert

        #Rüstungsname wird festgelegt (und slot angezeigt)
        adjective = ["Dirty", "Crooked", "Big", "Old", "Shiny", "Bloody"]
        subst = [" Plate Armor", " Chain Armor", " Leather Armor"] #Future Feature: Typ der Rüstung erhöht Wert (Plate > Chain > Leather)
        self.name = random.choice(adjective) + random.choice(subst)

        #Rüstungsattribute werden festgelegt
        slot_names = ["head","chest","leg","arm"]
        slot_modifier = [2,3,1,1] #Rüstungswert im Verhältnis zu slot (head = 2, chest = 3, etc.). Auch zusammen als dict denkbar.
        slot_choice = random.randrange(0,len(slot_names)) #wählt Index von names und modifier
        self.slot = slot_names[slot_choice]
        self.protection = slot_modifier[slot_choice]*level


    def __repr__(self):
        return "Your armor for the " + self.slot + ": " + self.name + ", with " + str(self.protection) + " protection."


# class Blacksmith():
#     def __init__(self, player):
#         self.symbol = " \n     [\n@xxxx[{::::::::::::::::::::::::::::::>\n     ["
#         self.greeting = ["Welcome, traveller. How may I help you?", "Hey! You. Get over here. How about a nice new sword for you?", "Oi! You have some coin to spend?"]
#         self.inventory  = []
#         self.set_inventory(player) #Auslage wird erstellt
#         self.gold = random.randrange(150,301) #Gold für Ankäufe
#         print(self.symbol, sep="\n")
#         print(random.choice(self.greeting))
#         self.buy_or_sell(player) #Interaktion mit blacksmith wird gestartet
#
#     def buy_or_sell(self, player):
#         print("Do you want to buy or sell something?")
#         a = input("> ")
#         while a.lower() not in ["buy", "sell"]:
#             print("What? I didn't catch that.")
#             self.buy_or_sell(player)
#         if a.lower() == "buy":
#             self.buy_inventory(player)
#         else:
#             self.sell_inventory(player) # TODO: methode erstellen
#
#
#     def set_inventory(self, player): #Auslage wird erstellt
#         lvl = player.level
#         for i in range(3): #blacksmith bekommt 3 Gegenstände
#             if random.random() < 0.6: #60% Chance auf Waffe in der Auslage, 50:50 besser?
#                 self.inventory.append(Weapon(lvl))
#             else:
#                 self.inventory.append(Armor(lvl))
#
#     def buy_inventory(self, player):
#         print("#" * screen_width)
#         for i in range(len(self.inventory)):
#             o = self.inventory[i]
#             if o.obj_type == "weapon":
#                 m = o.obj_type + ": " + o.name + ", damage: " + str(o.damage) + "\nPrice: " + str(o.value)
#             else:
#                 m = o.obj_type + ": " + o.name + " for your " + o.slot + ", protection: " + str(o.protection) + "\nPrice: " + str(o.value)
#             print(str(i+1) + ". " + m)
#         print("#" * screen_width) #TODO Hannes, mach das schön! :D
#         print(" ")
#         print("Which one do you want? (1, 2, 3, nothing)")
#         valid_input = ["1", "2", "3", "nothing"]
#         a_capital = input()
#         a = a_capital.lower() #Workaround fürs debuggen
#         auswahl = -1 #Hilfsmittel :D
#         while a not in valid_input:
#             print("Please give me a normal answer, stranger.")
#             self.buy_inventory(player)
#         if a == "1":
#             auswahl = 0
#         elif a == "2":
#             auswahl = 1
#         elif a == "3":
#             auswahl = 2
#         elif a == "nothing": #oder direkt else, für die Lesbarkeit aber noch so
#             print("Well, why do you waste my time then?")
#
#         if auswahl >= 0:
#             if self.inventory[auswahl] != " ":
#                 if player.gold > self.inventory[auswahl].value:
#                     print("So you want the " + self.inventory[auswahl].name + ". Are you sure? (y/n)")
#                     ax = input()
#                     a2 = ax.lower() #debug workaround
#
#                     if a2 == "y": #der eigentliche Kauf
#                         if self.inventory[auswahl].obj_type == "weapon":
#                             player.get_weapon(self.inventory[auswahl], p=False)
#                             player.equip_weapon(self.inventory[auswahl])
#                         else:
#                             player.get_armor(self.inventory[auswahl], p=False)
#                             player.equip_armor(self.inventory[auswahl])
#
#                         player.gold -= self.inventory[auswahl].value #Bezahlvorgang
#                         self.inventory[auswahl] = " " #Inventarslot wird geleert. Man könnte auch direkt nen neuen Gegenstand rein, aber weiß nich ob das so cool ist :D
#                     else: #Quasi if a2 == "n" oder was anderes
#                         (print("Your loss."))
#                         self.buy_inventory(player)
#                 else:
#                     print("You don't have the coin for that!")
#                     self.buy_inventory(player)
#             else:
#                 print("I got nothing there for you.")
#                 self.buy_inventory(player)
#
#     def sell_inventory(self, player):
#         print("Not yet, traveller!") #TODO
#         #Spielerinventar zeigen
#         #Spieler wählt aus was verkauft werden soll
#         #Wenn Schmied genug Gold hat, wird Gegenstand verkauft (player.drop_weapon oder .drop_armor könnte genutzt werden)

