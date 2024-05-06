from typing import List

from project.meals.meal import Meal


class Client:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: List[Meal] = []
        self.bill = 0.0
        self.orders = []

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):

        contain_only_digits = [v for v in value if v.isdigit()]

        if not (len(value) == 10 and value.startswith('0') and len(contain_only_digits) == 10):
            raise ValueError("Invalid phone number!")

        self.__phone_number = value
