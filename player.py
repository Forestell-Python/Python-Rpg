from entity import Entity
from potion import Potion
from weapon import Weapon

class Player(Entity):
    def __init__(self, name, max_hp, attack, money=0):
        super().__init__(name, max_hp, attack)
        self.money = money
        self.exp = 0
        self.level = 1
        self.exp_to_next = 100

    def show_stats(self):
        super().show_stats()
        print(f"Balance: {self.money}")
        print(f"Level: {self.level}")
        print(f"Experience: {self.exp}/{self.exp_to_next}")
        print(f"Current Weapon: {self.weapon.name} (+{self.weapon.bonus} damage)")
        if len(self.inventory) == 0:
            return
        print("Inventory:")
        i = 1
        for item in self.inventory:
            print(f"{i}: {item.name}")
            i += 1

    def add_money(self, amount):
        self.money += amount

    def heal(self, amount):
        old_hp = self.hp
        self.hp = min(self.hp + amount, self.max_hp)
        print(f"{self.name} healed {self.hp - old_hp} hp")

    def rest(self):
        price = 25
        if self.money < price:
            print("Not enough money")
            return
        self.money -= price
        self.heal(self.max_hp // 4)
        

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= self.exp_to_next:
            self.level_up()
        print(f"{self.name}: {self.exp}/{self.exp_to_next} exp")

    def level_up(self):
        while self.exp >= self.exp_to_next:
            self.level += 1
            self.exp -= self.exp_to_next
            self.exp_to_next *= 2
            self.max_hp += 20
            self.attack += 3
            self.hp = self.max_hp
            print(f"{self.name} leveled up to {self.level} level! Health: {self.max_hp}, Damage: {self.attack}. You healed up")

    def to_dict(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "atk": self.attack,
            "money": self.money,
            "exp": self.exp,
            "level": self.level,
            "exp_to_next": self.exp_to_next
        }

    def pick_up(self, item):
        self.inventory.append(item)
        print(f"You picked up {item.name}")

    def change_weapon(self):

        weapons = [item for item in self.inventory if isinstance(item, Weapon)]

        if not weapons:
            return

        for i, weapon in enumerate(weapons, start=1):
            print(f"{i}: {weapon.name}")
        
        while True:
            try:
                new_weapon = int(input("Choose a weapon (0 to quit): "))

                if 0 <= new_weapon <= len(weapons):
                    break

                print("Enter a number that is in a list above or 0")
            except ValueError:
                print("Write a number")
        if new_weapon == 0:
            print(f"There is still {self.weapon.name}")
            return
        self.weapon = weapons[new_weapon - 1]
        print(f"You chose: {self.weapon.name}")

    def use_potion(self):
        potions = [item for item in self.inventory if isinstance(item, Potion)]

        if not potions:
            print("No potions")
            return None

        for i, potion in enumerate(potions, start=1):
            print(f"{i}: {potion.name}")

        while True:
            try:
                choice = int(input("Choose a potion (0 to quit): "))
                if 0 <= choice <= len(potions):
                    break
                print("Invalid number")
            except ValueError:
                print("Write a number")

        if choice == 0:
            return None

        potion = potions[choice - 1]
        potion.use(self)
        self.inventory.remove(potion)
        return True