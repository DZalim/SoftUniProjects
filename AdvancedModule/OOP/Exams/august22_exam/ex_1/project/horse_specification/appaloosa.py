from project.horse_specification.horse import Horse


class Appaloosa(Horse):

    MAX_SPEED = 120
    SPEED_INCREASE = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):

        value = self.speed + self.SPEED_INCREASE

        if value > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed = value
