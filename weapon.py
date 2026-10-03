from item import Item

class Weapon(Item):
    def __init__(self, name, bonus):
        super().__init__(name)
        self.bonus = bonus