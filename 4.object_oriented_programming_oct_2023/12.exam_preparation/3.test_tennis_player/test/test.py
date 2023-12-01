from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class Tests(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("Boris", 18, 450.5)
        self.other = TennisPlayer("Martin", 20, 450)

    def test_01_init(self):
        self.assertEqual("Boris", self.player.name)
        self.assertEqual(18, self.player.age)
        self.assertEqual(450.5, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_02_invalid_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.player.name = "Bo"

        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))
        self.assertEqual("Boris", self.player.name)

    def test_03_invalid_age_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))
        self.assertEqual(18, self.player.age)

    def test_03_add_new_win_if_already_exists(self):
        self.player.wins = ["Wimbledon"]

        result = self.player.add_new_win("Wimbledon")
        expected_result = "Wimbledon has been already added to the list of wins!"

        self.assertEqual(expected_result, result)
        self.assertEqual(["Wimbledon"], self.player.wins)

    def test_04_add_new_win_success(self):
        self.player.add_new_win("Wimbledon")
        self.assertEqual(["Wimbledon"], self.player.wins)

        self.player.add_new_win("Australian Open")
        self.assertEqual(["Wimbledon", "Australian Open"], self.player.wins)

    def test_05_lt_method_returns_false(self):
        result = self.player < self.other
        expected_result = "Boris is a better player than Martin"

        self.assertEqual(expected_result, result)

    def test_06_lt_method_returns_true(self):
        result = self.other < self.player
        expected_result = "Boris is a top seeded player and he/she is better than Martin"

        self.assertEqual(expected_result, result)

    def test_07_str_method(self):
        self.player.add_new_win("Wimbledon")
        self.player.add_new_win("Australian Open")

        expected_result = "Tennis Player: Boris\n" \
                          "Age: 18\n" \
                          "Points: 450.5\n" \
                          "Tournaments won: Wimbledon, Australian Open"

        self.assertEqual(expected_result, str(self.player))


if __name__ == "__main__":
    main()
