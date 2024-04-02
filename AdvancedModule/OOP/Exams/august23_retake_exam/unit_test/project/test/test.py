from unittest import TestCase, main
from project.trip import Trip


class TestTrip(TestCase):

    def setUp(self):
        self.current_trip = Trip(2000, 2, True)

    def test_initialization_family_trip(self):
        self.assertEqual(self.current_trip.budget, 2000)
        self.assertEqual(self.current_trip.travelers, 2)

    def test_invalid_travelers_property(self):

        with self.assertRaises(ValueError) as ve:
            self.current_trip.travelers = 0

        expected_message = 'At least one traveler is required!'

        self.assertEqual(expected_message, str(ve.exception))

    def test_is_not_family_property(self):
        self.current_trip.travelers = 1
        self.current_trip.is_family = True
        self.assertFalse(self.current_trip.is_family)

    def test_is_family_property(self):
        self.current_trip.travelers = 2
        self.assertTrue(self.current_trip.is_family)

    def test_book_a_trip_invalid_destination(self):
        expected_message = 'This destination is not in our offers, please choose a new one!'
        self.assertEqual(self.current_trip.book_a_trip('Greece'), expected_message)

    def test_book_a_trip_valid_destination_and_invalid_budget(self):
        self.current_trip.budget = 450
        expected_message = 'Your budget is not enough!'
        self.assertEqual(self.current_trip.book_a_trip('Bulgaria'), expected_message)

    def test_book_a_trip_valid_destination_and_valid_budget_is_family(self):
        required_price = 500 * 0.9 * self.current_trip.travelers
        budget = self.current_trip.budget - required_price
        trip_price = {'Bulgaria': required_price}

        expected_message = f'Successfully booked destination Bulgaria! Your budget left is {budget:.2f}'

        self.assertEqual(expected_message, self.current_trip.book_a_trip('Bulgaria'))
        self.assertEqual(self.current_trip.budget, budget)
        self.assertEqual(self.current_trip.booked_destinations_paid_amounts, trip_price)

    def test_book_a_trip_valid_destination_and_valid_budget_is_not_family(self):
        self.current_trip.travelers = 1
        self.current_trip.is_family = False
        required_price = 500 * self.current_trip.travelers
        budget = self.current_trip.budget - required_price
        trip_price = {'Bulgaria': required_price}

        expected_message = f'Successfully booked destination Bulgaria! Your budget left is {budget:.2f}'

        self.assertEqual(expected_message, self.current_trip.book_a_trip('Bulgaria'))
        self.assertEqual(self.current_trip.budget, budget)
        self.assertEqual(self.current_trip.booked_destinations_paid_amounts, trip_price)

    def test_booking_status_without_trips(self):
        self.current_trip.booked_destinations_paid_amounts = {}
        expected_message = f'No bookings yet. Budget: {self.current_trip.budget:.2f}'
        self.assertEqual(expected_message, self.current_trip.booking_status())
        self.assertEqual(self.current_trip.booked_destinations_paid_amounts, {})

    def test_booking_status_with_trips(self):
        self.current_trip.budget = 20000

        bulgaria_pay = 500 * 0.9 * self.current_trip.travelers
        australia_pay = 5700 * 0.9 * self.current_trip.travelers

        budget = self.current_trip.budget - bulgaria_pay - australia_pay

        self.current_trip.book_a_trip('Bulgaria')
        self.current_trip.book_a_trip('Australia')

        result = ["Booked Destination: Australia",
        f"Paid Amount: {australia_pay:.2f}",
        "Booked Destination: Bulgaria",
        f"Paid Amount: {bulgaria_pay:.2f}",
        "Number of Travelers: 2",
        f"Budget Left: {budget:.2f}"
                  ]

        self.assertEqual(self.current_trip.booking_status(), '\n'.join(result))


if __name__ == "__main__":
    main()
