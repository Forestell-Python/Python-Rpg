def battle(player, enemy):
    if not player.is_alive() or not enemy.is_alive():
        return
    print("=" * 20 + " BATTLE " + "=" * 20)
    print(f"========== {player.name.upper()} ==========")
    player.show_stats()
    print(f"========== {enemy.name.upper()} ==========")
    enemy.show_stats()
    while player.is_alive() and enemy.is_alive():
        player.beat(enemy)
        if not enemy.is_alive():
            print(f"{player.name} won!")
            player.add_money(enemy.max_hp // 2)
            player.gain_exp(enemy.max_hp)
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