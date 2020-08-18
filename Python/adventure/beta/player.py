class Player:
    def __init__(self, name: str):
        self.name = name
        self.play_class = ""
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = "b2"
        self.game_over = False
