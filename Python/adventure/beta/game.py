import math
import random
import sys
import time

from lib import game_object
from lib.map import zonemap, solved_places
from lib.npc import Bandit, Orc, Giant
from lib.player import myPlayer
from lib.static import clear, screen_width, speech_manipulation


def title_screen_selections():
    option = input("> ")
    if option.lower() == "play":
        setup_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()

    while option.lower() not in ["play", "help", "quit"]:
        print("Invalid command. Type 'play', 'help', 'quit'")
        title_screen_selections()


def title_screen():
    clear()
    print("#" * screen_width)
    print("#" + (" " * int((screen_width - len("Welcome to the Text RPG")) / 2)) + "Welcome to the Text RPG" + (
            " " * int((screen_width - 2 - len("Welcome to the Text RPG")) / 2)) + "#")
    print("#" + "=" * (screen_width - 2) + "#")
    print("#" + (" " * int((screen_width - 6) / 2)) + "-play-" + (" " * int((screen_width - 9) / 2)) + "#")
    print("#" + (" " * int((screen_width - 6) / 2)) + "-help-" + (" " * int((screen_width - 9) / 2)) + "#")
    print("#" + (" " * int((screen_width - 6) / 2)) + "-quit-" + (" " * int((screen_width - 9) / 2)) + "#")
    print("#" * screen_width + "\n")
    title_screen_selections()


def help_menu():
    clear()
    print("#" * screen_width)
    print(("=" * int((screen_width - len("HELP MENU")) / 2)) + "HELP MENU" + (
            "=" * int((screen_width - len("HELP MENU")) / 2)))
    print("#" * screen_width)
    print("")
    print(" -- You can always decide to 'examine' a location or 'move' to another.")
    print(" -- You can always see your inventory with 'show inventory' and show your stats with 'show stats'")
    print("-- If you examine a location you may trigger a random encounter and you can 'fish', 'hunt'. 'rest', "
          "'learn' or 'get corn'")
    print(" -- If you move, you can decide to move 'up', 'down', 'left' or 'right'")
    print("")
    print("Press ENTER to continue.")
    input()
    title_screen()
    title_screen_selections()


def fight_setup(player, poss):
    clear()
    print("#" * screen_width)
    print(" " * int((screen_width - len("FIGHT")) / 2) + "FIGHT")
    print("#" * screen_width)
    x = random.random()
    if x < poss[0]:
        enemy = Bandit()
    elif poss[0] < x < poss[0] + poss[1]:
        enemy = Orc()
    else:
        enemy = Giant()  # else, solange nur 3 mögliche Gegner
    fight(player, enemy, zonemap)


def fight(player, enemy, zonemap):
    print("                 ")
    print("You fight against: " + enemy.name)
    enemy.health_print()
    player.health_mana()
    # Auswahl für Kampf --------------------------------------------------
    a = fight_options().lower()  # das geht sicher eleganter
    valid_options = ["attack", "heal", "magic", "flee", "show stats", "quit"]  # In den fight_options() immer ergänzen
    while a not in valid_options:
        print("Please use a valid answer.")
        a = fight_options().lower()
    # Spieler-Angriff --------------------------------------------------
    if a == "attack":
        player_attack(player, enemy, zonemap)
    # Spieler-Magie --------------------------------------------------
    elif a == "magic":
        use_magic(player, enemy, zonemap)
    # Spieler-Andere Optionen --------------------------------------------------
    elif a == "heal":
        player.use_potion()
        activate_status_effect(player, enemy, zonemap)
    elif a == "flee":
        flee_from_fight(player, enemy, zonemap)
    elif a == "show stats":
        player.show_stats()
        fight(player, enemy, zonemap)
    elif a == "quit":  # ganz Spiel aus im Kampf?
        sys.exit()


def player_attack(player, enemy, zonemap):
    if not player.weapon.broken:
        print("You attack with your weapon and do " + str(player.weapon.damage) + " damage.")
        player.weapon.durability[0] -= 1
        print("Weapon durability: " + str((player.weapon.durability[0] / player.weapon.durability[1]) * 100) + "%")
        if player.weapon.durability[0] == 0:
            player.weapon.broken = True
            print("Your weapon broke! Repair it at a Blacksmith's.")
        enemy.health -= player.weapon.damage
    else:
        broken_damage = math.ceil(
            player.weapon.damage * 0.1)  # Immer aufgerundet (aka 1,2 wird 2), 10% Waffenschaden falls kaputt
        print("Your weapon is broken. You only do " + str(broken_damage) + " damage.")
        enemy.health -= broken_damage
    print("enemy: " + random.choice(enemy.quip))
    check_victory(player, enemy, zonemap)


