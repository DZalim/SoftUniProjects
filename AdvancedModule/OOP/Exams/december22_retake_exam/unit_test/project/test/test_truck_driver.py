from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):

    def setUp(self):
        self.driver = TruckDriver('George', 10.0)

    def test_correct_initialization(self):
        self.assertEqual('George', self.driver.name)
        self.assertEqual(10.0, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_setter_raises_error(self):
        expected_message = "George went bankrupt."

        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -5

        self.assertEqual(expected_message, str(ve.exception))

    def test_add_cargo_offer_with_existing_location(self):
        self.driver.add_cargo_offer('Varna', 200)
        expected_message = "Cargo offer is already added."

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer('Varna', 200)

        self.assertEqual(expected_message, str(ex.exception))

    def test_add_cargo_offer_with_not_existing_location(self):
        expected_message = "Cargo for 200 to Varna was added as an offer."

        self.assertEqual(expected_message, self.driver.add_cargo_offer('Varna', 200))
        self.assertEqual({'Varna': 200}, self.driver.available_cargos)

    def test_drive_best_cargo_offers_with_no_available_offer(self):
        expected_message = "There are no offers available."
        self.assertEqual(expected_message, self.driver.drive_best_cargo_offer())

    def test_drive_best_cargo_offers_with_available_offer(self):
        self.driver.add_cargo_offer('Varna', 200)
        self.driver.add_cargo_offer('Burgas', 100)

        expected_message = "George is driving 200 to Varna."
        earned_money = 200 * self.driver.money_per_mile
        miles = self.driver.miles + 200

        self.assertEqual(expected_message, self.driver.drive_best_cargo_offer())
        self.assertEqual(earned_money, self.driver.earned_money)
        self.assertEqual(miles, self.driver.miles)

    def test_eat(self):
        self.driver.earned_money = 100

        self.driver.eat(250)
        self.driver.eat(500)

        self.assertEqual(self.driver.earned_money, 60)

    def test_sleep(self):
        self.driver.earned_money = 100

        self.driver.sleep(1000)
        self.driver.sleep(2000)

        self.assertEqual(self.driver.earned_money, 10)

    def test_pump_gas(self):
        self.driver.earned_money = 2000

        self.driver.pump_gas(1500)
        self.driver.pump_gas(3000)

        self.assertEqual(self.driver.earned_money, 1000)

    def test_repair_truck(self):
        self.driver.earned_money = 16000

        self.driver.repair_truck(10000)
        self.driver.repair_truck(20000)

        self.assertEqual(self.driver.earned_money, 1000)

    def test_repr_method(self):
        expected_message = "George has 0 miles behind his back."

        self.assertEqual(expected_message, str(self.driver))


if __name__ == '__main__':
    main()
