from project.plantation import Plantation
from unittest import TestCase, main

class PlantationTests(TestCase):
    def test_init(self):
        plantation = Plantation(10)
        self.assertEqual(10, plantation.size)
        self.assertEqual({}, plantation.plants)
        self.assertEqual([], plantation.workers)

    def test_size_setter(self):
        with self.assertRaises(ValueError) as ex:
            plantation = Plantation(-1)
        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_worker_with_existing_worker_if_raises(self):
        plantation = Plantation(10)
        plantation.workers = ['nurko']
        with self.assertRaises(ValueError) as ex:
            plantation.hire_worker('nurko')
        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_worker_with_no_existing_worker_if_works(self):
        plantation = Plantation(10)
        plantation.workers = ['nurko']
        result = plantation.hire_worker('nurko2')
        self.assertEqual(['nurko', 'nurko2'], plantation.workers)
        self.assertEqual(f"nurko2 successfully hired.", result)

    def test_len_method_if_works_properly(self):
        plantation = Plantation(10)
        plantation.plants = {'aa': ['bb', 'cc'], 'ee': ['rr', 'gg']}
        result = plantation.__len__()
        self.assertEqual(4, result)

    def test_plantation_method_with_no_existing_worker_if_raises(self):
        plantation = Plantation(10)
        with self.assertRaises(ValueError) as ex:
            plantation.planting('nurko', 'lipa')
        self.assertEqual(f"Worker with name nurko is not hired!", str(ex.exception))

    def test_plantation_method_with_more_length_if_raises(self):
        plantation = Plantation(1)
        plantation.plants = {'aa': ['bb']}
        plantation.workers = ['aa']
        with self.assertRaises(ValueError) as ex:
            plantation.planting('aa', 'lipa')
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_plantation_method_with_old_and_worker(self):
        plantation = Plantation(12)
        plantation.plants = {'nurko': ['bb']}
        plantation.workers = ['nurko', 'nurko2']
        result = plantation.planting('nurko', 'lipa')
        self.assertEqual({'nurko': ['bb', 'lipa']}, plantation.plants)
        self.assertEqual(f"nurko planted lipa.", result)
        result = plantation.planting('nurko2', 'bor')
        self.assertEqual({'nurko': ['bb', 'lipa'], 'nurko2': ['bor']}, plantation.plants)
        self.assertEqual(f"nurko2 planted it's first bor.", result)

    def test_if_str_method_returns_correctly(self):
        plantation = Plantation(12)
        plantation.plants = {'nurko': ['bb']}
        plantation.workers = ['nurko', 'nurko2']
        result = plantation.__str__()
        expected_res = f"Plantation size: 12\n"
        expected_res += 'nurko, nurko2\n'
        expected_res += "nurko planted: bb"
        self.assertEqual(expected_res.strip(), result)

    def test_if_repr_method_works(self):
        plantation = Plantation(12)
        plantation.plants = {'nurko': ['bb']}
        plantation.workers = ['nurko', 'nurko2']
        result = plantation.__repr__()
        expected_res = 'Size: 12\n'
        expected_res += 'Workers: nurko, nurko2'
        self.assertEqual(expected_res, result)





if __name__ == 'main':
    main()