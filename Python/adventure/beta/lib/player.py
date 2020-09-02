import random
import time

from lib.static import screen_width, clear, speech_manipulation
from lib import game_object, npc


class Player:
    def __init__(self):
        self.name = ""
        self.play_class = ""
        self.health_max = 0
        self.health_cur = self.health_max
        self.mp_cur_max = []
        self.ep = 0
        self.level = 1
        self.status_effects = []
        self.location = "b2"
        self.game_over = False
        self.weapon = game_object.Weapon(self.level)
        self.weapon.equipped = True
        self.potions = 1
        self.inventory = {"weapons": [self.weapon], "armor": [], "misc": dict()}
        self.spells = list()
        self.gold = 10
        self.head = "empty"  # "empty" gebraucht für Player.equip_armor()
        self.chest = "empty"
        self.arm = "empty"
        self.leg = "empty"
        self.armor = 0
        self.pos = (0.95, 0.05, 0)

    # HUD-Optionen --------------------------------------------------------
    def health(self):
        print("Your health: " + str(self.health_cur) + "/" + str(self.health_max) + " HP")
        print("Your mana: " + str(self.mp_cur_max[0]) + "/" + str(self.mp_cur_max[1]) + " MP")
        
    def print_inventory(self, interactive=False):
        clear()
        print("#" * screen_width)
        print(
            "=" * int((screen_width - len("WEAPONS")) / 2) + "WEAPONS" + "=" * int((screen_width - len("WEAPONS")) / 2))
        for weapon in self.inventory["weapons"]:
            if weapon.equipped == True:
                print("EQUIPPED: " + str(weapon)[13:])
            else:
                print(str(weapon)[13:])
        print("")
        print("=" * int((screen_width - len("ARMOR")) / 2) + "ARMOR" + "=" * int((screen_width - len("ARMOR")) / 2))
        for armor in self.inventory["armor"]:
            if armor.equipped == True:
                print("EQUIPPED: A" + str(armor)[6:])
            else:
                print("A" + str(armor)[6:])
        print("")
        print(
            "=" * int((screen_width - len("POTIONS")) / 2) + "POTIONS" + "=" * int((screen_width - len("POTIONS")) / 2))
        if self.potions == 1:
            print("You have " + str(self.potions) + " potion.")
        if self.potions > 1:
            print("You have " + str(self.potions) + " potions.")
        print("")
        print("=" * int((screen_width - len("MISC")) / 2) + "MISC" + "=" * int((screen_width - len("MISC")) / 2))
        for misc in self.inventory["misc"]:
            print(misc + ": " + str(self.inventory["misc"][misc]))
        print("")

        if not interactive:
            print("Press ENTER to continue.")
            input()
            clear()

    def show_stats(self):
        clear()
        print("#" * screen_width)
        print("")
        print("Name:" + " " * (20 - len("Name:")) + self.name)
        print("Class:" + " " * (20 - len("Class:")) + self.play_class)
        print("Level:" + " " * (20 - len("Level:")) + str(self.level))
        print("Gold:" + " " * (20 - len("Gold:")) + str(self.gold))  # Gold ergänzt
        print("EP:" + " " * (20 - len("EP:")) + str(self.ep))
        print("Health:" + " " * (20 - len("Health:")) + str(self.health_cur) + "/" + str(self.health_max))
        print("Mana:" + " " * (20 - len("Mana:")) + str(self.mp_cur_max[0]) + "/" + str(self.mp_cur_max[1]))
        print("Armor:" + " " * (20 - len("Armor:")) + str(self.armor))
        print(
            "Weapon:" + " " * (20 - len("Weapon:")) + self.weapon.name + " with " + str(self.weapon.damage) + " damage")
        print("")
        print("#" * screen_width)
        print("")
        print("Press ENTER to continue.")
        input()
        clear()

    def write_notebook(self):
        clear()
        print("#" * screen_width)
        print("#" + " " * int((screen_width - len("NOTEBOOK")) / 2 - 1) + "NOTEBOOK" + " " * int(
            (screen_width - len("NOTEBOOK")) / 2 - 1) + "#")
        print("#" * screen_width)
        print("\nYou can escape the notebook with writing 'END' in the last line.")
        print("\nOlder Entries:\n")
        with open("../notebook.txt", "r") as notebook:
            for line in notebook.readlines():
                print("> " + line, end="")

        print("\nAppend the following lines:\n")

        with open("../notebook.txt", "a") as notebook:
            while True:
                inp = input("> ")
                if inp.strip() == "END":
                    break
                else:
                    notebook.write(inp + "\n")

    def show_notebook(self):
        clear()
        print("#" * screen_width)
        print("#" + " " * int((screen_width - len("NOTEBOOK")) / 2 - 1) + "NOTEBOOK" + " " * int(
            (screen_width - len("NOTEBOOK")) / 2 - 1) + "#")
        print("#" * screen_width)
        with open("../notebook.txt", "r") as notebook:
            for line in notebook.readlines():
                print("> " + line, end="")

    # Loot-Optionen --------------------------------------------------------

    def get_gold(self, amount):
        self.gold += amount
        print("You found " + str(amount) + " gold.")

    def get_potion(self):
        self.potions += 1
        print("You find a potion.")

    def get_ep(self, amount):
        self.ep += amount
        print("You get " + str(amount) + " experience.")
        if self.ep > 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health_max += 20
        self.ep -= 100
        self.pos = (
            self.pos[0] - (self.level * 0.05), self.pos[1] + (self.level * 0.1), self.pos[2] + (self.level * 0.05))
        speech_manipulation(
            "Congratulations, you leveled up. You are now a level " + str(self.level) + " " + self.play_class + ".\n",
            0.03)
        speech_manipulation("You have " + str(self.health_max) + " max HP and " + str(self.mp_cur_max[1])+ " max MP.", 0.03)
        time.sleep(2)
        while self.ep > 100:
            self.level_up()

    # Waffen-Optionen --------------------------------------------------------
    def get_weapon(self, weapon, p=True):
        if p == True:
            print("You put " + weapon.name + " in your backpack.")
        self.inventory["weapons"].append(weapon)

    def drop_weapon(self, weapon):  # Future Feature
        for num,w in enumerate(self.inventory["weapons"]):
            if weapon.name == w.name and weapon.damage == w.damage and weapon.durability == w.durability and not w.equipped:
                print("You dropped: " + w.name)
                self.inventory["weapons"].pop(num)  # Problem: popped evtl. identische Waffen.

    def equip_weapon(self, weapon):
        self.weapon.equipped = False
        self.weapon = weapon
        self.weapon.equipped = True
        print("You wield: " + self.weapon.name)

    # Rüstungs-Optionen --------------------------------------------------------
    def get_armor(self, armor, p=True):
        if p == True:
            print("You put " + armor.name + " in your backpack.")
        self.inventory["armor"].append(armor)

    def drop_armor(self, armor):  # Future Feature
        for num,a in enumerate(self.inventory["armor"]):
            if armor.slot == a.slot and armor.name == a.name and armor.protection == a.protection and armor.durability == a.durability and not a.equipped:
                print("You dropped: " + a.name)
                self.inventory["armor"].pop(num)

    def equip_armor(self, armor):
        if armor.slot == "head":
            if self.head != "empty":  # unequip falls bereits vorhanden, sodass Rüstungswert sinkt.
                self.armor -= self.head.protection
                self.head.equipped = False
            self.armor += armor.protection
            self.head = armor
            self.head.equipped = True
        elif armor.slot == "chest":
            if self.chest != "empty":
                self.armor -= self.chest.protection
                self.chest.equipped = False
            self.armor += armor.protection
            self.chest = armor
            self.chest.equipped = True
        elif armor.slot == "leg":
            if self.leg != "empty":
                self.armor -= self.leg.protection
                self.leg.equipped = False
            self.armor += armor.protection
            self.leg = armor
            self.leg.equipped = True
        elif armor.slot == "arm":
            if self.arm != "empty":
                self.armor -= self.arm.protection
                self.arm.equipped = False
            self.armor += armor.protection
            self.arm = armor
            self.arm.equipped = True

    def use_potion(self):
        if self.potions > 0:
            self.health_cur += 25
            if self.health_cur > self.health_max:
                self.health_cur = self.health_max
            self.potions -= 1
            print("Ahhhh this feels good. You feel new power filling up your body. (HP +25)")
        else:
            print("You don't have any potions left.")
        time.sleep(2)
        clear()

    def get_object(self, obj):
        if obj not in self.inventory["misc"] and type(obj) == str:
            self.inventory["misc"][obj] = 1
        elif obj in self.inventory["misc"]:
            self.inventory["misc"][obj] += 1
        elif obj.obj_type() == "weapon":
            self.inventory["weapons"].append(obj)
        elif obj.obj_type() == "armor":
            self.inventory["armor"].append(obj)

    # Interaktionen --------------------------------------------------------
    def fishing(self):
        if self.location in ["a4", "c1", "c2"] and "fishingrot" in self.inventory:
            p = random.random()
            if p > 0.95:
                print("You get an old, stinky boot. *urgh*")
                if "Old, stinky boot" not in self.inventory:
                    self.inventory["Old, stinky boot"] = 1
                else:
                    self.inventory["Old, stinky boot"] += 1
            elif p > 0.5:
                print("You got a nice, fresh fish")
                if "fish" not in self.inventory:
                    self.inventory["fish"] = 1
                else:
                    self.inventory["fish"] += 1

            else:
                print("You got nothing for now. But you can fish all day long.")

        else:
            print("Well you can try to fish here. But you will not get any more than some dirt.")

        time.sleep(2)
        clear()

    def getCorn(self):
        if self.location == "d2":
            p = random.random()
            if p > 0.25:
                print("You get some nice corn.")
                if "bag of corn" not in self.inventory["misc"]:
                    self.inventory["misc"]["bag of corn"] = 1
                else:
                    self.inventory["misc"]["bag of corn"] += 1
            else:
                print("Baaah. You better not take this corn with you.")
        else:
            print("Well you cannot get corn out of this place.")

        time.sleep(2)
        clear()

    def hunting(self):
        if self.location in ["b3", "b4", "c3"]:
            p = random.random()
            if p > 0.95:
                print("You get some nice deer. This will give you good food for some days.")
                if "meat" not in self.inventory:
                    self.inventory["meat"] = 10
                else:
                    self.inventory["meat"] += 10
            elif p > 0.6:
                print("You get some rabbits and a small boar.")
                if "meat" not in self.inventory:
                    self.inventory["meat"] = 7
                else:
                    self.inventory["meat"] += 7
            else:
                print("Well you are out of luck for now.")
        else:
            print("You will find no wild animals in this area. Try your luck in the eastern forest.")
        time.sleep(2)

    def buy_equipment(self):
        if self.location == "b1":
            npc.Blacksmith(self)
            
    def learn_spell(self):
        if self.location == "c4":
            npc.Magician(self)

# Hier wird dann ein neuer Spieler erzeugt, der von anderen Dateien importiert werden kann.
myPlayer = Player()
