class Pokemon:
    def __init__(self, name, level, type, maximum_health,
                 current_health, is_knocked_out ):
        self.name = name
        self.level = level
        self.type = type
        self.maximum_health = maximum_health
        self.current_health = current_health
        self.is_knocked_out = is_knocked_out

    def lose_health(self, health_loss):
        self.current_health = self.current_health - health_loss
        print("{name} now has {health} health".format(name=self.name, health=self.current_health))

    def regain_health(self, health_gain):
        self.current_health = self.current_health + health_gain
        print("{name} now has {health} health".format(name=self.name, health=self.current_health))

    def knock_out(self):
        if self.current_health <= 0:
            self.is_knocked_out = True
            print("{name} is now knocked out".format(name=self.name)

    def revive(self):
        if self.current_health <= 0:
            self.is_knocked_out = False
            print(self.is_knocked_out)

    def attack(self, opposite_pokemon):
        self.opposite_pokemon = opposite_pokemon
        if self.opposite_pokemon.type == "grass":
            if self.type == "grass":
                attack_multiplier = 1
            if self.type == "water"
                attack_multiplier = 0.5
            if self.type == "fire":
                attack_multiplier = 2
        if self.opposite_pokemon.type == "water":
            if self.type == "grass":
                attack_multiplier = 2
            if self.type == "water"
                attack_multiplier = 1
            if self.type == "fire":
                attack_multiplier = 0.5
        if self.opposite_pokemon.type == "fire":
            if self.type == "grass":
                attack_multiplier = 0.5
            if self.type == "water"
                attack_multiplier = 2
            if self.type == "fire":
                attack_multiplier = 1

        attack_damage = self.level * attack_multiplier
        print("{name} is dealing {damage} damage to the opposite pokemon".format(name=self.name, damage=attack_damage))
        return attack_damage




