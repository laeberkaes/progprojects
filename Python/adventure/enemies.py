import weapon, random

class enemy():
    def __init__(self,race,size,level,health=100):
        self.race = race
        self.size = size
        self.level = level
        self.weapon = weapon.getWeapon(level)
        self.health_max = health*size
        self.healt_cur = self.health_max

    def makeSound(self):
        return random.choice(["Roaaar","Arrghhh","Ajajajajaj","Huga"])

    def attack(self):
        return self.weapon.damage