import weapon
import random

class Player:
    def __init__(self,name=random.choice(["Alouis","Horst","Adalbert","Hildegard","Yvonne","Igerne"])):
        self.level = 1
        self.name = name
        self.ep = 0
        self.health_max = 100
        self.health_cur = self.health_max
        self.protect = 0
        self.gold = 20
        self.potion = 1
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

    def getProtext(self,amount):
        self.protect += amount
