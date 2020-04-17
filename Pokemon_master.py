class Pokemon:
    def __init__(self, name, level, type, current_health, is_knocked_out ):
        self.name = name
        self.level = level
        self.type = type
        self.maximum_health = self.level * 5
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


class Trainer:
    def __init__(self, pokemons, trainer_name, num_of_potions, active_pokemon):
        self.pokemons = pokemons
        self.trainer_name = trainer_name
        self.num_of_potions = num_of_potions
        self.active_pokemon = active_pokemon

    def use_potion(self):
        self.active_pokemon
        print()
        return

    def attack_trainer(self):

        print()
        return

    def switch_pokemon(self, pokemon_number):

        print()
        return

    def attack_active_pokemon(self):

        print()
        return


charmander = Pokemon('charmander', 7, 'fire', current_health=self.maximum_health, False)
bulbasaur = Pokemon('bulbasaur', 9, 'grass', current_health=self.maximum_health, False)
squirtle = Pokemon('squirtle', 11, 'water', current_health=self.maximum_health, False)
celebi = Pokemon('celebi', 11, 'grass', current_health=self.maximum_health, False)
lapras = Pokemon('lapras', 9, 'water', current_health=self.maximum_health, False)
growlithe = Pokemon('growlithe', 7, 'fire', current_health=self.maximum_health, False)

Ash_keczap = Trainer([charmander, bulbasaur, squirtle], "Ash", 3, 1)
justin_timberlake = Trainer([celebi, lapras, growlithe], "Justin", 3, 1)


