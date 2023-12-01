from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }
    VALID_ROBOTS = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot
    }

    def __init__(self):
        self.robots: list = []
        self.services: list = []

    def add_service(self, service_type: str, name: str):
        if service_type not in RobotsManagingApp.VALID_SERVICES:
            raise Exception("Invalid service type!")

        new_service = RobotsManagingApp.VALID_SERVICES[service_type](name)
        self.services.append(new_service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in RobotsManagingApp.VALID_ROBOTS:
            raise Exception("Invalid robot type!")

        new_robot = RobotsManagingApp.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(new_robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next(filter(lambda x: x.name == robot_name, self.robots))
        service = next(filter(lambda x: x.name == service_name, self.services))

        if service.type != robot.service_compatibility:
            return "Unsuitable service."

        if len(service.robots) == service.capacity:
            raise Exception("Not enough capacity for this robot!")

        for r in self.robots:
            if r.name == robot_name:
                self.robots.remove(r)
                break

        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(filter(lambda x: x.name == service_name, self.services))

        if robot_name not in [x.name for x in service.robots]:
            raise Exception("No such robot in this service!")

        for r in service.robots:
            if r.name == robot_name:
                service.robots.remove(r)
                self.robots.append(r)

                return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next(filter(lambda x: x.name == service_name, self.services))

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = next(filter(lambda x: x.name == service_name, self.services))
        price = sum([x.price for x in service.robots])

        return f"The value of service {service.name} is {price:.2f}."

    def __str__(self):
        result = [service.details() for service in self.services]

        return '\n'.join(result)
