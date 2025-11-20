import unittest
from city_functions import city_name

class TestCityFunctions(unittest.TestCase):
    def test_two_args(self):
        self.assertEqual(city_name("Santiago", "Chile"), "Santiago, Chile")

unittest.main()
