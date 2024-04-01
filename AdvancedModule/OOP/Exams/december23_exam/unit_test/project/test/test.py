from unittest import TestCase, main
from collections import deque

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.station = RailwayStation("Station A")

    def test_init(self):
        self.assertEqual(self.station.name, "Station A")
        self.assertIsInstance(self.station.arrival_trains, deque)
        self.assertIsInstance(self.station.departure_trains, deque)

    def test_valid_name_property(self):
        self.assertEqual(self.station.name, "Station A")

    def test_invalid_name_property(self):

        with self.assertRaises(ValueError) as ve:
            self.station.name = "Ab"

        expected_message = "Name should be more than 3 symbols!"

        self.assertEqual(expected_message, str(ve.exception))

    def test_new_arrival_on_board(self):
        new_arrival_train = "Train 1"

        self.station.arrival_trains.append(new_arrival_train)
        self.assertEqual(self.station.arrival_trains[-1], "Train 1")

    def test_train_has_arrived_invalid(self):
        first_train = "Train 1"
        second_train = "Train 2"
        self.station.new_arrival_on_board(first_train)
        self.station.new_arrival_on_board(second_train)

        expected_message = f"There are other trains to arrive before {second_train}."

        self.assertEqual(self.station.train_has_arrived(second_train),
                         expected_message)

        self.assertEqual(deque(['Train 1', 'Train 2']), self.station.arrival_trains)
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_train_has_arrived_valid(self):
        first_train = "Train 1"
        second_train = "Train 2"
        self.station.new_arrival_on_board(first_train)
        self.station.new_arrival_on_board(second_train)

        expected_message = f"{first_train} is on the platform and will leave in 5 minutes."

        self.assertEqual(self.station.train_has_arrived(first_train),
                         expected_message)
        self.assertEqual(deque(['Train 2']), self.station.arrival_trains)
        self.assertEqual(deque(['Train 1']), self.station.departure_trains)

    def test_train_has_left_valid(self):
        first_train = "Train 1"
        second_train = "Train 2"
        self.station.arrival_trains.append(first_train)
        self.station.arrival_trains.append(second_train)
        self.station.train_has_arrived(first_train)

        self.assertTrue(self.station.train_has_left(first_train))

    def test_train_has_left_invalid(self):
        first_train = "Train 1"
        second_train = "Train 2"
        self.station.arrival_trains.append(first_train)
        self.station.arrival_trains.append(second_train)
        self.station.train_has_arrived(first_train)

        self.assertFalse(self.station.train_has_left(second_train))


if __name__ == '__main__':
    main()
