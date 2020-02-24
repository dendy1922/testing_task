import random


def generate_prime_numb(n=500):
    """
    generate random prime number
    """
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return random.choice([i for i in sieve if i])