def use_magic(player, enemy, zonemap):
    if player.spells:
        i = 0
        print("#" * screen_width)
        print("Your spells:")
        for spell in player.spells:
            if spell.status_effect == "healing":
                print(str(i + 1) + ". " + spell.name + " with " + str(spell.damage) + " healing")
            else:
                print(str(i + 1) + ". " + spell.name + " with " + str(spell.damage) + " damage")
            i += 1
        print("Which one do you want to cast? (choose number)")
        a = str(input("> ")).lower()
        valid_choices = [str(k + 1) for k in range(i)]
        if a not in valid_choices:
            print("You misspoke your spell and failed to cast it. Try again.")
            use_magic(player, enemy, zonemap)
        else:
            cast_spell = ""
            for cast in list(enumerate(valid_choices)):
                if cast[1] == a:
                    cast_spell = player.spells[cast[0]]
        # This is where the magic happens... -----------------------------------------
        if player.mp_cur_max[0] >= cast_spell.mana_cost:  # genug mana?
            player.mp_cur_max[0] -= cast_spell.mana_cost
            if cast_spell.status_effect == "healing":  # Selbstheilung
                amount = player.health_max - player.health_cur
                if amount == 0:
                    print("You are at full health.")
                elif amount < cast_spell.damage:
                    print("You heal for " + str(amount) + " HP.")
                    player.health_cur += amount
                else:
                    print("You heal yourself for " + str(cast_spell.damage) + " HP.")
                    player.health_cur += cast_spell.damage
                activate_status_effect(player, enemy, zonemap)  # Status-Schaden nach Selbstheilung
            else:  # spell ist NICHT healing -->
                print("You cast " + cast_spell.name)
                if cast_spell.damage > 0:  # Spell hat Sofort-Schaden
                    print("Your enemy takes " + str(cast_spell.damage) + " damage")
                    enemy.health -= cast_spell.damage
                if not enemy.active_effect:  # Noch kein Effekt vorhanden
                    if random.random() < cast_spell.status_chance:
                        print("Your enemy suffers from " + cast_spell.status_effect)
                        enemy.active_effect.append(cast_spell)  # Gegner bekommt Spell übergeben (wegen Effekt)
                    else:
                        print("You failed to apply any status effects.")
                else:
                    print("Your enemy is already under a spell, you don't apply any effects.")
                check_victory(player, enemy, zonemap)
        else:
            print("You don't have enough mana, you cast " + random.choice(
                ["butterflies", "bubbles", "hot air", "a flower"]) + " instead.")
            fight(player, enemy, zonemap)
    else:
        print("You haven't learnt any spells.")
        fight(player, enemy, zonemap)


def flee_from_fight(player, enemy, zonemap):
    if random.random() < 0.6:  # 60% Fluchtchance (fix? Future-Feature)
        print("You got away.")
        print("You don't get any rewards.")

    else:
        print("Your enemy won't let you go!")
        activate_status_effect(player, enemy, zonemap)


def enemy_attack(player, enemy, zonemap):
    # Gegner-Angriff --------------------------------------------------
    if random.random() < enemy.accuracy:  # Spieler nimmt Schaden
        if player.armor == 0:  # Wenn keine Rüstung anliegt
            print("Your enemy attacks and does " + str(enemy.strength) + " damage.")
            player.health_cur -= enemy.strength
        else:  # Es gibt Rüstung
            print("Your enemy attacks and does " + str(enemy.strength - player.armor) + " damage.")
            player.health_cur -= enemy.strength - player.armor
            # Es wird ein Index eines zufälligen aber angelegten Rüstungsteils gewählt
            x = player.inventory["armor"][
                random.choice([a for a, b in list(enumerate(player.inventory["armor"])) if b.equipped == True])]
            x.durability[0] -= 1
            print("Your " + x.slot + " armor was hit.")
            print("Durability: " + str((x.durability[0] / x.durability[1]) * 100) + "%")
        if player.health_cur <= 0:
            print("Your enemy defeated you!")
            game_over()
        else:
            fight(player, enemy, zonemap)
    else:  # Spieler nimmt keinen Schaden
        print("Your enemy attacks.")
        time.sleep(0.7)  # dramatic pause :D
        print("Missed!")
        fight(player, enemy, zonemap)


