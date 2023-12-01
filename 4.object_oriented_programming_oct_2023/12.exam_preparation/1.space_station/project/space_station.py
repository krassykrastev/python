from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUT_TYPES = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist,
    }

    successful_missions = 0
    unsuccessful_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str) -> str:
        if astronaut_type not in SpaceStation.VALID_ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")

        for astro in self.astronaut_repository.astronauts:
            if astro.name == name:
                return f"{name} is already added."

        new_astro = SpaceStation.VALID_ASTRONAUT_TYPES[astronaut_type](name)

        self.astronaut_repository.add(new_astro)

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str) -> str:
        for planet in self.planet_repository.planets:
            if planet.name == name:
                return f"{name} is already added."

        new_planet = Planet(name)

        self.planet_repository.add(new_planet)

        for item in items.split(", "):
            new_planet.items.append(item)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str) -> str:
        current_astro = self.astronaut_repository.find_by_name(name)

        if not current_astro:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(current_astro)

        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self) -> None:
        for astro in self.astronaut_repository.astronauts:
            astro.increase_oxygen(10)

    def send_on_mission(self, planet_name: str) -> str:
        current_planet = self.planet_repository.find_by_name(planet_name)

        if not current_planet:
            raise Exception("Invalid planet name!")

        astros = [a for a in sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen)]

        mission_astros = [a for a in astros if a.oxygen > 30][:5]

        if not mission_astros:
            raise Exception("You need at least one astronaut to explore the planet!")

        participating_astros = 0

        for astro in mission_astros:
            while astro.oxygen > 0:
                if current_planet.items:
                    astro.backpack.append(current_planet.items.pop())
                    astro.breathe()

                else:
                    participating_astros += 1
                    SpaceStation.successful_missions += 1

                    return (f"Planet: {planet_name} was explored. "
                            f"{participating_astros} astronauts participated in collecting items.")

            participating_astros += 1

        SpaceStation.unsuccessful_missions += 1
        return "Mission is not completed."

    def report(self) -> str:
        result = [f"{SpaceStation.successful_missions} successful missions!\n"
                  f"{SpaceStation.unsuccessful_missions} missions were not completed!\n"
                  f"Astronauts' info:"]

        for astro in self.astronaut_repository.astronauts:
            result.append(f"Name: {astro.name}\nOxygen: {astro.oxygen}")

            if astro.backpack:
                result.append(f"Backpack items: {', '.join(astro.backpack)}")
            else:
                result.append(f"Backpack items: none")

        return "\n".join(result)
