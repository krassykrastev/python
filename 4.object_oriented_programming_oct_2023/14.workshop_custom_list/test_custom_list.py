from unittest import TestCase, main
from custom_list import CustomList


class CustomListTests(TestCase):
    def setUp(self):
        self.cl = CustomList(5, "asd", 3.6)

    def test_init(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__values)
        cl = CustomList(5, "asd", 3.6)
        self.assertEqual([5, "asd", 3.6], cl._CustomList__values)

    def test_append_no_argument_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.cl.append()
        self.assertIn("missing 1 required positional argument", str(ex.exception))

    def test_append_adds_element_to_the_end(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.append(100)
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual([5, "asd", 3.6, 100], self.cl._CustomList__values)
        self.assertEqual(self.cl._CustomList__values[-1], 100)
        self.assertEqual(self.cl._CustomList__values, result)

    def test_append_element_to_empty_list(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__values)
        cl.append(5)
        self.assertEqual([5], cl._CustomList__values)

    def test_invalid_index_type_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cl.remove("asd")
        self.assertIn("Invalid index type. You must pass an integer", str(ex.exception))

    def test_remove_invalid_index_raises(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        with self.assertRaises(IndexError) as ex:
            self.cl.remove(3)
        self.assertEqual("Invalid index", str(ex.exception))
        with self.assertRaises(IndexError) as ex:
            self.cl.remove(-4)
        self.assertEqual("Invalid index", str(ex.exception))
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)

    def test_remove_multiple_same_elements_are_not_removed(self):
        self.cl.append("asd")
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual([5, "asd", 3.6, "asd"], self.cl._CustomList__values)
        result = self.cl.remove(1)
        self.assertEqual(result, "asd")
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, 3.6, "asd"], self.cl._CustomList__values)

    def test_remove_returns_element(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.remove(1)
        self.assertEqual(result, "asd")
        self.assertEqual(len(self.cl._CustomList__values), 2)
        self.assertEqual([5, 3.6], self.cl._CustomList__values)

    def test_remove_minus_index_returns_element(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.remove(-1)
        self.assertEqual(result, 3.6)
        self.assertEqual(len(self.cl._CustomList__values), 2)
        self.assertEqual([5, "asd"], self.cl._CustomList__values)

    def test_save_remove_invalid_index_type_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cl.save_remove("asd")
        self.assertIn("Invalid index type. You must pass an integer", str(ex.exception))

    def test_save_remove_minus_index_returns_element(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.save_remove(-1)
        self.assertEqual(result, 3.6)
        self.assertEqual(len(self.cl._CustomList__values), 2)
        self.assertEqual([5, "asd"], self.cl._CustomList__values)
    def test_save_remove_invalid_index_returns_none(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.save_remove(12)
        self.assertIsNone(result)

    def test_get_invalid_index_type_raises(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        with self.assertRaises(ValueError) as ex:
            self.cl.remove("asd")
        self.assertIn("Invalid index type. You must pass an integer", str(ex.exception))
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)

    def test_get_invalid_index_returns_none(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.get(12)
        self.assertIsNone(result)

    def test_get(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.get(1)
        self.assertEqual("asd", result)

    def test_get_optional_invalid_index_returns_optional_arg(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.get(11, "Test")
        self.assertEqual("Test", result)
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)

    def test_extend(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.extend(1, 2, 3)
        self.assertEqual(len(self.cl._CustomList__values), 6)
        self.assertEqual([5, "asd", 3.6, 1, 2, 3], self.cl._CustomList__values)
        self.assertEqual(self.cl._CustomList__values, result)

    def test_extend_with_iterable(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.extend([1, 1], 2, 3)
        self.assertEqual(len(self.cl._CustomList__values), 7)
        self.assertEqual([5, "asd", 3.6, 1, 1, 2, 3], self.cl._CustomList__values)
        self.assertEqual(self.cl._CustomList__values, result)

    def test_insert_invalid_index_type_raises(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        with self.assertRaises(ValueError) as ex:
            self.cl.insert("asd", "a")
        self.assertIn("Invalid index type. You must pass an integer", str(ex.exception))
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)

    def test_invalid_index_appends_the_value(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.insert(4, "a")
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual([5, "asd", 3.6, "a"], self.cl._CustomList__values)

    def test_insert(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.insert(0, 100)
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual([100, 5, "asd", 3.6], self.cl._CustomList__values)
        self.assertEqual(self.cl._CustomList__values, result)

        result = self.cl.insert(2, 90)
        self.assertEqual(len(self.cl._CustomList__values), 5)
        self.assertEqual([100, 5, 90, "asd", 3.6], self.cl._CustomList__values)
        self.assertEqual(self.cl._CustomList__values, result)

    def test_pop_empty_list_raises(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__values)
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        with self.assertRaises(IndexError) as ex:
            cl.pop()
        self.assertIn("empty list", str(ex.exception))
        self.assertEqual([], cl._CustomList__values)

    def test_pop_returns_element(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.pop()
        self.assertEqual(result, 3.6)
        self.assertEqual(len(self.cl._CustomList__values), 2)
        self.assertEqual([5, "asd"], self.cl._CustomList__values)

    def test_clear(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.clear()
        self.assertIsNone(result)
        self.assertEqual(len(self.cl._CustomList__values), 0)
        self.assertEqual([], self.cl._CustomList__values)

    def test_index_invalid_element_raises(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        with self.assertRaises(Exception) as ex:
            self.cl.index(55)
        self.assertIn("not in list", str(ex.exception))

    def test_returns_value(self):
        self.cl.append("asd")
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual([5, "asd", 3.6, "asd"], self.cl._CustomList__values)
        result = self.cl.index("asd")
        self.assertEqual(result, 1)
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual([5, "asd", 3.6, "asd"], self.cl._CustomList__values)

    def test_count(self):
        self.cl.append("asd")
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual([5, "asd", 3.6, "asd"], self.cl._CustomList__values)
        result = self.cl.count(6)
        self.assertEqual(result, 0)
        result = self.cl.count(5)
        self.assertEqual(result, 1)
        result = self.cl.count("asd")
        self.assertEqual(result, 2)

    def test_reverse_returns_reversed_list_values_list_remains_unchanged(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.reverse()
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        self.assertEqual([3.6, "asd", 5], result)

    def test_copy_returns_copy_of_the_list(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.copy()
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        self.assertNotEqual(id(self.cl._CustomList__values), id(result))
        self.assertEqual([5, "asd", 3.6], result)

    def test_copy_nested_structures_are_copies_not_references(self):
        self.cl.append([1, 2, 3])
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual([5, "asd", 3.6, [1, 2, 3]], self.cl._CustomList__values)
        result = self.cl.copy()
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual([5, "asd", 3.6, [1, 2, 3]], self.cl._CustomList__values)
        self.assertNotEqual(id(self.cl._CustomList__values), id(result))
        self.assertEqual([5, "asd", 3.6, [1, 2, 3]], result)

        last_ref_element = self.cl._CustomList__values[-1]
        self.assertEqual(last_ref_element, [1, 2, 3])
        self.assertNotEqual(id(last_ref_element), id(result[-1]))

    def test_size(self):
        cl = CustomList()
        self.assertEqual(0, len(cl._CustomList__values))
        result = cl.size()
        self.assertEqual(0, result)
        self.assertEqual(3, len(self.cl._CustomList__values))
        result = self.cl.size()
        self.assertEqual(3, result)

    def test_add_first(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.add_first(100)
        self.assertIsNone(result)
        self.assertEqual(len(self.cl._CustomList__values), 4)
        self.assertEqual([100, 5, "asd", 3.6], self.cl._CustomList__values)
        cl = CustomList()
        self.assertEqual(len(cl._CustomList__values), 0)
        result = cl.add_first(100)
        self.assertEqual([100], cl._CustomList__values)

    def test_dictionize(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.dictionize()
        self.assertEqual(result, {5: "asd", 3.6: " "})
        self.cl.append(100)
        result = self.cl.dictionize()
        self.assertEqual(result, {5: "asd", 3.6: 100})

    def test_move(self):
        self.cl.append(100)
        self.assertEqual([5, "asd", 3.6, 100], self.cl._CustomList__values)
        result = self.cl.move(2)
        self.assertEqual([3.6, 100, 5, "asd"], self.cl._CustomList__values)
        self.assertEqual(result, [3.6, 100, 5, "asd"])

    def test_move_larger_amount_than_the_list(self):
        self.cl.append(100)
        self.assertEqual([5, "asd", 3.6, 100], self.cl._CustomList__values)
        result = self.cl.move(5)
        self.assertEqual([5, "asd", 3.6, 100], self.cl._CustomList__values)
        self.assertEqual(result, [5, "asd", 3.6, 100])

    def test_invalid_amount_type(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        with self.assertRaises(ValueError) as ex:
            self.cl.move("asd")
        self.assertIn("Invalid index type", str(ex.exception))

    def test_sum(self):
        self.assertEqual(len(self.cl._CustomList__values), 3)
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.sum()
        self.assertEqual(11.6, result)

    def test_overbound(self):
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.overbound()
        self.assertEqual(0, result)
        self.cl.append("123456")
        self.assertEqual([5, "asd", 3.6, "123456"], self.cl._CustomList__values)
        result = self.cl.overbound()
        self.assertEqual(3, result)

    def test_underbound(self):
        self.assertEqual([5, "asd", 3.6], self.cl._CustomList__values)
        result = self.cl.underbound()
        self.assertEqual(1, result)
        self.cl.append("a")
        self.assertEqual([5, "asd", 3.6, "a"], self.cl._CustomList__values)
        result = self.cl.underbound()
        self.assertEqual(3, result)


if __name__ == '__main__':
    main()
