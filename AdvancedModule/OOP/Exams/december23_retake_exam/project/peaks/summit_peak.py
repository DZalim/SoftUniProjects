from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):

    @staticmethod
    def get_recommended_gear():
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def calculate_difficulty_level(self):
        if self.elevation > 2500:
            return "Extreme"
        elif 1500 <= self.elevation <= 2500:
            return "Advanced"
