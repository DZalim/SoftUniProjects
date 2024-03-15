from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, MainService.CAPACITY)

    def details(self):
        robots = ' '.join(robot.name for robot in self.robots)
        return (f"{self.name} Main Service:\n"
                f"Robots: {robots if robots else 'none'}")
