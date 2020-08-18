import random

class Weapon:
    def __init__(self,name,damage,value,health=100):
        self.name = name
        self.damage = damage
        self.value = value
        self.health = health

heavy = [Weapon(name,damage,value) for name in ["Streitaxt","Kriegshammer","Kriegsarmbrust"] for damage in [15,10,20] for value in [11,12,9]]
medium = [Weapon(name,damage,value) for name in ["Schwer","Speer","Bogen"] for damage in [12,8,10] for value in [5,7,6]]
light = [Weapon(name,damage,value) for name in ["Dolch","Knüppel","Harke"] for damage in [4,6,2] for value in [1,2,3]]

def getWeapon(level):
    if level<3:
        return random.choice(light)
    if level>7:
        return random.choice(heavy)
    else:
        return random.choice(medium)