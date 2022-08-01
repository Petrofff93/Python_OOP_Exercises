import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Test', 'Bear', 'Roar')

    def test_mammal_initialized_correctly(self):
        self.assertEqual('Test', self.mammal.name)
        self.assertEqual('Bear', self.mammal.type)
        self.assertEqual('Roar', self.mammal.sound)

    def test_mammal_make_sound_method_returns_correct_data(self):
        result = 'Test makes Roar'
        self.assertEqual(result, self.mammal.make_sound())

    def test_get_kingdom_method_returns_correct_private_attribute(self):
        result = "animals"
        self.assertEqual(result, self.mammal.get_kingdom())

    def test_info_method_returns_correct_data(self):
        result = 'Test is of type Bear'
        self.assertEqual(result, self.mammal.info())


if __name__ == '__main__':
    unittest.main()
