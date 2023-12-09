from math import ceil

from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, 120)

    def miss(self, time_to_catch: int):
        decrease = ceil(time_to_catch * 0.6)
        self.oxygen_level = max(0, self.oxygen_level - decrease)

    def renew_oxy(self):
        self.oxygen_level = 120
