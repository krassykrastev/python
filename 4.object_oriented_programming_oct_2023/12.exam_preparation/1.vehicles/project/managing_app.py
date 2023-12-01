from typing import List

from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLES = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan
    }
    ROUTE_ID = 1

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[PassengerCar, CargoVan] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if driving_license_number in [x.driving_license_number for x in self.users]:
            return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ManagingApp.VALID_VEHICLES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if license_plate_number in [x.license_plate_number for x in self.vehicles]:
            return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(ManagingApp.VALID_VEHICLES[vehicle_type](brand, model, license_plate_number))

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if all([route.start_point == start_point, route.end_point == end_point]):
                if route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."

                elif route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."

                elif route.length > length:
                    route.is_locked = True

        self.routes.append(Route(start_point, end_point, length, ManagingApp.ROUTE_ID))
        ManagingApp.ROUTE_ID += 1

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route = next(filter(lambda r: r.route_id == route_id, self.routes))
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        vehicles_in_need_of_repair = [v for v in self.vehicles if v.is_damaged]

        if len(vehicles_in_need_of_repair) > count:
            sorted_vehicles = sorted(vehicles_in_need_of_repair, key=lambda x: (x.brand, x.model))
            vehicles_in_need_of_repair = sorted_vehicles[:count]

        for vehicle in vehicles_in_need_of_repair:
            vehicle.change_status()
            vehicle.recharge()

        return f"{len(vehicles_in_need_of_repair)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda x: -x.rating)
        result = ["*** E-Drive-Rent ***"]
        result.extend([str(user) for user in sorted_users])

        return '\n'.join(result)
