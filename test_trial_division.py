import unittest
from my_server import trial_division

class TestTrialDivision(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(trial_division(13), [13])
        self.assertEqual(trial_division(2), [2])
        self.assertEqual(trial_division(17), [17])

    def test_composite(self):
        self.assertEqual(trial_division(12), [1, 2, 2, 3])
        self.assertEqual(trial_division(360), [1, 2, 2, 2, 3, 3, 5])
        self.assertEqual(trial_division(100), [1, 2, 2, 5, 5])

    def test_one(self):
        self.assertEqual(trial_division(1), [1])

    def test_zero(self):
        self.assertEqual(trial_division(0), [0])

    def test_negative(self):
        self.assertEqual(trial_division(-12), [-12])

if __name__ == "__main__":
    unittest.main()
