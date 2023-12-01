from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        raise NotImplementedError

    @abstractmethod
    def create_sofa(self):
        raise NotImplementedError

    @abstractmethod
    def create_table(self):
        raise NotImplementedError


class Chair:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Sofa:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Table:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class VictorianFactory(AbstractFactory):
    style = "Victorian"

    def create_chair(self):
        return Chair(f"{self.style} chair")

    def create_sofa(self):
        return Sofa(f"{self.style} sofa")

    def create_table(self):
        return Table(f"{self.style} table")


class ModernFactory(AbstractFactory):
    style = "Modern"

    def create_chair(self):
        return Chair(f"{self.style} chair")

    def create_sofa(self):
        return Sofa(f"{self.style} sofa")

    def create_table(self):
        return Table(f"{self.style} table")


class FuturisticFactory(AbstractFactory):
    style = "Futuristic"

    def create_chair(self):
        return Chair(f"{self.style} chair")

    def create_sofa(self):
        return Sofa(f"{self.style} sofa")

    def create_table(self):
        return Table(f"{self.style} table")

