from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    INITIALLY_WEIGHT = 7
    WEIGHT_INCREASE = 1

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, FemaleRobot.INITIALLY_WEIGHT)

    def eating(self):
        self.weight += FemaleRobot.WEIGHT_INCREASE
