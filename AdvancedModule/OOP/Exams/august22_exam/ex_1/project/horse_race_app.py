from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    VALID_HORSE_TYPES = {
        'Appaloosa': Appaloosa,
        'Thoroughbred': Thoroughbred
    }

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        if self.find_horse_by_name(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.VALID_HORSE_TYPES:
            new_horse = self.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)

            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):

        if self.find_jockey(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):

        if self.find_race_type(race_type):
            raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):

        current_jockey = self.find_jockey(jockey_name)
        if not current_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        last_horse = self.find_horse_by_type(horse_type)
        if not last_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if current_jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        last_horse.is_taken = True
        current_jockey.horse = last_horse
        return f"Jockey {jockey_name} will ride the horse {last_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):

        current_race = self.find_race_type(race_type)
        if not current_race:
            raise Exception(f"Race {race_type} could not be found!")

        current_jockey = self.find_jockey(jockey_name)
        if not current_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not current_jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if current_jockey in current_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        current_race.jockeys.append(current_jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):

        horse_race = self.find_race_type(race_type)

        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner_speed = max([jockey.horse.speed for jockey in horse_race.jockeys])
        winner_jockey = [jockey for jockey in horse_race.jockeys if jockey.horse.speed == winner_speed][0]

        return (f"The winner of the {race_type} race, with a speed of {winner_speed}km/h is "
                f"{winner_jockey.name}! Winner's horse: {winner_jockey.horse.name}.")

    def find_horse_by_name(self, name):
        horse = [h for h in self.horses if name == h.name]
        return horse[0] if horse else None

    def find_horse_by_type(self, horse_type):
        horses = [h for h in self.horses if h.__class__.__name__ == horse_type and not h.is_taken]
        return horses[-1] if horses else None

    def find_jockey(self, name):
        jockey = [j for j in self.jockeys if name == j.name]
        return jockey[0] if jockey else None

    def find_race_type(self, type):
        race_type = [race for race in self.horse_races if type == race.race_type]
        return race_type[0] if race_type else None
