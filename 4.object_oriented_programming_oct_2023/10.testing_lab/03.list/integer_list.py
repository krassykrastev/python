# You are provided with a class IntegerList. It should only store integers. The initial integers should be set by the
# constructor. They are stored as a list. IntegerList has a functionality to add, remove_index, get, insert, get the
# biggest number, and get the index of an element. Your task is to test the class.
# Note: You are not allowed to change the structure of the provided code
# Constraints
# •	add operation, should add an element and return the list.
#   o	If the element is not an integer, a ValueError is thrown
# •	remove_index operation removes the element on that index and returns it.
#   o	If the index is out of range, an IndexError is thrown
# •	__init__ should only take integers, and store them
# •	get should return the specific element
#   o	If the index is out of range, an IndexError is thrown
# •	insert
#   o	If the index is out of range, IndexError is thrown
#   o	If the element is not an integer, ValueError is thrown
# •	get_biggest
# •	get_index
# Hint: Do not forget to test the constructor

from unittest import TestCase, main
from extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.integer_list = IntegerList('50', 1, False, 3.5, 2, 3)

    def test_correct_init(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_operation_adds_integer_to_the_list(self):
        expected_data = self.integer_list.get_data()
        self.integer_list.add(5)
        self.assertEqual(expected_data, self.integer_list.get_data())

    def test_add_operation_with_float_element_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.add(3.5)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index_operation_with_out_of_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(100)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_with_valid_index_removes_element(self):
        expected_element = [1, 3]
        deleted_element = 2
        actual_deleted_element = self.integer_list.remove_index(1)
        self.assertEqual(expected_element, self.integer_list.get_data())
        self.assertEqual(deleted_element, actual_deleted_element)

    def test_get_with_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(100)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_with_valid_index_returns_element(self):
        expected_element = 2
        actual_element = self.integer_list.get(1)
        self.assertEqual(expected_element, actual_element)

    def test_insert_integer_on_valid_index_expected_inserted_element(self):
        expected_data = [1, 2, 4, 3]
        self.integer_list.insert(len(self.integer_list.get_data()) - 1, 4)
        self.assertEqual(expected_data, self.integer_list.get_data())

    def test_insert_element_with_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(100, 5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_float_element_on_valid_index_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(0, 5.5)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest_expect_success(self):
        expected_element = 3
        actual_element = self.integer_list.get_biggest()
        self.assertEqual(expected_element, actual_element)

    def test_get_index_expect_success(self):
        expected_element = 1
        actual_element = self.integer_list.get_index(2)
        self.assertEqual(expected_element, actual_element)


if __name__ == '__main__':
    main()