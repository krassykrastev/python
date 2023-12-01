from typing import List, Optional
from project.planet.planet import Planet


class PlanetRepository:

    def __init__(self):
        self.planets: List[Planet] = []

    def add(self, planet: Planet) -> None:
        self.planets.append(planet)

    def remove(self, planet: Planet) -> None:
        self.planets.remove(planet)

    def find_by_name(self, name: str) -> Optional[Planet]:
        for planet in self.planets:
            if planet.name == name:
                return planet
