from typing import List

from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:

    VALID_SUSTENANCE_TYPES = {
        'Food': Food,
        'Drink': Drink
    }

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *players: Player):

        added_names = []

        for player in players:
            if not self.find_player(player.name):
                self.players.append(player)
                added_names.append(player.name)

        return f"Successfully added: {', '.join(added_names)}"

    def add_supply(self, *supplies: Supply):

        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.find_player(player_name)

        if player and sustenance_type in Controller.VALID_SUSTENANCE_TYPES:
            last_supply = self.find_last_supply_from_the_given_type(sustenance_type)

            if sustenance_type == 'Food' and not last_supply:
                raise Exception("There are no food supplies left!")

            if sustenance_type == 'Drink' and not last_supply:
                raise Exception("There are no drink supplies left!")

            if player.stamina == 100:
                return f"{player_name} have enough stamina."

            if player.stamina + last_supply.energy > 100:
                player.stamina = 100
            else:
                player.stamina += last_supply.energy

            self.supplies.remove(last_supply)
            return f"{player_name} sustained successfully with {last_supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_one = self.find_player(first_player_name)
        player_two = self.find_player(second_player_name)

        if player_one.stamina == 0 and player_two.stamina == 0:
            return (f"Player {player_one.name} does not have enough stamina.\n"
                    f"Player {player_two.name} does not have enough stamina.")

        if player_one.stamina == 0:
            return f"Player {player_one.name} does not have enough stamina."

        if player_two.stamina == 0:
            return f"Player {player_two.name} does not have enough stamina."

        lower_stamina = min(player_one.stamina, player_two.stamina)
        highest_stamina = max(player_one.stamina, player_two.stamina)

        player_with_lower_stamina = [player for player in [player_one, player_two] if player.stamina == lower_stamina][0]
        player_with_highest_value = [player for player in [player_one, player_two] if player.stamina == highest_stamina][0]

        current_players = [player_with_lower_stamina, player_with_highest_value]

        for index in range(2):
            current_attacker = current_players[0] if index % 2 == 0 else current_players[1]
            other_player = current_players[1] if index % 2 == 0 else current_players[0]

            other_player.stamina -= current_attacker.stamina / 2

            if other_player.stamina <= 0:
                other_player.stamina = 0

            winner = current_attacker
            return f"Winner: {winner.name}"

    def next_day(self):

        for player in self.players:
            value = player.stamina - player.age * 2

            if value < 0:
                player.stamina = 0
            else:
                player.stamina = value

            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):

        players = '\n'.join([str(player) for player in self.players])
        supplies = '\n'.join([supply.details() for supply in self.supplies])

        return f"{players}\n{supplies}"

    def find_player(self, name):
        player = [p for p in self.players if p.name == name]
        return player[0] if player else None

    def find_last_supply_from_the_given_type(self, sus_type):
        sustenance = [s for s in self.supplies if type(s).__name__ == sus_type]
        return sustenance[-1] if sustenance else None

