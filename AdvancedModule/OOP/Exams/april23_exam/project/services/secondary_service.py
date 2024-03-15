from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, SecondaryService.CAPACITY)

    def details(self):
        robots = ' '.join(robot.name for robot in self.robots)
        return (f"{self.name} Secondary Service:\n"
                f"Robots: {robots if robots else 'none'}")
