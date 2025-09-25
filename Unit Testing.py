import unittest

def add_numbers(a, b):
    return a + b

class TestFunction(unittest.TestCase):

    def test_addition(self):
        result = add_numbers(4, 6)
        self.assertEqual(result, 10)

if __name__ == "__main__":
    unittest.main()