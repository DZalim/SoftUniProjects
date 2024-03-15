from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00
    ADDITIONAL_REDUCE = 0.05

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)

    def drive(self, mileage: float):
        percent_to_reduce = mileage / self.max_mileage
        self.battery_level *= (1 - percent_to_reduce)
        self.battery_level *= self.ADDITIONAL_REDUCE
        self.battery_level = round(self.battery_level)
