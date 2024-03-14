from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:

    VALID_DIVERS = {
        'FreeDiver': FreeDiver,
        'ScubaDiver': ScubaDiver
    }

    VALID_FISHES = {
        'PredatoryFish': PredatoryFish,
        'DeepSeaFish': DeepSeaFish
    }

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVERS:
            return f"{diver_type} is not allowed in our competition."

        if self.get_current_diver(diver_name):
            return f"{diver_name} is already a participant."

        current_diver = self.VALID_DIVERS[diver_type](diver_name)
        self.divers.append(current_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISHES:
            return f"{fish_type} is forbidden for chasing in our competition."

        if self.get_current_fish(fish_name):
            return f"{fish_name} is already permitted."

        current_fish = self.VALID_FISHES[fish_type](fish_name, points)
        self.fish_list.append(current_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):

        current_diver = self.get_current_diver(diver_name)
        current_fish = self.get_current_fish(fish_name)

        if not current_diver:
            return f"{diver_name} is not registered for the competition."

        if not current_fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if current_diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if (current_diver.oxygen_level < current_fish.time_to_catch or
                (current_diver.oxygen_level == current_fish.time_to_catch and not is_lucky)):
            current_diver.miss(current_fish.time_to_catch)
            if current_diver.oxygen_level == 0:
                current_diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."

        if ((current_diver.oxygen_level == current_fish.time_to_catch and is_lucky) or
                current_diver.oxygen_level > current_fish.time_to_catch):
            current_diver.hit(current_fish)
            if current_diver.oxygen_level == 0:
                current_diver.update_health_status()
            return f"{diver_name} hits a {current_fish.points}pt. {fish_name}."

    def health_recovery(self):
        divers_with_health_issue = [diver for diver in self.divers if diver.has_health_issue]

        for diver in divers_with_health_issue:
            diver.update_health_status()
            diver.renew_oxy()

        return f"Divers recovered: {len(divers_with_health_issue)}"

    def diver_catch_report(self, diver_name: str):

        current_diver = self.get_current_diver(diver_name)
        fish_details = '\n'.join(fish.fish_details() for fish in current_diver.catch)

        return (f"**{diver_name} Catch Report**\n"
                f"{fish_details}")

    def competition_statistics(self):
        sorted_divers = sorted([diver for diver in self.divers if not diver.has_health_issue],
                               key=lambda diver: (-len(diver.catch), diver.name))

        divers_statistics = '\n'.join(str(diver) for diver in sorted_divers)

        return (f"**Nautical Catch Challenge Statistics**\n"
                f"{divers_statistics}")

    def get_current_diver(self, name):
        current_diver = [diver for diver in self.divers if name == diver.name]

        return current_diver[0] if current_diver else None

    def get_current_fish(self, name):
        current_fish = [fish for fish in self.fish_list if name == fish.name]

        return current_fish[0] if current_fish else None
