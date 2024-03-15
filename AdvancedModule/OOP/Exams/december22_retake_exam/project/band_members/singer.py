from project.band_members.musician import Musician


class Singer(Musician):
    SKILLS = ["sing high pitch notes", "sing low pitch notes"]

    def learn_new_skill(self, new_skill: str):
        return super().learn_new_skill(new_skill)
