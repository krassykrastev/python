from typing import List, Optional

from project.astronaut.astronaut import Astronaut


class AstronautRepository:

    def __init__(self):
        self.astronauts: List[Astronaut] = []

    def add(self, astronaut: Astronaut) -> None:
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut) -> None:
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str) -> Optional[Astronaut]:
        for astro in self.astronauts:
            if astro.name == name:
                return astro

