from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.name in [p.name for p in self.pokemons]:
            return f"This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for p_obg in self.pokemons:
            if p_obg.name == pokemon_name:
                self.pokemons.remove(p_obg)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        info = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        for p in self.pokemons:
            info.append(f"- {p.pokemon_details()}")
        return "\n".join(info)