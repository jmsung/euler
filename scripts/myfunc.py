import numpy as np


def fib(a, b):
    return a + b


def prime_factor(x):
    """ Return the prime factor of input x """
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
    """ Return whether the input n is primer number or not"""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_below(n):
    """ Return prime numbers below n

    Parameters
    ----------
    n: int
            Input value

    Return
    ------
    primes: list
            List of prime values below n
    """
    n = int(n)

    primes = [2]

    for i in range(3, n, 2):
        # if sum([i % prime == 0 for prime in primes]) > 0:
        #     continue
        if is_prime(i):
            primes.append(i)

    return primes


def findsprimes(n):
    primes = [2]
    for i in range(3, n + 1):
        for j in primes:
            if(j == primes[len(primes) - 1]):
                primes = primes + [i]
            if(i % j == 0):
                break
            else:
                continue
    return primes


def findfactors(n):
    primes = findsprimes(n)
    factors = []
    for i in range(n):
        for j in range(i, n):
            if(i * j == n):
                if(i not in primes):
                    if(j not in primes):
                        factors = findfactors(i) + findfactors(j)
                    else:

                        factors = [j] + findfactors(i)

                else:
                    if(j not in primes):
                        if(i not in primes):
                            factors = findfactors(i) + findfactors(j)
                        else:

                            factors = [i] + findfactors(j)
                    else:
                        factors = [i, j]

                break
    if(n in primes):
        factors = [n]
    return factors


def findsmallest(n):
    primes = findsprimes(n)
    primesnum = [0] * len(primes)
    allzefac = []
    for i in range(n + 1):
        allzefac = allzefac + [findfactors(i)]
    for i in primes:
        for j in allzefac:
            if(j.count(i) > primesnum[primes.index(i)]):
                primesnum[primes.index(i)] = j.count(i)

    summy = 1
    for i in range(len(primes)):
        if primesnum[i] != 0:
            summy = summy * primes[i] ** primesnum[i]
    return summy


def sum_of_squares(n):
    sum = 0
    for i in range(n + 1):
        sum += i**2
    return sum


def square_of_sum(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum**2


def get_product(x):
	"""Return product of all the element in x

    Parameters
    ----------
    x (list): list of int numbers

    Return
    ------
    product (float): the greatest product of size n
	"""
	if not x:
		return None

    product = 1
    for element in x:
        product *= element
    return product

def greatest_product(x, n):
    """Return the greatest product of n consecutive numbers in list x

    Parameters
    ----------
    n (int): size of consecurtive number
    x (list): list of int numbers

    Return
    ------
    greatest (int): the greatest product of size n
    """

    if len(x) < n:
        return None

    # the first product
    greatest = get_product(x[:n])

    # replace if greater
    for i in range(len(y)-n):
        new = get_product(y[i:i+n])
        greatest = new if new > greatest

    return greatest
