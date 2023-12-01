from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, MainService.CAPACITY)
        self.type = self.__class__.__name__

    def details(self):
        result = [f"{self.name} Main Service:"]
        robots = "none"

        if len(self.robots) > 0:
            robots = ' '.join([robot.name for robot in self.robots])

        result.append(f"Robots: {robots}")

        return '\n'.join(result)
