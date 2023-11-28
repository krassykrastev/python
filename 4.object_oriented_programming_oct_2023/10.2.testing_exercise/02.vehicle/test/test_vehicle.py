from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTest(TestCase):

    def setUp(self):
        self.test_vehicle = Vehicle(3.5, 115.5)

    def test_init(self):
        self.assertEqual(3.5, self.test_vehicle.fuel)
        self.assertEqual(3.5, self.test_vehicle.capacity)
        self.assertEqual(115.5, self.test_vehicle.horse_power)
        self.assertEqual(1.25, self.test_vehicle.fuel_consumption)
        self.assertIsInstance(self.test_vehicle.fuel, float)
        self.assertIsInstance(self.test_vehicle.capacity, float)
        self.assertIsInstance(self.test_vehicle.horse_power, float)
        self.assertIsInstance(self.test_vehicle.fuel_consumption, float)
        self.assertIsInstance(self.test_vehicle.DEFAULT_FUEL_CONSUMPTION, float)

    def test_drive_successful(self):
        self.test_vehicle.drive(2)
        self.assertEqual(1, self.test_vehicle.fuel)

    def test_drive_not_enough_fuel_raised(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.drive(10)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_successful(self):
        self.test_vehicle.fuel = 1
        self.test_vehicle.refuel(1.5)
        self.assertEqual(2.5, self.test_vehicle.fuel)

    def test_refuel_too_much_fuel_raised(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.refuel(100)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        result = str(self.test_vehicle)
        expected = "The vehicle has 115.5 horse power with 3.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
