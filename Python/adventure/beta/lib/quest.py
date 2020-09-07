class Quest:
    def __init__(self, name, description, ep, gold, potions, equipment, origin, player):
        self.name = name
        self.description = description
        self.ep_reward = ep
        self.gold_reward = gold
        self.potion_reward = potions
        self.equipment_reward = equipment
        self.quest_origin = origin
        self.solved = False
        player.quests.append(self)
        print("The Quest " + self.name + " was added to your active quests.")

    def __repr__(self):
        if not self.solved:
            return self.name + ", active."
        else:
            return self.name + ", solved."
