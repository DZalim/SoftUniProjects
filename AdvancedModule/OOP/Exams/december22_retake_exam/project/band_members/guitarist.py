from project.band_members.musician import Musician


class Guitarist(Musician):
    SKILLS = ["play metal", "play rock", "play jazz"]

    def learn_new_skill(self, new_skill: str):
        return super().learn_new_skill(new_skill)
