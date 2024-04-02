from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):

    def setUp(self):
        self.robot = Robot('10', 'Education', 10, 1000.00)

    def test_correct_initialization(self):
        self.assertEqual('10', self.robot.robot_id)
        self.assertEqual('Education', self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(1000.00, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_setter_invalid(self):

        expected_message = "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'"

        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'Science'

        self.assertEqual(expected_message, str(ve.exception))

    def test_price_setter_invalid(self):

        expected_message = "Price cannot be negative!"

        with self.assertRaises(ValueError) as ve:
            self.robot.price = -10

        self.assertEqual(expected_message, str(ve.exception))

    def test_upgrade_with_existing_hardware_component(self):
        self.robot.hardware_upgrades = ['teaching']
        expected_message = "Robot 10 was not upgraded."

        self.assertEqual(expected_message, self.robot.upgrade('teaching', 1000))

    def test_upgrade_with_not_existing_hardware_component(self):
        expected_message = 'Robot 10 was upgraded with teaching.'
        price = self.robot.price + (1000 * 1.5)
        self.assertEqual(expected_message, self.robot.upgrade('teaching', 1000))
        self.assertEqual(price, self.robot.price)
        self.assertEqual(['teaching'], self.robot.hardware_upgrades)

    def test_update_with_less_version_and_available_capacity(self):
        self.robot.software_updates = [5]
        expected_message = "Robot 10 was not updated."
        self.assertEqual(expected_message, self.robot.update(4, 5))

    def test_update_with_less_available_capacity(self):
        expected_message = "Robot 10 was not updated."
        self.assertEqual(expected_message, self.robot.update(6, 11))

    def test_update_with_new_version_and_available_capacity(self):
        self.robot.software_updates = [5]
        expected_message = f'Robot 10 was updated to version 6.0.'
        capacity = self.robot.available_capacity - 5
        self.assertEqual(expected_message, self.robot.update(6.0, 5))
        self.assertEqual([5, 6], self.robot.software_updates)
        self.assertEqual(capacity, self.robot.available_capacity)

    def test_greater_price(self):
        self.other_robot = Robot('11', 'Education', 10, 500.00)
        expected_message = 'Robot with ID 10 is more expensive than Robot with ID 11.'
        self.assertEqual(expected_message, self.robot.__gt__(self.other_robot))

    def test_equal_price(self):
        self.other_robot = Robot('11', 'Education', 10, 1000.00)
        expected_message = 'Robot with ID 10 costs equal to Robot with ID 11.'
        self.assertEqual(expected_message, self.robot.__gt__(self.other_robot))

    def test_less_price(self):
        self.other_robot = Robot('11', 'Education', 10, 1500.00)
        expected_message = 'Robot with ID 10 is cheaper than Robot with ID 11.'
        self.assertEqual(expected_message, self.robot.__gt__(self.other_robot))


if __name__ == '__main__':
    main()
