class Quest:
    def __init__(self, name, ep, player):
        self.name = name
        self.ep = ep
        self.solved = False
        player.quests.append(self)
        print("The Quest " + self.name + " was added to your active quests.")
