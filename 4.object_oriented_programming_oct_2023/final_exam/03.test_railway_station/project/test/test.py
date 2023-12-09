from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.station = RailwayStation("Central Station")

    def test_init_sets_correct_attributes(self):
        self.assertEqual(self.station.name, "Central Station")
        self.assertEqual(len(self.station.arrival_trains), 0)
        self.assertEqual(len(self.station.departure_trains), 0)

    def test_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "St"
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board_adds_train_to_arrival_queue(self):
        self.station.new_arrival_on_board("Train 1")
        self.assertEqual(self.station.arrival_trains[0], "Train 1")

    def test_train_has_arrived_moves_train_to_departure_queue(self):
        self.station.new_arrival_on_board("Train 1")
        self.station.train_has_arrived("Train 1")
        self.assertEqual(self.station.departure_trains[0], "Train 1")

    def test_train_has_arrived_returns_correct_message(self):
        self.station.new_arrival_on_board("Train 1")
        message = self.station.train_has_arrived("Train 1")
        self.assertEqual(message, "Train 1 is on the platform and will leave in 5 minutes.")

    def test_train_has_arrived_with_wrong_train_returns_correct_message(self):
        self.station.new_arrival_on_board("Train 1")
        message = self.station.train_has_arrived("Train 2")
        self.assertEqual(message, "There are other trains to arrive before Train 2.")

    def test_train_has_left_removes_train_from_departure_queue(self):
        self.station.new_arrival_on_board("Train 1")
        self.station.train_has_arrived("Train 1")
        self.station.train_has_left("Train 1")
        self.assertEqual(len(self.station.departure_trains), 0)

    def test_train_has_left_returns_correct_value(self):
        self.station.new_arrival_on_board("Train 1")
        self.station.train_has_arrived("Train 1")
        result = self.station.train_has_left("Train 1")
        self.assertTrue(result)

    def test_train_has_left_with_wrong_train_returns_correct_value(self):
        self.station.new_arrival_on_board("Train 1")
        self.station.train_has_arrived("Train 1")
        result = self.station.train_has_left("Train 2")
        self.assertFalse(result)

    def test_name_setter_raises_error_for_short_name(self):
        with self.assertRaises(ValueError):
            self.station.name = "St"

    def test_name_setter_sets_name_for_valid_input(self):
        self.station.name = "New Station"
        self.assertEqual(self.station.name, "New Station")


if __name__ == '__main__':
    main()
