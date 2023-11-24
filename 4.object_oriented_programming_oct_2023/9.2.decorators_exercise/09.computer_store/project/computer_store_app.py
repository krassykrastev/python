from typing import List

from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_TYPES = {"Desktop Computer": DesktopComputer, "Laptop": Laptop}

    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        computer = self.VALID_TYPES[type_computer](manufacturer, model)
        result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer = next((c for c in self.warehouse if c.ram >= wanted_ram and c.processor == wanted_processor and c.price <= client_budget), None)
        if not computer:
            raise Exception("Sorry, we don't have a computer for you.")
        self.profits += client_budget - computer.price
        self.warehouse.remove(computer)
        return f"{computer.__repr__()} sold for {client_budget}$."
