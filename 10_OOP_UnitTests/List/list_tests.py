import unittest

from extended_list import IntegerList


class TestList(unittest.TestCase):
    def test_if_list_obj_initialized_correctly_without_data(self):
        ll = IntegerList()
        self.assertEqual([], ll._IntegerList__data)

    def test_if_list_obj_initialized_correctly_with_wrong_data(self):
        ll = IntegerList('abs', 4.4, 4.3)
        self.assertEqual([], ll._IntegerList__data)

    def test_if_list_obj_initialized_correctly_with_correct_data(self):
        ll = IntegerList(5, 'asd')
        self.assertEqual([5], ll._IntegerList__data)

    def test_if_get_data_method_returns_correct_data(self):
        ll = IntegerList(5, 'asd')
        expected_result = ll.get_data()
        self.assertEqual([5], expected_result)

    def test_if_add_method_raises_with_incorrect_data(self):
        ll = IntegerList(5)
        with self.assertRaises(ValueError) as err:
            ll.add("5")
        self.assertEqual("Element is not Integer", str(err.exception))

    def test_add_correct_data_adds_element(self):
        ll = IntegerList(5)
        ll.add(10)
        self.assertEqual([5, 10], ll._IntegerList__data)

    def test_remove_index_method_raises_err_if_index_bigger(self):
        ll = IntegerList(4)
        with self.assertRaises(IndexError) as err:
            ll.remove_index(2)
        self.assertEqual("Index is out of range", str(err.exception))

    def test_remove_index_method_removes_data_by_correct_index(self):
        ll = IntegerList(5, 6, 7)
        result = ll.remove_index(1)
        self.assertEqual(result, 6)
        self.assertEqual([5, 7], ll.get_data())

    def test_get_method_raises_err_if_idx_out_of_range(self):
        ll = IntegerList(5, 6)
        with self.assertRaises(IndexError) as err:
            ll.get(2)
        self.assertEqual("Index is out of range", str(err.exception))

    def test_get_method_returns_correct_data(self):
        ll = IntegerList(5, 6)
        result = ll.get(1)
        self.assertEqual(result, 6)

    def test_insert_method_raises_if_idx_out_of_range(self):
        ll = IntegerList(5, 6)
        with self.assertRaises(IndexError) as err:
            ll.insert(3, 4)
        self.assertEqual("Index is out of range", str(err.exception))

    def test_insert_method_raises_if_element_not_correct(self):
        ll = IntegerList(3, 4)
        with self.assertRaises(ValueError) as err:
            ll.insert(0, 'not correct')
        self.assertEqual("Element is not Integer", str(err.exception))

    def test_insert_method_with_correct_data(self):
        ll = IntegerList(3, 4)
        ll.insert(0, 1)
        self.assertEqual([1, 3, 4], ll.get_data())

    def test_get_biggest_method_returns_correct_integer(self):
        ll = IntegerList(1, 10, 2, 3, 4)
        result = ll.get_biggest()
        self.assertEqual(10, result)

    def test_get_index_method_returns_correct_index(self):
        ll = IntegerList(1, 2, 3, 4)
        result = ll.get_index(2)
        self.assertEqual(1, result)


if __name__ == '__main__':
    unittest.main()
