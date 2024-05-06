from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):

    def setUp(self):
        self.shop = ShoppingCart('Sofia', 10000)

    def test_correct_initialization(self):
        self.assertEqual('Sofia', self.shop.shop_name)
        self.assertEqual(10000, self.shop.budget)
        self.assertEqual({}, self.shop.products)

    def test_shop_name_property_first_letter_not_upper(self):

        expected_message = "Shop must contain only letters and must start with capital letter!"

        with self.assertRaises(ValueError) as ve:
            self.shop.shop_name = 'sofia'

        self.assertEqual(expected_message, str(ve.exception))

    def test_shop_name_property_letters_not_alpha(self):

        expected_message = "Shop must contain only letters and must start with capital letter!"

        with self.assertRaises(ValueError) as ve:
            self.shop.shop_name = '12354'

        self.assertEqual(expected_message, str(ve.exception))

    def test_add_to_cart_error_raises(self):
        expected_message = "Product chocolate cost too much!"

        with self.assertRaises(ValueError) as ve:
            self.shop.add_to_cart('chocolate', 200)

        self.assertEqual(expected_message, str(ve.exception))

    def test_add_to_cart_correct(self):
        result = self.shop.add_to_cart('Chocolate', 10)
        expected_message = "Chocolate product was successfully added to the cart!"

        self.assertEqual(expected_message, result)
        self.assertEqual({'Chocolate': 10}, self.shop.products)

    def test_remove_from_cart_not_existing_product(self):
        expected_message = "No product with name chocolate in the cart!"

        with self.assertRaises(ValueError) as ve:
            self.shop.remove_from_cart('chocolate')

        self.assertEqual(expected_message, str(ve.exception))

    def test_remove_from_cart(self):
        self.shop.products = {'Chocolate': 10}

        expected_result = "Product Chocolate was successfully removed from the cart!"
        result = self.shop.remove_from_cart('Chocolate')

        self.assertEqual(expected_result, result)
        self.assertEqual({}, self.shop.products)

    def test_add_another_product(self):
        self.shop.products = {'Chocolate': 10}

        self.other_shop = ShoppingCart('Varna', 2000)
        self.other_shop.products = {'Banana': 30}

        new_name = 'SofiaVarna'
        new_budget = 12000
        self.new_shop = ShoppingCart(new_name, new_budget)
        self.new_shop.products = {'Chocolate': 10, 'Banana': 30}

        #self.assertEqual(self.shop.__add__(self.other_shop), self.new_shop)
        self.assertEqual({'Chocolate': 10, 'Banana': 30}, self.new_shop.products)


    def test_buy_products_without_budget(self):

        expected_message = "Not enough money to buy the products! Over budget with 10.00lv!"

        with self.assertRaises(ValueError) as ve:
            self.shop.products = {'Chocolate': 10, 'Banana': 30}
            self.shop.budget = 30
            self.shop.buy_products()

        self.assertEqual(expected_message, str(ve.exception))

    def test_buy_products(self):
        self.shop.products = {'Chocolate': 10, 'Banana': 30}
        expected_message = 'Products were successfully bought! Total cost: 40.00lv.'
        result = self.shop.buy_products()
        self.assertEqual(expected_message, result)


if __name__ == "__main__":
    main()
