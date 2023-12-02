from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):

    def test_init(self):
        car = SecondHandCar('TestModel', 'Test', 100000, 20000)
        self.assertEqual(car.model, 'TestModel')
        self.assertEqual(car.car_type, 'Test')
        self.assertEqual(car.mileage, 100000)
        self.assertEqual(car.price, 20000)
        self.assertEqual(car.repairs, [])

    def test_price_less_than_1_or_equal_raises(self):
        with self.assertRaises(ValueError) as ex:
            car = SecondHandCar('TestModel', 'Test', 100000, 1)
        self.assertEqual(str(ex.exception), 'Price should be greater than 1.0!')

        with self.assertRaises(ValueError) as ex:
            car = SecondHandCar('TestModel', 'Test', 100000, 0.9)
        self.assertEqual(str(ex.exception), 'Price should be greater than 1.0!')

    def test_mileage_less_than_100_or_equal_raises(self):
        with self.assertRaises(ValueError) as ex:
            car = SecondHandCar('TestModel', 'Test', 100, 20000)
        self.assertEqual(str(ex.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

        with self.assertRaises(ValueError) as ex:
            car = SecondHandCar('TestModel', 'Test', 99, 20000)
        self.assertEqual(str(ex.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_promotional_price_higher_than_current_raises(self):
        car = SecondHandCar('TestModel', 'Test', 100000, 20000)
        with self.assertRaises(ValueError) as ex:
            car.set_promotional_price(20000)
        self.assertEqual(str(ex.exception), 'You are supposed to decrease the price!')

        with self.assertRaises(ValueError) as ex:
            car.set_promotional_price(20001)
        self.assertEqual(str(ex.exception), 'You are supposed to decrease the price!')

    def test_set_promotional_price(self):
        car = SecondHandCar('TestModel', 'Test', 100000, 20000)
        self.assertEqual(car.price, 20000)
        result = car.set_promotional_price(10000)
        self.assertEqual(car.price, 10000)
        self.assertEqual(result, 'The promotional price has been successfully set.')

    def test_repair_price_too_high_raises(self):
        car = SecondHandCar('TestModel', 'Test', 100000, 20000)
        self.assertEqual(car.price, 20000)
        self.assertEqual(car.repairs, [])
        half_price = car.price / 2
        result = car.need_repair(half_price + 1, 'Test repair')
        self.assertEqual(result, "Repair is impossible!")
        self.assertEqual(car.price, 20000)
        self.assertEqual(car.repairs, [])

    def test_repair_exact_half_price(self):
        car = SecondHandCar('TestModel', 'Test', 100000, 20000)
        self.assertEqual(car.price, 20000)
        self.assertEqual(car.repairs, [])
        half_price = car.price / 2
        current_price = car.price
        result = car.need_repair(half_price, 'Test repair')
        self.assertEqual(result, "Price has been increased due to repair charges.")
        self.assertEqual(car.price, current_price + half_price)
        self.assertEqual(car.repairs, ['Test repair'])

    def test_repair_less_than_half_price(self):
        car = SecondHandCar('TestModel', 'Test', 100000, 20000)
        self.assertEqual(car.price, 20000)
        self.assertEqual(car.repairs, [])
        half_price = (car.price / 2) - 1
        current_price = car.price
        result = car.need_repair(half_price, 'Test repair')
        self.assertEqual(result, "Price has been increased due to repair charges.")
        self.assertEqual(car.price, current_price + half_price)
        self.assertEqual(car.repairs, ['Test repair'])

    def test_compare_different_types_impossible(self):
        car = SecondHandCar('TestModel', 'Test', 100000, 20000)
        car2 = SecondHandCar('TestModel2', 'Test2', 100000, 20000)
        result = car2 > car
        self.assertEqual(result, 'Cars cannot be compared. Type mismatch!')

    def test_compare(self):
        car = SecondHandCar('TestModel', 'Test', 100000, 20000)
        car2 = SecondHandCar('TestModel2', car.car_type, 100000, 9000)
        result = car2 > car
        self.assertFalse(result)

    def test_str(self):
        car = SecondHandCar('TestModel', 'Test', 100000, 20000)
        result = str(car)
        self.assertEqual(result, "Model TestModel | Type Test | Milage 100000km\nCurrent price: 20000.00 | Number of Repairs: 0")
    

if __name__ == '__main__':
    main()
