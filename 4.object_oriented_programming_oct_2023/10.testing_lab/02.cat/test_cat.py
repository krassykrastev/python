# Create a class CatTests
# * In Judge, you need to submit just the CatTests class, with the unittest module imported and the main block.
# Create the following tests:
# •	The cat's size is increased after eating
# •	Cat is fed after eating
# •	Cat cannot eat if already fed, raises an error
# •	Cat cannot fall asleep if not fed, raises an error
# •	Cat is not sleepy after sleeping

from unittest import TestCase, main
from cat import Cat


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat('TestCat')

    def test_feed_cat_expect_fed_and_sleepy_cat_with_increased_size(self):
        expected_result = 1
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_result, self.cat.size)

    def test_feed_cat_when_cat_is_fed_raises_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleeping_cat_when_cat_is_fed_makes_cat_not_sleepy(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

    def test_sleeping_cat_when_cat_is_hungry_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == '__main__':
    main()