def activate_status_effect(player, enemy, zonemap):  # Es muss SICHER SEIN, dass der Gegner einen active spell hat
    if enemy.active_effect:
        magic = enemy.active_effect[0]
        magic.spell_activated = True
        magic.status_duration -= 1
        if magic.status_damage > 0:  # Es ist ein Spell mit Schadenswirkung
            print(magic.status_description)
            print("Your enemy takes " + str(magic.status_damage) + " damage.")
            enemy.health -= magic.status_damage
            if magic.status_duration < 0:
                enemy.active_effect.clear()
            check_victory(player, enemy, zonemap)
        else:
            if magic.status_effect == "knockout":
                print("Your enemy is knocked out and cannot attack you.")
            elif magic.status_effect == "freezing":
                print("Your enemy is frozen and cannot attack you.")
            if magic.status_duration < 0:
                enemy.active_effect.clear()
            fight(player, enemy, zonemap)
    else:
        enemy_attack(player, enemy, zonemap)


def win_fight(player, enemy, zonemap):
    print("       ")
    print("**** You won!!! ****")
    print("       ")
    zonemap[myPlayer.location]["ENCOUNTERS"] -= 1
    # Kampf ist vorbei --------------------------------------------------
    if random.random() < enemy.loot_chance:  # Chance ob Loot-Drop oder nicht (abhängig von Gegner)
        loot(enemy, player)  # Spieler erhält Trank(30%) oder Gegenstand(70%)
    else:
        print("Looks like you found nothing interesting...")
    # Garantierte Belohnungen: Gold und Erfahrung
    player.get_ep(enemy.ep_drop)
    player.get_gold(random.randrange(10, 20) * enemy.loot_level)
    time.sleep(2)  # Notwendig?
    clear()


def check_victory(player, enemy, zonemap):
    if enemy.health <= 0:
        win_fight(player, enemy, zonemap)
    else:
        if enemy.active_effect and enemy.active_effect[0].spell_activated == False:
            activate_status_effect(player, enemy, zonemap)
        elif enemy.active_effect and enemy.active_effect[0].spell_activated == True:
            enemy_attack(player, enemy, zonemap)
        elif not enemy.active_effect:
            enemy_attack(player, enemy, zonemap)


def loot(enemy, player):
    if random.random() < 0.70:  # Chance auf Gegenstand: 70%, sonst Trank
        g = random.choice([game_object.Weapon(enemy.loot_level), game_object.Armor(enemy.loot_level)])
        if g.obj_type == "weapon":
            print("You find: " + g.name)
            print("Damage: " + str(g.damage))
            print("Would you like to swap your weapon? (y/n)\n")
            ant = input("> ")
            while ant not in ["y", "n"]:
                print("I need a decision: ")
                ant = input("> ")
            print(" ")
            if ant.lower()[0] in ["y", ""]:
                player.equip_weapon(g)  # neue Waffe angelegt und alte Waffe equipped = False
            player.get_weapon(g, p=False)  # Waffe (zusätzlich) ins Inventar
        elif g.obj_type == "armor":
            print("You find: " + g.name)
            print("Protection: " + str(g.protection))
            print("Slot: " + g.slot)
            print("Would you like to swap your armor? (y/n)\n")
            ant = input("> ")
            print("")
            if ant.lower()[0] in ["y", ""]:
                player.equip_armor(g)  # Rüstung angelegt und alte Rüstung equipped = False
                print("You equip your new armor.")
            player.get_armor(g, p=False)  # Waffe (zusätzlich) ins Inventar
    else:
        player.get_potion()


def fight_options():
    print("Choose: attack, magic, heal, flee, show stats, quit\n")
    ant = input("> ")
    clear()
    return ant


