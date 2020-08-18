class Player:
    def __init__(self):
        self.name = ""
        self.play_class = ""
        self.hp = 0
        self.mp = 0
        self.ep = 0
        self.level = 1
        self.status_effects = []
        self.location = "b2"
        self.game_over = False
        self.weapon = weapon.getWeapon(self.level)
        self.potions = 1
        self.inventory = dict()
        self.gold = 10

    def levelUp(self):
        self.level += 1
        self.health_max += 20
        self.ep -= 100
        POSSIBILITIES = [POSSIBILITIES[0]-(self.level*0.05),POSSIBILITIES[1]+(self.level*0.1),POSSIBILITIES[2]+(self.level*0.05)]

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
        if self.potions > 0
            self.health_cur += 25
            if self.health_cur > self.health_max:
                self.health_cur = self.health_max
        self.potions -= 1

    def getProtect(self,amount):
        self.protect += amount

    def getObject(self,object):
        self.inventory.append(object)

    def fishing(self):
        if self.location in ["a4","c1","c2"] and "fishingrot" in self.inventory:
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

    def getCorn(self):
        if self.location == "d2":
            p = random.random()
            if p > 0.25:
                print("You get some nice corn.")
                if "corn" not in self.inventory:
                    self.inventory["corn"] = 1
                else:
                    self.inventory["corn"] += 1
            else:
                print("Baaah. You better not take this corn with you.")
