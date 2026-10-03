import json
from player import Player

def save_game(player, filename):
    with open(filename, "w") as f:
        json.dump(player.to_dict(), f, indent=2)
        print("Saved!")

def load_game(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            player = Player(data["name"], data["max_hp"], data["atk"], data["money"])
            player.hp = data["hp"]
            player.exp = data["exp"]
            player.level = data["level"]
            player.exp_to_next = data["exp_to_next"]
            return player
    except FileNotFoundError:
        print("Load error. Data filed wasn't found")
        return None