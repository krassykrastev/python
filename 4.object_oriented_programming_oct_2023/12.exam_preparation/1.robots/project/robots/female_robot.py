from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    INITIAL_WEIGHT = 7

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, FemaleRobot.INITIAL_WEIGHT)
        self.type = self.__class__.__name__
        self.service_compatibility = "SecondaryService"

    def eating(self):
        self.weight += 1
