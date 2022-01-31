import numpy as np


def fib(a, b):
    return a + b


def prime_factor(x):
    """ Return the prime factor of input x

    Parameters
    ----------
    x (int): input natural number > 1

    Return
    ------
    sorted_pf (set): list of prime factor of x """

    if not x:
        raise ValueError("Empty input.")

    if not isinstance(x, int):
        raise ValueError("Input value must be integer.")

    if x < 2:
        return None

    pf = set()
    while x > 1:
        for i in range(2, x + 1):
            if x % i == 0:
                x = int(x / i)
                pf.add(i)
                break
    sorted_pf = sorted(pf)

    return sorted_pf


def is_prime(n):
    """ Return whether the input n is prime number or not

    Parameters
    ----------
    n (int): input number

    Return
    ------
    result (bool): True if prime """

    if not isinstance(n, int) or n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primes_below(n):
    """ Return prime numbers below n

    Parameters
    ----------
    n (int): Input value

    Return
    ------
    primes (list): List of prime numbers below n """

    if n <= 2:
        return []

    n = int(n)
    primes = [2]

    for i in range(3, n, 2):
        if is_prime(i):
            primes.append(i)

    return primes


def element_product(x):
    """ Return the product of all the element in list x

    Parameters
    ----------
    x (list): list of int numbers

    Return
    ------
    product (float): the greatest product of size n """

    if not x:
        return None

    if 0 in x:
        return 0

    product = 1
    for element in x:
        product *= element
    return product


def greatest_product(x, n):
    """ Return the greatest product of n consecutive numbers in list x

    Parameters
    ----------
    x (list): list of numbers
    n (int): size of consecurtive number

    Return
    ------
    greatest (float): the greatest product of size n """

    if len(x) < n:
        return None

    # the first product
    greatest = element_product(x[:n])

    # replace if greater
    for i in range(len(x) - n + 1):
        new = element_product(x[i:i + n])
        if new > greatest:
            greatest = new

    return greatest


def divisors(n):
    """ Return a list of divisors of positive int n

    Parameters
    ----------
    n (int): A number to be divided

    Return
    ------
    divisors (list of int): the divisors """

    if not isinstance(n, int) or n < 1:
        return []

    divisors = set([1, n])

    for i in range(2, int(n / 2)):
        if n % i == 0:
            divisors.add(i)
            divisors.add(int(n / i))

    return list(divisors)
