from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)

    def drive(self, mileage: float):
        percent_to_reduce = mileage / self.max_mileage
        self.battery_level *= (1 - percent_to_reduce)
        self.battery_level = round(self.battery_level)
