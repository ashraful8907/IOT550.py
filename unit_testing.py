import unittest
from add_numbers import add_numbers

class TestFunction(unittest.TestCase):

    def test_addition(self):
        result = add_numbers(4, 6)
        self.assertEqual(result, 12)

if __name__ == "__main__":
    unittest.main()