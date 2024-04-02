from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self):
        self.player = TennisPlayer('George', 28, 100)

    def test_correct_initialization(self):
        self.assertEqual('George', self.player.name)
        self.assertEqual(28, self.player.age)
        self.assertEqual(100, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_setter_raises_error(self):
        expected_message = "Name should be more than 2 symbols!"

        with self.assertRaises(ValueError) as ve:
            self.player.name = "Ge"

        self.assertEqual(expected_message, str(ve.exception))

    def test_age_setter_raises_error(self):
        expected_message = "Players must be at least 18 years of age!"

        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        self.assertEqual(expected_message, str(ve.exception))

    def test_add_new_wins_with_existing_tournament_name(self):
        self.player.wins = ['Europe']
        expected_message = "Europe has been already added to the list of wins!"

        self.assertEqual(expected_message, self.player.add_new_win('Europe'))

    def test_add_new_wins_with_not_existing_tournament_name(self):
        self.player.add_new_win('Europe')
        self.assertEqual(['Europe'], self.player.wins)

    def test_less_than_points(self):
        self.other_player = TennisPlayer('Peter', 28, 200)
        expected_message = 'Peter is a top seeded player and he/she is better than George'
        self.assertEqual(expected_message, self.player.__lt__(self.other_player))

    def test_greater_than_points(self):
        self.other_player = TennisPlayer('Peter', 28, 50)
        expected_message = 'George is a better player than Peter'
        self.assertEqual(expected_message, self.player.__lt__(self.other_player))

    def test_info(self):
        self.player.wins.append('Europe')
        self.player.wins.append('Balkans')

        expected_result = f"Tennis Player: George\n" \
               f"Age: 28\n" \
               f"Points: 100.0\n" \
               f"Tournaments won: Europe, Balkans"

        self.assertEqual(expected_result, str(self.player))


if __name__ == "__main__":
    main()
