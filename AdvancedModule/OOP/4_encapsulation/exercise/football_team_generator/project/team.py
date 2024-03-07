from project.player import Player


class Team:

    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: list[Player] = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name):
        try:
            player = [player for player in self.__players if player.name == player_name][0]
            self.__players.remove(player)
            return player
        except IndexError:
            return f"Player {player_name} not found"
