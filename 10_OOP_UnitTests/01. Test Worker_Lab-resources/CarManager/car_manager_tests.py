import unittest

# from car_manager import Car


class TestCarManager(unittest.TestCase):
    def setUp(self):
        self.test_car = Car("Opel", "Astra", 1, 4)

    def test_if_car_obj_initialized_with_correct_data(self):

        self.assertEqual("Opel", self.test_car.make)
        self.assertEqual("Astra", self.test_car.model)
        self.assertEqual(1, self.test_car.fuel_consumption)
        self.assertEqual(4, self.test_car.fuel_capacity)

    def test_if_car_obj_raises_when_initialized_with_empty_car_make(self):
        with self.assertRaises(Exception) as err:
            self.test_car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(err.exception))

    def test_if_car_obj_raises_when_initialized_with_empty_car_model(self):
        with self.assertRaises(Exception) as err:
            self.test_car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(err.exception))

    def test_if_car_obj_raises_when_initialized_with_zero_fuel_consumption(self):
        with self.assertRaises(Exception) as err:
            self.test_car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(err.exception))

    def test_if_car_obj_raises_when_initialized_with_zero_fuel_capacity(self):
        with self.assertRaises(Exception) as err:
            self.test_car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(err.exception))

    def test_if_car_obj_can_receive_negative_fuel_amount(self):
        with self.assertRaises(Exception) as err:
            self.test_car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(err.exception))

    def test_car_obj_fuel_amount_updates_correctly(self):
        self.test_car.fuel_amount = 5
        self.assertEqual(5, self.test_car.fuel_amount)

    def test_refuel_method_raises_when_fuel_is_negative_or_zero(self):
        with self.assertRaises(Exception) as err:
            self.test_car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(err.exception))

    def test_refuel_method_adds_qty_to_fuel_amount(self):
        self.test_car.refuel(2)
        self.assertEqual(2, self.test_car.fuel_amount)

    def test_refuel_method_adds_equal_to_fuel_capa_when_amount_is_bigger(self):
        self.test_car.refuel(5)
        self.assertEqual(4, self.test_car.fuel_amount)

    def test_drive_method_raises_when_not_enough_fuel_to_drive(self):
        with self.assertRaises(Exception) as err:
            self.test_car.drive(600)
        self.assertEqual("You don't have enough fuel to drive!", str(err.exception))

    def test_drive_method_reduces_fuel_amount_when_correct(self):
        self.test_car.fuel_amount = 5
        self.test_car.drive(100)
        self.assertEqual(4, self.test_car.fuel_amount)


if __name__ == '__main__':
    unittest.main()
