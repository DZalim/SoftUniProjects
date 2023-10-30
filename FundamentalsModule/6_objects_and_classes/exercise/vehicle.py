class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        returning_string = ""
        if self.price <= money and self.owner is None:
            change = money - self.price
            returning_string = f"Successfully bought a {self.type}. Change: {change:.2f}"
            self.owner = owner
        elif self.price > money:
            returning_string = "Sorry, not enough money"
        else:
            returning_string = "Car already sold"
        return returning_string


    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"


    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


#Test
vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
