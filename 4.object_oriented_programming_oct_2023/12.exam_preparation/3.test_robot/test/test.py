from project.robot import Robot
from unittest import TestCase, main


class Tests(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("1A", "Military", 50, 2500.54)
        self.other = Robot("2A", "Education", 50, 1500.54)

    def test_01_init(self):
        self.assertEqual("1A", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(50, self.robot.available_capacity)
        self.assertEqual(2500.54, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_02_check_valid_categories(self):
        self.robot.category = "Education"
        self.assertEqual("Education", self.robot.category)

        self.robot.category = "Entertainment"
        self.assertEqual("Entertainment", self.robot.category)

        self.robot.category = "Humanoids"
        self.assertEqual("Humanoids", self.robot.category)

    def test_03_invalid_category_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.category = "Music"

        expected_message = "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'"
        self.assertEqual(expected_message, str(ex.exception))

    def test_04_invalid_price_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.price = -1

        expected_message = "Price cannot be negative!"
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual(2500.54, self.robot.price)

        self.robot.price = 0
        self.assertEqual(0, self.robot.price)

    def test_05_upgrade_valid_hardware(self):
        expected_message = "Robot 1A was upgraded with Propeller."
        result = self.robot.upgrade("Propeller", 10)

        self.assertEqual(["Propeller"], self.robot.hardware_upgrades)
        self.assertEqual(2515.54, self.robot.price)
        self.assertEqual(expected_message, result)

        self.robot.upgrade("Cooler", 20)
        self.assertEqual(["Propeller", "Cooler"], self.robot.hardware_upgrades)
        self.assertEqual(2545.54, self.robot.price)

    def test_06_upgrade_invalid_hardware(self):
        self.robot.upgrade("Propeller", 10)
        expected_message = "Robot 1A was not upgraded."
        result = self.robot.upgrade("Propeller", 10)

        self.assertEqual(["Propeller"], self.robot.hardware_upgrades)
        self.assertEqual(2515.54, self.robot.price)
        self.assertEqual(expected_message, result)

    def test_07_update_valid_software(self):
        expected_message = "Robot 1A was updated to version 1."
        result = self.robot.update(1, 25)

        self.assertEqual([1], self.robot.software_updates)
        self.assertEqual(25, self.robot.available_capacity)
        self.assertEqual(expected_message, result)

        expected_message = "Robot 1A was updated to version 3."
        result = self.robot.update(3, 25)

        self.assertEqual([1, 3], self.robot.software_updates)
        self.assertEqual(0, self.robot.available_capacity)
        self.assertEqual(expected_message, result)

    def test_08_update_software_invalid(self):
        expected_message = "Robot 1A was not updated."
        result = self.robot.update(1, 55)

        self.assertEqual([], self.robot.software_updates)
        self.assertEqual(50, self.robot.available_capacity)
        self.assertEqual(expected_message, result)

        self.robot.update(2, 10)
        result = self.robot.update(1, 5)

        self.assertEqual([2], self.robot.software_updates)
        self.assertEqual(40, self.robot.available_capacity)
        self.assertEqual(expected_message, result)

    def test_09_greater_than(self):
        message_greater_than = "Robot with ID 1A is more expensive than Robot with ID 2A."
        result = self.robot > self.other
        self.assertEqual(message_greater_than, result)

        message_less_than = "Robot with ID 2A is cheaper than Robot with ID 1A."
        result = self.other > self.robot
        self.assertEqual(message_less_than, result)

        self.other.price = self.robot.price
        message_equal = "Robot with ID 1A costs equal to Robot with ID 2A."
        result = self.robot > self.other
        self.assertEqual(message_equal, result)


if __name__ == "__main__":
    main()
