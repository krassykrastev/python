# Create a class WorkerTests
# * In Judge, you need to submit just the WorkerTests class, with the unittest module imported and the main block.
# Create the following tests:
# •	Test if the worker is initialized with the correct name, salary, and energy
# •	Test if the worker's energy is incremented after the rest method is called
# •	Test if an error is raised if the worker tries to work with negative energy or equal to 0
# •	Test if the worker's money is increased by his salary correctly after the work method is called
# •	Test if the worker's energy is decreased after the work method is called
# •	Test if the get_info method returns the proper string with the correct values
from unittest import TestCase, main
from worker import Worker


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker('TestGuy', 25000, 100)

    def test_correct_initialization(self):
        self.assertEqual('TestGuy', self.worker.name)
        self.assertEqual(25000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_when_worker_has_energy_expect_money_increase_and_energy_decrease(self):
        expected_energy = self.worker.energy - 1
        expected_money = self.worker.salary
        self.worker.work()
        self.assertEqual(expected_energy, self.worker.energy)
        self.assertEqual(expected_money, self.worker.money)

    def test_work_when_worker_does_not_have_energy_raises_exception(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_increment_energy_with_one_when_resting(self):
        expected_energy = self.worker.energy + 1
        self.worker.rest()
        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_returns_valid_string(self):
        expected_info = f'{self.worker.name} has saved {self.worker.money} money.'
        self.assertEqual(expected_info, self.worker.get_info())


if __name__ == '__main__':
    main()
