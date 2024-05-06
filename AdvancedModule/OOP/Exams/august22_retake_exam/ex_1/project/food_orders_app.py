from typing import List

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:

    ALLOWED_MEALS = {
        'Starter': Starter,
        'MainDish': MainDish,
        'Dessert': Dessert
    }

    receipt_id = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):
        current_client = self.search_client(client_phone_number)

        if current_client:
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):

        for meal in meals:
            if meal.__class__.__name__ in self.ALLOWED_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        result = []

        for meal in self.menu:
            result.append(meal.details())

        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = self.search_client(client_phone_number)
        if not client:
            client = Client(client_phone_number)

        for meal_name, quantity in meal_names_and_quantities.items():
            meal = [meal for meal in self.menu if meal_name == meal.name][0]

            if not meal:
                raise Exception(f"{meal_name} is not on the menu!")

            if quantity > meal.quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")

        meal_names = []
        total_amount = 0

        for meal_name, quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal_name == meal.name:
                    client.shopping_cart.append(meal)
                    client_bill = meal.price * quantity
                    client.bill += client_bill
                    meal.quantity -= quantity
                    meal_names.append(meal_name)
                    total_amount += client_bill

        client.orders.extend(meal_names)

        names = ', '.join(client.orders)
        return f"Client {client_phone_number} successfully ordered {names} for {total_amount:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.search_client(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for client_meal in client.shopping_cart:
            for meal in self.menu:
                if client_meal.name == meal.name:
                    meal.quantity += client_meal.quantity

        client.bill = 0
        client.shopping_cart = []
        client.orders = []

    def finish_order(self, client_phone_number: str):
        client = self.search_client(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        bill = client.bill
        client.bill = 0
        client.shopping_cart = []
        client.orders = []

        FoodOrdersApp.receipt_id += 1
        return f"Receipt #{FoodOrdersApp.receipt_id} with total amount of {bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


    def search_client(self, number):
        client = [c for c in self.clients_list if c.phone_number == number]
        return client[0] if client else None
