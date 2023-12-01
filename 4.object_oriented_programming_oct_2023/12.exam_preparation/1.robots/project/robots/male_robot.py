from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    INITIAL_WEIGHT = 9

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, MaleRobot.INITIAL_WEIGHT)
        self.type = self.__class__.__name__
        self.service_compatibility = "MainService"

    def eating(self):
        self.weight += 3
