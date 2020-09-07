class Quest():
    def __init__(self):
        self.quest_name = "Example-Quest"
        self.quest_description = "Go X, do Y."
        self.tag = [", active", ", done"]
        self.quest_solved = False
        self.quest_goals = 2 #Falls 2 objectives erfüllt werden müssen.
        self.quest_gold_reward = 100
        self.quest_ep_reward = 100
        self.quest_potion_reward = 1 #man weiß ja nie, ob man sowas mal braucht
        self.quest_origin = "b1" #location quest giver
        self.quest_equipment_reward = ... #Spell / Armor / Weapon Objekte

    def show_quest(self):
        if self.quest_solved:
            print(self.quest_name + self.tag[1])
        else:
            print(self.quest_name + self.tag[0])
        
    def achieve_goal(self):
        self.quest_goals -= 1
        if self.quest_goals <= 0:
            self.quest_solved = True
    
    def get_reward(self,player):
        if self.quest_gold_reward > 0:
            player.gold += self.quest_gold_reward #Nicht die player.get_gold wegen anderem print
            print("You were rewarded with " + str(self.quest_gold_reward)+" Gold.")
        if self.quest_ep_reward > 0:
            player.get_ep(self.quest_ep_reward)
        if self.quest_potion_reward > 0: #setup für max 1 potoin als reward
            if self.quest_potion_reward == 1:
                print("You got a potion.")
            else:
                print("You got " + str(self.quest_equipment_reward) + " potions.")
            player.potions += self.quest_potion_reward
        if self.quest_equipment_reward != ...:
            if self.quest_equipment_reward.obj_type == "spell":
                player.spells.append(self.quest_equipment_reward)
                print("You were taught the spell: "+self.quest_equipment_reward.name)
            elif self.quest_equipment_reward.obj_type == "weapon":
                print("You received a weapon.")
                player.get_weapon(self.quest_equipment_reward)
            elif self.quest_equipment_reward.obj_type == "armor":
                print("You recieved armor.")
                player.get_armor(self.quest_equipment_reward)
    
    def solve_quest(self, player):
        if player.location == self.quest_origin and self.quest_goals <= 0:
            self.get_reward(player)