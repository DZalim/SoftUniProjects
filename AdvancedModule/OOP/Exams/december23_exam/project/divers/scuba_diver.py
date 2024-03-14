from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):

    INITIAL_OXYGEN_VALUE = 540

    def __init__(self, name: str):
        super().__init__(name, ScubaDiver.INITIAL_OXYGEN_VALUE)

    def miss(self, time_to_catch: int):
        reduced_value = time_to_catch * 0.30
        self.check_oxygen_value(reduced_value)

    def renew_oxy(self):
        self.oxygen_level = ScubaDiver.INITIAL_OXYGEN_VALUE
