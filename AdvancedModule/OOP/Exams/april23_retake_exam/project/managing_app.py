from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    VALID_VEHICLES = {
        'PassengerCar': PassengerCar,
        'CargoVan': CargoVan
    }

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        current_user = self.get_user(driving_license_number)

        if current_user:
            return f"{driving_license_number} has already been registered to our platform."

        user_to_add = User(first_name, last_name, driving_license_number)
        self.users.append(user_to_add)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        vehicle = self.get_vehicle(license_plate_number)
        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        vehicle_to_add = self.VALID_VEHICLES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle_to_add)

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_id = len(self.routes) + 1

        current_route = self.get_route_by_point(start_point, end_point)
        if current_route and current_route.length == length:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        if current_route and current_route.length < length:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        if current_route and current_route.length > length:
            current_route.is_locked = True

        route_to_create = Route(start_point, end_point, length, route_id)
        self.routes.append(route_to_create)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int, is_accident_happened: bool):
        user = self.get_user(driving_license_number)
        vehicle = self.get_vehicle(license_plate_number)
        route = self.get_route_by_id(route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):

        sorted_vehicle = sorted([vehicle for vehicle in self.vehicles if vehicle.is_damaged],
                             key=lambda vehicle: (vehicle.brand, vehicle.model))

        count_of_repaired_vehicles = min(len(sorted_vehicle), count)

        for current_vehicle_index in range(count_of_repaired_vehicles):
            vehicle = sorted_vehicle[current_vehicle_index]
            vehicle.change_status()
            vehicle.recharge()

        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        sorted_user = sorted([user for user in self.users], key=lambda user: -user.rating)
        user_info = '\n'.join(str(user) for user in sorted_user)

        return (f"*** E-Drive-Rent ***\n"
                f"{user_info}")

    def get_user(self, license_number):
        current_user = [user for user in self.users if user.driving_license_number == license_number]
        return current_user[0] if current_user else None

    def get_vehicle(self, plate_number):
        vehicle = [vehicle for vehicle in self.vehicles if vehicle.license_plate_number == plate_number]
        return vehicle[0] if vehicle else None

    def get_route_by_point(self, start, end):
        route = [route for route in self.routes
                 if route.start_point == start and route.end_point == end]

        return route[0] if route else None

    def get_route_by_id(self, route_id):
        route = [route for route in self.routes if route.route_id == route_id]
        return route[0] if route else None
