import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(10, 200)

    def test_vehicle_obj_initialized_correct(self):
        self.assertEqual(10, self.vehicle.fuel)
        self.assertEqual(10, self.vehicle.capacity)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_method_raises_if_fuel_not_enough(self):
        with self.assertRaises(Exception) as err:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(err.exception))

    def test_drive_method_reduces_fuel_when_correctly_ran(self):
        current_fuel = self.vehicle.fuel
        self.vehicle.drive(4)
        self.assertEqual(current_fuel - (4 * 1.25), self.vehicle.fuel)

    def test_refuel_method_raises_when_too_much_fuel_added(self):
        with self.assertRaises(Exception) as err:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(err.exception))

    def test_refuel_method_adds_fuel_when_correct(self):
        self.vehicle.fuel -= 5
        self.assertEqual(5, self.vehicle.fuel)

        self.vehicle.refuel(5)
        self.assertEqual(10, self.vehicle.fuel)

    def test_str_method_returns_correct_string(self):
        actual_result = str(self.vehicle)
        expected_result = "The vehicle has 200 horse power with 10 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
