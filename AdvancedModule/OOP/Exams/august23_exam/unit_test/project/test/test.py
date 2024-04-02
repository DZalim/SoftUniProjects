from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):

    def setUp(self):
        self.current_car = SecondHandCar('Toyota', 'hatchback', 150000, 10000)

    def test_correct_initialization(self):
        self.assertEqual('Toyota', self.current_car.model)
        self.assertEqual('hatchback', self.current_car.car_type)
        self.assertEqual(150000, self.current_car.mileage)
        self.assertEqual(10000, self.current_car.price)
        self.assertEqual([], self.current_car.repairs)

    def test_price_property_error_raises(self):

        with self.assertRaises(ValueError) as ve:
            self.current_car.price = 1

        expected_message = 'Price should be greater than 1.0!'

        self.assertEqual(str(ve.exception), expected_message)

    def test_mileage_property_error_raises(self):

        with self.assertRaises(ValueError) as ve:
            self.current_car.mileage = 100

        expected_message = 'Please, second-hand cars only! Mileage must be greater than 100!'

        self.assertEqual(str(ve.exception), expected_message)

    def test_set_promotional_price_raises_error(self):

        with self.assertRaises(ValueError) as ve:
            self.current_car.set_promotional_price(11000)

        expected_message = 'You are supposed to decrease the price!'
        self.assertEqual(str(ve.exception), expected_message)

    def test_set_promotional_price_valid(self):
        expected_message = 'The promotional price has been successfully set.'
        self.assertEqual(expected_message, self.current_car.set_promotional_price(9000))
        self.assertEqual(9000, self.current_car.price)

    def test_need_repair_insufficient_amount(self):
        expected_message = 'Repair is impossible!'
        self.assertEqual(expected_message, self.current_car.need_repair(6000, 'change_turbo'))

    def test_need_repair_sufficient_amount(self):
        expected_message = f'Price has been increased due to repair charges.'
        price = self.current_car.price + 2000
        self.assertEqual(expected_message, self.current_car.need_repair(2000, 'change oil'))
        self.assertEqual(price, self.current_car.price)
        self.assertEqual(['change oil'], self.current_car.repairs)


    def test_price_comparison_other_car_type(self):
        self.other_car = SecondHandCar('Toyota', 'sedan', 110000, 11000)
        expected_message = 'Cars cannot be compared. Type mismatch!'
        self.assertEqual(expected_message, self.current_car.__gt__(self.other_car))

    def test_price_comparison_each_car_type(self):
        self.other_car = SecondHandCar('Toyota', 'hatchback', 110000, 11000)
        expected_message = False
        self.assertEqual(expected_message, self.current_car.__gt__(self.other_car))

    def test_string_info(self):
        expected_message = f"""Model Toyota | Type hatchback | Milage 150000km
Current price: 10000.00 | Number of Repairs: 0"""

        self.assertEqual(expected_message, str(self.current_car))

if __name__ == '__main__':
    main()
