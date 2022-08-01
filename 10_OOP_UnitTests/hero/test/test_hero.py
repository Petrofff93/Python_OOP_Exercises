import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Test", 10, 100, 50)

    def test_hero_obj_initialized_correctly(self):
        self.assertEqual("Test", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(50, self.hero.damage)

    def test_battle_method_raises_when_two_heroes_have_equal_name(self):
        enemy = Hero("Test", 99, 100, 50)

        with self.assertRaises(Exception) as err:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(err.exception))

    def test_battle_method_raises_when_health_zero_or_less(self):
        self.hero.health = 0
        enemy = Hero("test2", 44, 44, 44)

        with self.assertRaises(ValueError) as err:
            self.hero.battle(enemy)
        self.assertEqual(
            "Your health is lower than or equal to 0. You need to rest",
            str(err.exception),
        )

    def test_battle_method_raises_when_enemy_hero_has_zero_or_less_hp(self):
        enemy = Hero("Test2", 44, 0, 44)

        with self.assertRaises(ValueError) as err:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Test2. He needs to rest", str(err.exception))

    def test_battle_methods_return_draw_when_correct(self):
        enemy = Hero("Test2", 10, 100, 50)
        result = self.hero.battle(enemy)
        self.assertEqual("Draw", result)

    def test_battle_method_update_after_hero_wins(self):
        enemy = Hero("Test2", 5, 10, 10)
        expected_level = self.hero.level + 1
        expected_health = self.hero.health + 5 - (enemy.damage * enemy.level)
        expected_dmg = self.hero.damage + 5

        result = self.hero.battle(enemy)

        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_dmg, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_method_when_enemy_wins(self):
        enemy = Hero("Test2", 100, 1000, 100)
        expected_enemy_level = enemy.level + 1
        expected_enemy_health = enemy.health + 5 - (self.hero.damage * self.hero.level)
        expected_enemy_dmg = enemy.damage + 5

        result = self.hero.battle(enemy)

        self.assertEqual(expected_enemy_level, enemy.level)
        self.assertEqual(expected_enemy_health, enemy.health)
        self.assertEqual(expected_enemy_dmg, enemy.damage)
        self.assertEqual("You lose", result)

    def test_str_method_returns_correct_data(self):
        actual_result = str(self.hero)
        expected_result = "Hero Test: 10 lvl\n" "Health: 100\n" "Damage: 50\n"
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
