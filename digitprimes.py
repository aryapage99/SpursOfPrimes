# -*- coding: utf-8 -*-
"""digitprimes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CgoaIku2ZySI5HGb-TCA-3buvPk8Lhje
"""

# Importing libraries
import math
import matplotlib.pyplot as plt

# Defining a function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Defining a function to find the prime factors of a number
def prime_factors(n):
    factors = []
    # Dividing by 2 until n is odd
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    # Dividing by odd numbers from 3 to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    # If n is still greater than 2, it is a prime factor
    if n > 2:
        factors.append(n)
    return factors

# Defining a function to compute the smaller ratio of prime factors of a semiprime number
def smaller_ratio(semiprime):
    # A semiprime number has exactly two prime factors
    factors = prime_factors(semiprime)
    if len(factors) != 2:
        return None
    # The smaller ratio is the smaller factor divided by the larger factor
    smaller_factor = min(factors)
    larger_factor = max(factors)
    ratio = smaller_factor / larger_factor
    return ratio

# Defining a range of semiprime numbers from 10 to 10000
semiprimes = [n for n in range(10, 1000000) if len(prime_factors(n)) == 2]

# Computing the smaller ratio of prime factors for each semiprime number
ratios = [smaller_ratio(n) for n in semiprimes]

# Mapping the ratio to the number of digits the semiprime number has
digits = [len(str(n)) for n in semiprimes]

# Plotting the ratios and digits as a scatter graph
plt.scatter(digits, ratios, color='blue', marker='.')
plt.xlabel('Number of digits')
plt.ylabel('Smaller ratio of prime factors')
plt.title('Smaller ratio of prime factors vs number of digits for semiprime numbers')
plt.show()