from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):

    INITIAL_BUDGET = 500.00
    INCREASE_POINTS = 145

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self.INITIAL_BUDGET)

    def win(self):
        self.advantage += self.INCREASE_POINTS
        self.wins += 1
