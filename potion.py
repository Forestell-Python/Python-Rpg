from item import Item

class Potion(Item):
    def __init__(self, name, effect_type, value):
        super().__init__(name)
        self.effect_type = effect_type
        self.value = value

    def use(self, player):
        if self.effect_type == "heal":
            self.heal(player)

    def heal(self, player):
        player.heal(self.value)