from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    INITIALLY_WEIGHT = 9
    WEIGHT_INCREASE = 3

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, MaleRobot.INITIALLY_WEIGHT)

    def eating(self):
        self.weight += MaleRobot.WEIGHT_INCREASE
