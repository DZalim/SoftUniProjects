from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):

    INITIAL_BUDGET = 1000.00
    INCREASE_POINTS = 115

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self.INITIAL_BUDGET)

    def win(self):
        self.advantage += self.INCREASE_POINTS
        self.wins += 1
