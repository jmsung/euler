import unittest


from scripts.myfunc import (
    fib, prime_factor, is_prime, primes_below, element_product,
    greatest_product
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

    def test_primes_below(self):
        test_data = [
            (6, [2, 3, 5]),
            (2.1, [2]),
            (2, []),
            (11, [2, 3, 5, 7])
        ]
        for test_input, test_output in test_data:
            self.assertEqual(primes_below(test_input), test_output)

    def test_element_product(self):
        test_data = [
            ([1, -2, 3], -6),
            ([0, 1000, 3], 0),
            ([], None)
        ]
        for test_input, test_output in test_data:
            self.assertEqual(element_product(test_input), test_output)

    def test_greatest_product(self):
        test_data = [
            ([[1, 2, 3, 4, 5], 2], 20),
            ([[3, 2, 4, 5], 5], None),
            ([[-1, 2.5, 3, -4, 5], 2], 7.5),
        ]
        for test_input, test_output in test_data:
            self.assertEqual(greatest_product(*test_input), test_output)
