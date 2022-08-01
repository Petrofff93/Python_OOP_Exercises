import unittest

# from project.worker import Worker


class WorkerTests(unittest.TestCase):
    def test_if_worker_is_initialized_correctly(self):
        worker_name = 'Test'
        worker_salary = 200
        worker_energy = 100
        worker = Worker(worker_name, worker_salary, worker_energy)

        self.assertEqual('Test', worker.name)
        self.assertEqual(200, worker.salary)
        self.assertEqual(100, worker.energy)

    def test_if_worker_work_method_raises_exception_when_no_energy(self):
        worker_name = 'Test'
        worker_salary = 200
        worker_energy = 0
        worker = Worker(worker_name, worker_salary, worker_energy)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual(str(ex.exception), 'Not enough energy.')

    def test_if_worker_work_method_increase_salary_reduce_energy(self):
        worker_name = 'Test'
        worker_salary = 200
        worker_energy = 100
        worker = Worker(worker_name, worker_salary, worker_energy)

        worker.work()
        expected_result = 0 + worker.salary
        actual_result = worker.money
        self.assertEqual(expected_result, actual_result)

        expected_result = worker_energy - 1
        actual_result = worker.energy
        self.assertEqual(expected_result, actual_result)

    def test_if_workers_energy_is_incremented_after_rest_method(self):
        worker_name = 'Test'
        worker_salary = 200
        worker_energy = 100
        worker = Worker(worker_name, worker_salary, worker_energy)

        worker.rest()
        expected_result = worker_energy + 1
        actual_result = worker.energy
        self.assertEqual(expected_result, actual_result)

    def test_if_get_info_method_returns_proper_data(self):
        worker_name = 'Test'
        worker_salary = 200
        worker_energy = 100
        worker = Worker(worker_name, worker_salary, worker_energy)

        expected_result = 'Test has saved 0 money.'
        actual_result = worker.get_info()
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