def print_location():
    print("#" * screen_width)
    print((" " * int((screen_width - len(zonemap[myPlayer.location]["ZONENAME"])) / 2)) + zonemap[myPlayer.location][
        "ZONENAME"] + (" " * int((screen_width - len(zonemap[myPlayer.location]["ZONENAME"])) / 2)))
    print((" " * int((screen_width - len(zonemap[myPlayer.location]["DESCRIPTION"])) / 2)) + zonemap[myPlayer.location][
        "DESCRIPTION"] + (" " * int((screen_width - len(zonemap[myPlayer.location]["DESCRIPTION"])) / 2)))
    if zonemap[myPlayer.location]["SOLVED"] == True:
        print((" " * int(
            (screen_width - len(zonemap[myPlayer.location]["EXAMINATION"] + "EXAMINATION")) / 2)) + "EXAMINATION: " +
              zonemap[myPlayer.location]["EXAMINATION"] + (" " * int(
            (screen_width - len(zonemap[myPlayer.location]["EXAMINATION"] + "EXAMINATION")) / 2)))
    print("#" * screen_width)


def prompt():
    print("You are here:")
    print_location()
    print("\n" + "=" * len("What would you like to do?"))
    print("What would you like to do?\n")
    print("-" * len("What would you like to do?"))
    print(" " * (int((len("What would you like to do?") - len("examine or move?")) / 2)) + "examine or move?")
    print("-" * len("What would you like to do?") + "\n")

    action = input("> ")
    acceptable_locations = ["move", "go", "travel", "walk", "quit", "examine", "inspect", "interact", "look", "hunting",
                            "hunt", "fishing", "fish", "corn", "get corn", "harvest", "heal", "healing", "potion",
                            "use potion", "show inventory", "inventory", "show stats", "stats", "buy", "sell", "repair",
                            "blacksmith", "knock", "magic", "learn", "spell", "rest", "play"]

    while action.lower() not in acceptable_locations:
        print("Unknown action. Try again. (move, examine, quit)")
        action = input("> ")

    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in ["move", "go", "travel", "walk"]:
        player_move()
    elif action.lower() in ["examine", "inspect", "interact", "look"]:
        player_examine()
    elif action.lower() in ["fishing", "fish"]:
        myPlayer.fishing()
    elif action.lower() in ["hunting", "hunt"]:
        myPlayer.hunting()
    elif action.lower() in ["corn", "get corn", "harvest"]:
        myPlayer.get_corn()
    elif action.lower() in ["heal", "healing", "potion", "use potion"]:
        myPlayer.use_potion()
    elif action.lower() in ["show inventory", "inventory"]:
        myPlayer.print_inventory()
    elif action.lower() in ["show stats", "stats"]:
        myPlayer.show_stats()
    elif action.lower() in ["buy", "sell", "blacksmith", "repair"]:
        myPlayer.buy_equipment()
    elif action.lower() in ["knock", "magic", "learn", "spell"]:
        myPlayer.learn_spell()
    elif action.lower() == "rest":
        myPlayer.rest()
    elif action.lower() == "play":
        myPlayer.play_game()

def player_move():
    dest = input("Where do you like to move to? ('up', 'down', 'left', 'right')\n> ")

    while dest not in ['up', 'down', 'left', 'right']:
        print("Invalid entry!")
        dest = input("Where do you like to move to? ('up', 'down', 'left', 'right')\n> ")

    if dest.lower() == "up":
        if zonemap[myPlayer.location]["UP"] != "":
            destination = zonemap[myPlayer.location]["UP"]
            movement(destination)
        else:
            stay(dest)
    elif dest.lower() == "down":
        if zonemap[myPlayer.location]["DOWN"] != "":
            destination = zonemap[myPlayer.location]["DOWN"]
            movement(destination)
        else:
            stay(dest)
    elif dest.lower() == "right":
        if zonemap[myPlayer.location]["RIGHT"] != "":
            destination = zonemap[myPlayer.location]["RIGHT"]
            movement(destination)
        else:
            stay(dest)
    elif dest.lower() == "left":
        if zonemap[myPlayer.location]["LEFT"] != "":
            destination = zonemap[myPlayer.location]["LEFT"]
            movement(destination)
        else:
            stay(dest)


def movement(destination):
    myPlayer.location = destination
    print("You have moved to the " + zonemap[myPlayer.location]["ZONENAME"] + ".")
    time.sleep(3)
    clear()


def stay(direct):
    directions = {"up": "north", "down": "south", "left": "west", "right": "east"}
    print("You cannot move further " + directions[direct] + ".")
    time.sleep(3)
    clear()


