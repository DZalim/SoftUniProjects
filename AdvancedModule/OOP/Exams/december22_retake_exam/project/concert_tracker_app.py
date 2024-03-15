from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    VALID_MUSICIANS = {
        'Guitarist': Guitarist,
        'Drummer': Drummer,
        'Singer': Singer
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")

        musician = self.get_musician(name)
        if musician:
            raise Exception(f"{name} is already a musician!")

        musician_to_add = self.VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(musician_to_add)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = self.get_band(name)
        if band:
            raise Exception(f"{name} band is already created!")

        band_to_create = Band(name)
        self.bands.append(band_to_create)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self.get_concert_place(place)
        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        concert_to_create = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert_to_create)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.get_musician(musician_name)
        band = self.get_band(band_name)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.get_band(band_name)

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician_in_band = [musician for musician in band.members if musician.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician_in_band)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        concert = self.get_concert_place(concert_place)
        band = self.get_band(band_name)

        members_count = {
            'Drummer': 0,
            'Singer': 0,
            'Guitarist': 0
        }

        for member in band.members:
            type_of_member = member.__class__.__name__
            members_count[type_of_member] += 1

        for count in members_count.values():
            if count < 1:
                raise Exception("{band name} can't start the concert because it doesn't have enough members!")

        NEEDEED_SKILLS = {
            'Rock': {
                'Drummer': ['play the drums with drumsticks'],
                'Singer': ['sing high pitch notes'],
                'Guitarist': ['play rock']
            },
            'Metal': {
                'Drummer': ['play the drums with drumsticks'],
                'Singer': ['sing low pitch notes'],
                'Guitarist': ['play metal']
            },
            'Jazz': {
                'Drummer': ['play the drums with drum brushes'],
                'Singer': ['sing low pitch notes', 'sing high pitch notes'],
                'Guitarist': ['play jazz']
            }
        }

        for member in band.members:
            type_of_member = member.__class__.__name__
            get_needed_skills = NEEDEED_SKILLS[concert.genre][type_of_member]
            for skill in get_needed_skills:
                if skill not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."

    def get_musician(self, name):
        musician = [musician for musician in self.musicians if name == musician.name]
        return musician[0] if musician else None

    def get_band(self, name):
        band = [band for band in self.bands if name == band.name]
        return band[0] if band else None

    def get_concert_place(self, place):
        concert = [concert for concert in self.concerts if place == concert.place]
        return concert[0] if concert else None
