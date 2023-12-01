from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=CargoVan.MAX_MILEAGE)

    def drive(self, mileage: float):
        reduction = round(mileage / self.max_mileage * 100) + 5
        self.battery_level -= reduction
