from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):

    def setUp(self):
        self.plant = Plantation(100)

    def test_correct_initialization(self):
        self.assertEqual(100, self.plant.size)
        self.assertEqual({}, self.plant.plants)
        self.assertEqual([], self.plant.workers)

    def test_size_setter_raise_error(self):
        expected_message = "Size must be positive number!"

        with self.assertRaises(ValueError) as ve:
            self.plant.size = -5

        self.assertEqual(expected_message, str(ve.exception))

    def test_hire_worker_raises_error(self):
        self.plant.workers = ['Pesho']
        expected_message = "Worker already hired!"

        with self.assertRaises(ValueError) as ve:
            self.plant.hire_worker('Pesho')

        self.assertEqual(expected_message, str(ve.exception))

    def test_hire_worker(self):
        result = self.plant.hire_worker('Pesho')
        expected_message = "Pesho successfully hired."

        self.assertEqual(expected_message, result)
        self.assertEqual(['Pesho'], self.plant.workers)

    def test__len__method(self):
        self.plant.plants = {'Pesho': ['Rose', 'Jasmine'], 'Ivan': ['Tulip']}
        self.assertEqual(3, self.plant.__len__())

    def test_planting_when_worker_does_not_exist_in_workers(self):
        expected_message = "Worker with name Pesho is not hired!"

        with self.assertRaises(ValueError) as ve:
            self.plant.planting('Pesho', 'Rose')

        self.assertEqual(expected_message, str(ve.exception))

    def test_planting_when_len_greater_than_size(self):
        self.plant.size = 3
        self.plant.workers = ['Pesho', 'Ivan']
        self.plant.plants = {'Pesho': ['Rose', 'Jasmine'], 'Ivan': ['Tulip']}
        expected_message = "The plantation is full!"

        with self.assertRaises(ValueError) as ve:
            self.plant.planting('Pesho', 'Rose')

        self.assertEqual(expected_message, str(ve.exception))

    def test_planting_if_worker_exit_in_plants(self):
        self.plant.size = 3
        self.plant.workers = ['Pesho']
        self.plant.plants = {'Pesho': ['Rose']}
        expected_message = "Pesho planted Jasmine."
        result = self.plant.planting('Pesho', 'Jasmine')
        self.assertEqual(expected_message, result)
        self.assertEqual({'Pesho': ['Rose', 'Jasmine']}, self.plant.plants)

    def test_planting_if_worker_does_not_exit_in_plants(self):
        self.plant.size = 3
        self.plant.workers = ['Pesho']
        expected_message = f"Pesho planted it's first Rose."
        result = self.plant.planting('Pesho', 'Rose')

        self.assertEqual(expected_message, result)
        self.assertEqual({'Pesho': ['Rose']}, self.plant.plants)

    def test__str__method(self):
        self.plant.size = 3
        self.plant.workers = ['Pesho', 'Ivan']
        self.plant.plants = {'Pesho': ['Rose', 'Jasmine'], 'Ivan': ['Tulip']}

        expected_message = '\n'.join(["Plantation size: 3", 'Pesho, Ivan', 'Pesho planted: Rose, Jasmine', 'Ivan planted: Tulip'])

        self.assertEqual(expected_message, str(self.plant))

    def test__rpr__method(self):
        self.plant.size = 3
        self.plant.workers = ['Pesho', 'Ivan']

        expected_message = '\n'.join(['Size: 3', 'Workers: Pesho, Ivan'])

        self.assertEqual(expected_message, self.plant.__repr__())


if __name__ == "__main__":
    main()
