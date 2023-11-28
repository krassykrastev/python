from unittest import TestCase, main
from project.hero import Hero


class HeroTest(TestCase):
    username = "Test hero"
    level = 5
    health = 25.6
    damage = 10.2

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)

    def test_enemy_same_username(self):
        enemy = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_health_less_than_zero(self):
        self.hero.health = 0
        enemy = Hero("Enemy", self.level, self.health, self.damage)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        self.hero.health = - 1
        with self.assertRaises(ValueError) as ex1:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex1.exception))

    def test_enemy_health_less_than_zero(self):
        enemy = Hero("Enemy", self.level, self.health, self.damage)
        enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight Enemy. He needs to rest", str(ex.exception))

        enemy.health = -1
        with self.assertRaises(ValueError) as ex1:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight Enemy. He needs to rest", str(ex1.exception))

    def test_draw(self):
        enemy = Hero("Enemy", self.level, self.health, self.damage)
        enemy.health = self.health
        result = self.hero.battle(enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(-25.4, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_hero_wins(self):
        enemy = Hero("Enemy", 1, 1, 1)
        result = self.hero.battle(enemy)
        self.assertEqual("You win", result)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(29.6, self.hero.health)
        self.assertEqual(15.2, self.hero.damage)

    def test_hero_loses(self):
        enemy = Hero("Enemy", 100, 100, 100)
        result = self.hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(101, enemy.level)
        self.assertEqual(54, enemy.health)
        self.assertEqual(105, enemy.damage)

    def test_str(self):
        result = str(self.hero)
        expected = f"Hero {self.username}: {self.level} lvl\nHealth: {self.health}\nDamage: {self.damage}\n"
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
