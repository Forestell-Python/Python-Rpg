import random
from weapon import Weapon

class Entity:
    def __init__(self, name, max_hp, attack, weapon=None):
        self.name = name
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.attack = attack
        self.weapon = weapon if weapon is not None else Weapon("Fists", 0)
        self.inventory = []

    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, amount):
        self.hp = max(self.hp - amount, 0)
        print(f"{self.name}: {self.hp}/{self.max_hp} hp")
    
    def show_stats(self):
        print(f"""{self.name}:
Health: {self.hp}/{self.max_hp}
Damage: {self.attack}""")

    def calculate_damage(self):
        damage = self.attack + self.weapon.bonus
        damage = random.randint(max(damage - 2, 2), damage + 2)

        if random.random() < 0.1:
            damage *= 2
            print("CRITICAL HIT!!!")

        return damage

    def beat(self, enemy):
        damage = self.calculate_damage()

        print(f"{self.name} dealt {enemy.name} {damage} damage")
        enemy.take_damage(damage)