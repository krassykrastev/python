from project.truck_driver import TruckDriver

import unittest


class TestTruckDriver(unittest.TestCase):
    def setUp(self) -> None:
        self.t = TruckDriver('Ivan', 1)

    def test_proper_init(self):
        self.assertEqual('Ivan', self.t.name)
        self.assertEqual(1, self.t.money_per_mile)
        self.assertEqual({}, self.t.available_cargos)
        self.assertEqual(0, self.t.earned_money)
        self.assertEqual(0, self.t.miles)

    def test_earned_money_raises_value_error(self):
        test_case = [-1]
        for x in test_case:
            with self.assertRaises(ValueError) as ve:
                self.t.earned_money = x
            self.assertEqual("Ivan went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_success(self):
        expected = "Cargo for 1000 to Varna was added as an offer."
        actual = self.t.add_cargo_offer('Varna', 1000)
        self.assertEqual(expected, actual)
        self.assertEqual({'Varna': 1000}, self.t.available_cargos)

    def test_add_cargo_exception(self):
        self.t.add_cargo_offer('Varna', 1000)
        with self.assertRaises(Exception) as ex:
            self.t.add_cargo_offer('Varna', 20)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_drive_best_cargo_success(self):
        self.t.add_cargo_offer('Plovdiv', 1)
        self.t.add_cargo_offer('Sofia', 2)
        self.t.add_cargo_offer('Varna', 10)
        self.t.add_cargo_offer('Burgas', 5)
        expected = "Ivan is driving 10 to Varna."
        actual = self.t.drive_best_cargo_offer()
        self.assertEqual(expected, actual)
        self.assertEqual(10, self.t.earned_money)
        self.assertEqual(10, self.t.miles)

    def test_drive_lots_of_miles_makes_money(self):
        self.t.add_cargo_offer('Plovdiv', 2000)
        self.t.money_per_mile = 10
        self.assertEqual(0, self.t.earned_money)

        self.t.drive_best_cargo_offer()

        self.assertEqual(19250, self.t.earned_money)

    def test_drive_lots_of_miles_went_bankrupt(self):
        self.t.add_cargo_offer('Plovdiv', 2000)
        self.t.money_per_mile = 0.1
        self.assertEqual(0, self.t.earned_money)

        with self.assertRaises(ValueError) as ve:
            self.t.drive_best_cargo_offer()
        self.assertEqual("Ivan went bankrupt.", str(ve.exception))

    def test_drive_no_location(self):
        self.assertEqual({}, self.t.available_cargos)
        actual = self.t.drive_best_cargo_offer()
        expected = "There are no offers available."
        self.assertEqual(expected, actual)

    def test_activities_eat(self):
        self.t.earned_money = 1000
        for x in range(1, 1000 + 1):
            self.t.eat(x)
        self.assertEqual(920, self.t.earned_money)

    def test_activities_sleep(self):
        self.t.earned_money = 1000
        for x in range(1, 10000 + 1):
            self.t.sleep(x)
        self.assertEqual(550, self.t.earned_money)

    def test_activities_pump_gas(self):
        self.t.earned_money = 10000
        for x in range(1, 15000 + 1):
            self.t.pump_gas(x)
        self.assertEqual(5000, self.t.earned_money)

    def test_activities_repair_truck(self):
        self.t.earned_money = 20000
        for x in range(1, 20000 + 1):
            self.t.repair_truck(x)
        self.assertEqual(5000, self.t.earned_money)

    def test_combined_activities(self):
        self.t.earned_money = 20000
        self.t.check_for_activities(10000)
        self.assertEqual(8250, self.t.earned_money)

    def test_repr(self):
        self.t.add_cargo_offer('Varna', 1000)
        expected = "Ivan has 1000 miles behind his back."
        self.t.drive_best_cargo_offer()
        self.assertEqual(expected, self.t.__repr__())


if __name__ == '__main__':
    unittest.main()
