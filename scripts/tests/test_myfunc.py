import unittest


from scripts.myfunc import (
    fib, prime_factor, is_prime
)


class TestMyFunc(unittest.TestCase):
    def test_fib(self):
        test_data = [
            ([1, 2], 3),
            ([3, 12], 15),
        ]
        for test_input, test_output in test_data:
            self.assertEqual(fib(*test_input), test_output)

    def test_prime_factor(self):
        test_data = [
            (6, [2, 3]),
            (1, None),
        ]
        for test_input, test_output in test_data:
            self.assertEqual(prime_factor(test_input), test_output)

    def test_is_prime(self):
        test_data = [
            (2, True),
            (31, True),
            (1, False),
            (1.5, False),
            ('test', False)
        ]
        for test_input, test_output in test_data:
            self.assertEqual(is_prime(test_input), test_output)
