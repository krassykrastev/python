from unittest import TestCase, main

from project.survivor import Survivor


class TestSurvivor(TestCase):
    def setUp(self) -> None:
        self.survivor = Survivor('George', 25)

    def test_init_attrs_set_correctly(self):
        self.assertEqual('George', self.survivor.name)
        self.assertEqual(25, self.survivor.age)
        self.assertEqual(100, self.survivor.needs)
        self.assertEqual(100, self.survivor.health)

    def test_name__when_not_value__expect__value_error(self):
        with self.assertRaises(ValueError) as er:
            Survivor('', 25)
        self.assertEqual("Name not valid!", str(er.exception))

    def test_age__when_value_below_0__expect__value_error(self):
        with self.assertRaises(ValueError) as er:
            Survivor('George', -1)
        self.assertEqual("Age not valid!", str(er.exception))

    def test_health__when_value_below_0__expect__value_error(self):
        with self.assertRaises(ValueError) as er:
            self.survivor.health = -1
        self.assertEqual("Health not valid!", str(er.exception))

    def test_needs__when_value_below_0__expect__value_error(self):
        with self.assertRaises(ValueError) as er:
            self.survivor.needs = -1
        self.assertEqual("Needs not valid!", str(er.exception))

    def test_needs_healing__when_below_100__expect_true(self):
        self.survivor.health = 99
        self.assertEqual(True, self.survivor.needs_healing)

    def test_needs_healing__when_above_100__expect_false(self):
        self.survivor.health = 101
        self.assertEqual(False, self.survivor.needs_healing)

    def test_needs_sustenance__when_above_100__expect_false(self):
        self.survivor.needs = 101
        self.assertEqual(False, self.survivor.needs_sustenance)

    def test_needs_sustenance__when_below_100__expect_true(self):
        self.survivor.needs = 99
        self.assertEqual(True, self.survivor.needs_sustenance)



if __name__ == '__main__':
    main()