from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:

    VALID_CLIMBERS = {
        'ArcticClimber': ArcticClimber,
        'SummitClimber': SummitClimber
    }

    VALID_PEAKS = {
        'ArcticPeak': ArcticPeak,
        'SummitPeak': SummitPeak
    }

    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBERS:
            return f"{climber_type} doesn't exist in our register."

        try:
            current_climber = next(filter(lambda climber: climber.name == climber_name, self.climbers))
        except StopIteration:
            registered_climber = self.VALID_CLIMBERS[climber_type](climber_name)
            self.climbers.append(registered_climber)

            return f"{climber_name} is successfully registered as a {climber_type}."

        return f"{climber_name} has been already registered."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAKS:
            return f"{peak_type} is an unknown type of peak."

        peak_to_add = self.VALID_PEAKS[peak_type](peak_name, peak_elevation)
        self.peaks.append(peak_to_add)

        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):

        try:
            peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            return

        try:
            climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return

        recommended_gear = peak.get_recommended_gear()
        missing_gear = []

        for g in recommended_gear:
            if g not in gear:
                missing_gear.append(g)

        if missing_gear:
            climber.is_prepared = False
            return (f"{climber_name} is not prepared to climb {peak_name}. "
                    f"Missing gear: {', '.join(sorted(missing_gear))}.")
        else:
            return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name: str, peak_name: str):

        try:
            current_climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            current_peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if current_climber.can_climb() and current_climber.is_prepared:
            current_climber.climb(current_peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {current_peak.difficulty_level}."

        if not current_climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        current_climber.rest()
        return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):

        sorted_climbers = sorted([climber for climber in self.climbers if climber.conquered_peaks],
                                 key=lambda climber: (-len(climber.conquered_peaks), climber.name))

        climber_statistics = "\n".join(str(c) for c in sorted_climbers)

        return (f"Total climbed peaks: {len(self.peaks)}\n"
                f"**Climber's statistics:**\n"
                f"{climber_statistics}")
