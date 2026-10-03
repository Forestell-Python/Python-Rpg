import random
from potion import Potion

def battle(player, enemy):
    if not player.is_alive() or not enemy.is_alive():
        return
    print("=" * 20 + " BATTLE " + "=" * 20)
    print(f"========== {player.name.upper()} ==========")
    player.show_stats()
    print(f"========== {enemy.name.upper()} ==========")
    enemy.show_stats()
    while player.is_alive() and enemy.is_alive():
        while True:
            choice = choose_action()
            if choice == "1":
                player.beat(enemy)
            elif choice == "2":
                success = player.use_potion()
                if success is None:
                    continue
            break

        if not enemy.is_alive():
            print(f"{player.name} won!")

            player_loot = loot(enemy.max_hp)
            money = player_loot.pop("Money")
            exp = player_loot.pop("Exp")
            player.add_money(money)
            player.gain_exp(exp)
            
            for item in player_loot.values():
                player.pick_up(item)
                
            return
        enemy.beat(player)
    print(f"{player.name} lost!")

def choose_enemy(enemies):
    while True:
        for key, (name, hp, atk) in enemies.items():
            print(f"{key}: {name} (hp {hp}, atk {atk})")
        print("0: Quit matchmaking")
        enemy = input("Choose the number of the enemy: ")
        if enemy == "0":
            return None
        elif enemy in enemies:
            return enemies[enemy]
        else:
            print("Incorrect key")

def choose_action():
    print(f"{"=" * 10} Choose an action {"=" * 10}")
    print("1. Beat an enemy")
    print("2. Use a potion")
    while True:
        choice = input("Choose: ")
        if choice in ["1", "2"]:
            return choice
        print("Invalid number")

def loot(enemymaxhp):
    loot_amount = {}

    loot_amount["Money"] = enemymaxhp // 2
    loot_amount["Exp"] = enemymaxhp

    if random.randint(1, 100) <= 25:
        loot_amount["Health Potion"] = Potion("Health Potion", "heal", random.randint(40, 80))

    return loot_amount