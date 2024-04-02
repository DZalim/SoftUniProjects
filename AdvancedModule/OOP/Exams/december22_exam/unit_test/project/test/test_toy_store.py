from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyShelf(TestCase):

    def setUp(self):
        self.toy_store = ToyStore()

    def test_correct_initialization(self):
        result = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertEqual(result, self.toy_store.toy_shelf)

    def test_add_toy_with_not_existing_shelf(self):
        expected_result = "Shelf doesn't exist!"

        with self.assertRaises(Exception) as ve:
            self.toy_store.add_toy('M', 'Mm')

        self.assertEqual(expected_result, str(ve.exception))

    def test_add_toy_with_same_shelf_and_toy_name(self):
        expected_result = "Toy is already in shelf!"

        with self.assertRaises(Exception) as ve:
            self.toy_store.toy_shelf['A'] = 'A'

            self.toy_store.add_toy('A', 'A')

        self.assertEqual(expected_result, str(ve.exception))

    def test_add_toy_with_already_taken_shelf(self):
        expected_result = "Shelf is already taken!"

        with self.assertRaises(Exception) as ve:
            self.toy_store.toy_shelf['A'] = 'Aa'

            self.toy_store.add_toy('A', 'Bb')

        self.assertEqual(expected_result, str(ve.exception))

    def test_add_toy_correct(self):
        expected_result = "Toy:A placed successfully!"

        self.assertEqual(expected_result, self.toy_store.add_toy('A', 'A'))
        self.assertEqual('A', self.toy_store.toy_shelf['A'])

    def test_remove_toy_not_existing_shelf(self):
        expected_result = "Shelf doesn't exist!"

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('M', 'Mm')

        self.assertEqual(expected_result, str(ex.exception))

    def test_remove_toy_with_other_name(self):
        self.toy_store.toy_shelf['A'] = 'A'
        expected_result = "Toy in that shelf doesn't exists!"

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('A', 'B')

        self.assertEqual(expected_result, str(ex.exception))

    def test_remove_toy_success(self):
        self.toy_store.toy_shelf['A'] = 'A'
        expected_result = "Remove toy:A successfully!"
        result = self.toy_store.remove_toy('A', 'A')

        self.assertEqual(expected_result, result)
        self.assertIsNone(self.toy_store.toy_shelf['A'])


if __name__ == '__main__':
    main()
