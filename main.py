from player import Player
from enemy import Enemy
from weapon import Weapon
from battle import battle, choose_enemy
from storage import save_game, load_game

FILEPATH = r"rpg/data.json"
        
def main():
    vlad = Player("Vlad", 100, 15)

    enemies = {
        "1": ("Goblin", 30, 5),
        "2": ("Orc", 60, 10),
        "3": ("Dragon", 150, 20)
    }

    vlad.inventory.append(Weapon("Sword", 5))
    vlad.inventory.append(Weapon("Axe", 10))
    vlad.inventory.append(Weapon("Dagger", 2))

    while vlad.is_alive():
        print("=" * 40)
        print("RPG")
        print("=" * 40)
        print("1. Battle")
        print("2. Stats")
        print("3. Rest")
        print("4. Save")
        print("5: Load")
        print("6: Change a weapon")
        print("0. Leave")
        num = input("Choose a function: ")

        if num == "1":
            enemy = choose_enemy(enemies)
            if enemy is None:
                continue
            name, hp, atk = enemy
            battle(vlad, Enemy(name, hp, atk))
        elif num == "2":
            vlad.show_stats()
        elif num == "3":
            vlad.heal()
        elif num == "4":
            save_game(vlad, FILEPATH)
            print("Saved!")
        elif num == "5":
            loaded = load_game(FILEPATH)
            if loaded:
                vlad = loaded
                print("Loaded!")
        elif num == "6":
            vlad.change_weapon()
        elif num == "0":
            print("See you later!")
            break
        else:
            print("No function")
    print("Game over!")
    

if __name__ == "__main__":
    main()