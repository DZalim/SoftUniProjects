from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:

    VALID_EQUIPMENT = {
        'KneePad': KneePad,
        'ElbowPad': ElbowPad
    }

    VALID_TEAMS = {
        'OutdoorTeam': OutdoorTeam,
        'IndoorTeam': IndoorTeam
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):

        for char in value:
            if not char.isalnum():
                raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT:
            raise Exception("Invalid equipment type!")

        current_equipment = self.VALID_EQUIPMENT[equipment_type]()
        self.equipment.append(current_equipment)

        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS:
            raise Exception("Invalid team type!")

        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."

        current_team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(current_team)

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        current_equipment = self.get_equipment(equipment_type)
        current_team = self.get_team(team_name)

        if current_equipment.price > current_team.budget:
            raise Exception("Budget is not enough!")

        self.equipment.remove(current_equipment)
        current_team.equipment.append(current_equipment)
        current_team.budget -= current_equipment.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        current_team = self.get_team(team_name)

        if not current_team:
            raise Exception("No such team!")

        if current_team.wins > 0:
            raise Exception(f"The team has {current_team.wins} wins! Removal is impossible!")

        self.teams.remove(current_team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        equipments = [equipment.increase_price()
                      for equipment in self.equipment if equipment_type == equipment.__class__.__name__]
        return f"Successfully changed {len(equipments)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        first_team = self.get_team(team_name1)
        second_team = self.get_team(team_name2)

        if first_team.__class__.__name__ != second_team.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        first_team_points = first_team.advantage + sum([equipment.protection for equipment in first_team.equipment])
        second_team_points = second_team.advantage + sum([equipment.protection for equipment in second_team.equipment])

        if first_team_points == second_team_points:
            return "No winner in this game."

        winner = first_team if first_team_points > second_team_points else second_team
        winner.win()
        return f"The winner is {winner.name}."

    def get_statistics(self):

        sorted_teams = sorted([team for team in self.teams], key=lambda team: -team.wins)

        team_statistics = '\n'.join(team.get_statistics() for team in sorted_teams)

        return (f"Tournament: {self.name}\n"
                f"Number of Teams: {len(self.teams)}\n"
                f"Teams:\n"
                f"{team_statistics}")

    def get_equipment(self, type_of_equipment):
        equipments = [equipment for equipment in self.equipment if type_of_equipment == equipment.__class__.__name__]
        return equipments[-1] if equipments else None

    def get_team(self, name):
        team = [team for team in self.teams if name == team.name]
        return team[0] if team else None
