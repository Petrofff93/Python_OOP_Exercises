import unittest

# from project.cat import Cat


class CatTests(unittest.TestCase):
    def test_if_cat_obj_initialized_correctly(self):
        cat = Cat('Tom')
        self.assertEqual('Tom', cat.name)
        self.assertEqual(cat.fed, False)
        self.assertEqual(cat.sleepy, False)
        self.assertEqual(cat.size, 0)

    def test_if_cat_size_increases_after_eating_method_is_called(self):
        cat = Cat('Tom')
        self.assertEqual(0, cat.size)
        cat.eat()
        expected_result = 1
        actual_result = cat.size
        self.assertEqual(expected_result, actual_result)

    def test_if_cat_is_fed_after_eating_method_is_called(self):
        cat = Cat('Tom')
        self.assertFalse(cat.fed)
        cat.eat()
        expected_result = True
        actual_result = cat.fed
        self.assertEqual(expected_result, actual_result)

    def test_if_cat_can_eat_while_it_is_already_fed(self):
        cat = Cat('Tom')
        cat.fed = True

        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual(str(ex.exception), 'Already fed.')

    def test_if_cat_is_sleepy_after_eating_method_is_called(self):
        cat = Cat('Tom')
        self.assertFalse(cat.sleepy)
        cat.eat()
        expected_result = True
        actual_result = cat.sleepy
        self.assertEqual(expected_result, actual_result)

    def test_if_cat_can_sleep_if_not_fed(self):
        cat = Cat('Tom')

        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')

    def test_cat_is_not_sleepy_after_sleeping(self):
        cat = Cat('Tom')
        cat.sleepy = True
        cat.fed = True
        cat.sleep()
        expected_result = False
        actual_result = cat.sleepy
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
