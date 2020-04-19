class Pokemon:
    def __init__(self, name, level, type, is_knocked_out):
        self.name = name
        self.level = level
        self.type = type
        self.maximum_health = self.level * 5
        self.current_health = self.maximum_health
        self.is_knocked_out = is_knocked_out
        self.trainer_name = None

    def __repr__(self):
        return self.name

    def lose_health(self, health_loss):
        print("{name} had {health}/{max_health} health before damage".format(name=self.name, health=self.current_health, max_health=self.maximum_health))
        self.current_health = self.current_health - health_loss
        print("{name} now has {health}/{max_health} health \n".format(name=self.name, health=self.current_health, max_health=self.maximum_health))

    def regain_health(self, health_gain):
        after_potion = self.current_health + health_gain
        if after_potion < self.maximum_health:
            self.current_health = self.current_health + health_gain
        if after_potion > self.maximum_health:
            self.current_health = self.maximum_health
        print("{name} now has {health}/{max_health} health".format(name=self.name, health=self.current_health, max_health=self.maximum_health))

    def knock_out(self):
        print(self.trainer_name)
        if self.current_health <= 0:
            self.is_knocked_out = True
            print("{name} is now knocked out. Choose another pokemon".format(name=self.name))
            return self.is_knocked_out

    def revive(self):
        self.is_knocked_out = False
        print(self.is_knocked_out)
        return self.is_knocked_out

    def attack(self, opposite_pokemon):
        self.opposite_pokemon = opposite_pokemon
        if self.opposite_pokemon.type == "grass":
            if self.type == "grass":
                attack_multiplier = 1
            if self.type == "water":
                attack_multiplier = 0.5
            if self.type == "fire":
                attack_multiplier = 2
        if self.opposite_pokemon.type == "water":
            if self.type == "grass":
                attack_multiplier = 2
            if self.type == "water":
                attack_multiplier = 1
            if self.type == "fire":
                attack_multiplier = 0.5
        if self.opposite_pokemon.type == "fire":
            if self.type == "grass":
                attack_multiplier = 0.5
            if self.type == "water":
                attack_multiplier = 2
            if self.type == "fire":
                attack_multiplier = 1

        attack_damage = self.level * attack_multiplier
        print(self.trainer_name)
        print("{name} is dealing {damage} damage to the opposite pokemon".format(name=self.name, damage=attack_damage))
        return attack_damage


class Trainer():
    def __init__(self, pokemons, trainer_name, num_of_potions, active_pokemon):
        self.pokemons = pokemons
        self.trainer_name = trainer_name
        self.num_of_potions = num_of_potions
        self.active_pokemon = self.pokemons[active_pokemon -1]
        self.knocked_out_pokemons = []

        #assigning trainer name to pokemon and classifying which pokemon is knocked out
        for pokemon in self.pokemons:
            pokemon.trainer_name = self.trainer_name
            if pokemon.is_knocked_out == True:
                self.knocked_out_pokemons.append(pokemon)
                self.pokemons.remove(pokemon)



    def use_potion(self):
        # reduces num_of_potions by 1
        # heals active pokemon
        print(self.trainer_name)
        amount_of_healing = 20
        self.active_pokemon.regain_health(amount_of_healing)
        self.num_of_potions += -1
        print("{trainer_name}'s {pokemon} has been heald by {healing} \n".format(trainer_name=self.trainer_name, pokemon=self.active_pokemon.name, healing=amount_of_healing))

    def attack_trainer(self, trainer_to_attack):
        # give damage to another trainer's active pokemon
        if self.active_pokemon.is_knocked_out == True:
            print("{pokemon} is knocked out and can't fight anymore, choose a different pokemon: {pokemons}\n".format(pokemon=self.active_pokemon.name, pokemons=self.pokemons))

        else:
            pokemon_we_attack = trainer_to_attack.active_pokemon
            attack_damage = self.active_pokemon.attack(pokemon_we_attack)
            pokemon_we_attack.lose_health(attack_damage)

            if pokemon_we_attack.current_health <= 0:
                pokemon_we_attack.knock_out()



    def switch_pokemon(self, pokemon_number):
        print(self.trainer_name)
        print("Your pokemons are {pokemons}".format(pokemons=self.pokemons))
        if self.pokemons[pokemon_number - 1].is_knocked_out == True:
            print("{pokemon} is knocked out and you can't choose it".format(pokemon=self.pokemons[pokemon_number - 1].name))
        else:
            self.active_pokemon = self.pokemons[pokemon_number - 1]
            print("{trainer} chose {name}\n".format(trainer=self.trainer_name, name=self.active_pokemon.name))



charmander = Pokemon('charmander', 7, 'fire', False)
bulbasaur = Pokemon('bulbasaur', 9, 'grass', False)
squirtle = Pokemon('squirtle', 11, 'water', False)
celebi = Pokemon('celebi', 11, 'grass', False)
lapras = Pokemon('lapras', 9, 'water', False)
growlithe = Pokemon('growlithe', 7, 'fire', False)

Ash_keczap = Trainer([charmander, bulbasaur, squirtle], "Ash", 3, 1)
justin_timberlake = Trainer([celebi, lapras, growlithe], "Justin", 3, 1)

# Possible moves:
# attack opposite pokemon
# switch active pokemon
# use potion

Ash_keczap.attack_trainer(justin_timberlake)
justin_timberlake.switch_pokemon(3)
Ash_keczap.attack_trainer(justin_timberlake)
justin_timberlake.attack_trainer(Ash_keczap)
Ash_keczap.use_potion()
justin_timberlake.attack_trainer(Ash_keczap)
Ash_keczap.attack_trainer(justin_timberlake)
justin_timberlake.attack_trainer(Ash_keczap)
Ash_keczap.attack_trainer(justin_timberlake)
justin_timberlake.attack_trainer(Ash_keczap)
Ash_keczap.attack_trainer(justin_timberlake)
justin_timberlake.attack_trainer(Ash_keczap)
Ash_keczap.attack_trainer(justin_timberlake)
justin_timberlake.switch_pokemon(3)
justin_timberlake.switch_pokemon(2)