from math import ceil

from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, 540)

    def miss(self, time_to_catch: int):
        decrease = ceil(time_to_catch * 0.3)
        self.oxygen_level = max(0, self.oxygen_level - decrease)

    def renew_oxy(self):
        self.oxygen_level = 540