def player_examine():
    if zonemap[myPlayer.location]["ENCOUNTERS"] > 0:
        fight_setup(myPlayer, zonemap[myPlayer.location]["POSSIBILITIES"])

    if zonemap[myPlayer.location]["SOLVED"] == True:
        print("You have already been here.")
        print(zonemap[myPlayer.location]["EXAMINATION"])
        time.sleep(3)
        clear()
    else:
        print(zonemap[myPlayer.location]["EXAMINATION"])
        zonemap[myPlayer.location]["SOLVED"] = True
        if all(solved_places.values()):
            myPlayer.game_over = True
        time.sleep(3)
        clear()


def intro():
    clear()
    question3 = "Welcome, " + myPlayer.name + " the " + myPlayer.play_class + ".\n"
    speech_manipulation(question3, 0.05)
    speech_manipulation("Welcome to this fantasy world I created for you. ;)\n", 0.05)
    speech_manipulation("I hope you will have some fun\n ... \n ... \n ...\n", 0.15)
    speech_manipulation(
        "Well, you are not the first adventurer here. There have been many before you. And to be honest, there will "
        "be many after you ... when you have ... ",
        0.05)
    speech_manipulation("passed away ... \n", 0.25)
    speech_manipulation("Now have some fun exploring the world. We will see each other when it's time to.\n", 0.05)
    time.sleep(2)


def end_screen():
    speech_manipulation(
        "Congratulations, you have solved the complete game. I never thought you would be able to do this.", 0.05)
    print("")
    speech_manipulation(
        "I will get in touch with you soon. Wait for a sign from me. I think I have a good job for some strong "
        "adventurer like you.",
        0.04)
    time.sleep(5)
    clear()
    # print("Made by laeberkaes")
    # print("Hit me "UP" at: https://github.com/laeberkaes/ or @laeberkaes:uraltemorla.xyz")
    #
    # time.sleep(5)
    sys.exit()


def game_over():
    clear()
    speech_manipulation("Ouh there you are again.\n", 0.05)
    speech_manipulation(
        "Don't get me wrong. This is no surprise for me. Maybe you have more luck in your next reincarnation.\n",
        0.05)
    speech_manipulation("Have a good day. :)", 0.07)
    myPlayer.game_over = True
    time.sleep(2)
    sys.exit()


def game_loop():
    while not myPlayer.game_over:
        prompt()


def setup_game():
    clear()
    question1 = "Hello what's your name?\n"
    speech_manipulation(question1, 0.05)
    print("")
    myPlayer.name = input("> ").lower()

    clear()

    classes = ["warrior", "mage", "rogue"]
    question2 = "What Class do you want to play? (Warrior, Mage, Rogue)\n"
    speech_manipulation(question2, 0.01)
    print("")
    player_class = input("> ").lower()
    print("")
    if player_class.lower() in classes:
        myPlayer.play_class = player_class
        print("You are now a " + player_class)
        time.sleep(1.5)
    else:
        while player_class.lower() not in classes:
            print("No valid class.\n")
            player_class = input("> ").lower()
        if player_class.lower() in classes:
            myPlayer.play_class = player_class
            print("You are now " + player_class)
            time.sleep(1.5)

    if myPlayer.play_class == "warrior":
        myPlayer.health_max = 120
        myPlayer.health_cur = 120
        myPlayer.mp_cur_max.append(20)
        myPlayer.mp_cur_max.append(20)
    elif myPlayer.play_class == "mage":
        myPlayer.health_max = 80
        myPlayer.health_cur = 80
        myPlayer.mp_cur_max.append(80)
        myPlayer.mp_cur_max.append(80)
    elif myPlayer.play_class == "rogue":
        myPlayer.health_max = 100
        myPlayer.health_cur = 100
        myPlayer.mp_cur_max.append(40)
        myPlayer.mp_cur_max.append(40)

    # intro()

    clear()
    print("#" * screen_width + "\n")
    print("#" + (" " * int((screen_width - 2 - len("Let's start now")) / 2)) + "Let's start now" + (
            " " * int((screen_width - 2 - len("Let's start now")) / 2)) + "#\n")
    print("#" * screen_width + "\n")

    game_loop()

    end_screen()


if __name__ == "__main__":
    title_screen()
