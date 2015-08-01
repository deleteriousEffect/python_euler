import math


# Takes in a number and solves it for euler problem 3
class Euler3():

    def __init__(self, num):
        self.num = num
        # We only need to check for primes smaller than the square root
        # of the number being factored.
        self.prime_factors = [i for i in range(3, int(math.sqrt(self.num)), 2)
                              if (self.isPrime(i)) and (self.num % i == 0)]
        self.largest_prime_factor = self.prime_factors[-1]

    def isPrime(self, possible_prime):
        if possible_prime % 2 == 0 and possible_prime > 2:
            return False
        for i in range(3, int(math.sqrt(possible_prime)), 2):
            if possible_prime % i == 0:
                return False
        return True
