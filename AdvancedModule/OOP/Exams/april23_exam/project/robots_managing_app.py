from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    VALID_SERVICES = {
        'MainService': MainService,
        'SecondaryService':SecondaryService
    }

    VALID_ROBOTS = {
        'MaleRobot': MaleRobot,
        'FemaleRobot': FemaleRobot
    }

    VALID_COMBINATIONS = {
        'MaleRobot': 'MainService',
        'FemaleRobot': 'SecondaryService'
    }

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")

        service = self.VALID_SERVICES[service_type](name)
        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")

        robot = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        current_robot = self.get_robot(robot_name)
        current_service = self.get_service(service_name)

        robot_type = current_robot.__class__.__name__
        service_type = current_service.__class__.__name__

        if service_type != self.VALID_COMBINATIONS[robot_type]:
            return "Unsuitable service."

        if current_service.capacity == len(current_service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(current_robot)
        current_service.robots.append(current_robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        current_robot = self.get_robot_in_service(robot_name, service_name)
        current_service = self.get_service(service_name)

        if not current_robot:
            raise Exception("No such robot in this service!")

        current_service.robots.remove(current_robot)
        self.robots.append(current_robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        current_service = self.get_service(service_name)

        for robot in current_service.robots:
            robot.eating()

        return f"Robots fed: {len(current_service.robots)}."

    def service_price(self, service_name: str):
        current_service = self.get_service(service_name)
        total_price = sum([robot.price for robot in current_service.robots])

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return '\n'.join(service.details() for service in self.services)

    def get_robot(self, name):
        robot = [robot for robot in self.robots if name == robot.name]
        return robot[0] if robot else None

    def get_robot_in_service(self, robot_n, service_n):
        robot = [robot for service in self.services if service.name == service_n
                 for robot in service.robots if robot.name == robot_n]

        return robot[0] if robot else None

    def get_service(self, name):
        service = [service for service in self.services if name == service.name]
        return service[0] if service else None
