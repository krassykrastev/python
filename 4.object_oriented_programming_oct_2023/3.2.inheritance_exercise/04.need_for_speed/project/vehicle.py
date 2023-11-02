class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: int, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: int):
        consumed_fuel = kilometers * self.fuel_consumption
        if self.fuel >= consumed_fuel:
            self.fuel -= consumed_fuel
