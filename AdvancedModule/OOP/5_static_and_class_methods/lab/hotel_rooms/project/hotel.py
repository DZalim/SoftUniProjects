from typing import List
from project.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.guests: int = 0
        self.rooms: List[Room] = []

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number: str, people: int):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            return

        room_is_taken = room.take_room(people)

        if not room_is_taken:
            self.guests += people

    def free_room(self, room_number):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            return

        people = room.guests
        room_is_free = room.free_room()

        if not room_is_free:
            self.guests -= people

    def status(self):
        free_rooms = ', '.join(str(room.number) for room in self.rooms if not room.is_taken)
        taken_rooms = ', '.join(str(room.number) for room in self.rooms if room.is_taken)

        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {free_rooms}\n"
                f"Taken rooms: {taken_rooms}")
