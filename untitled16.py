# -*- coding: utf-8 -*-
"""Untitled16.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WIphQFPn3fAHv900TSv7mW9jmh7eI_WQ
"""

import matplotlib.pyplot as plt
import random

def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

def generate_composite_numbers(limit, count):
    composites = []
    num = 4  # Start with 4 as the first composite number

    while len(composites) < count:
        factors = prime_factors(num)
        if len(factors) > 1:
            composites.append(num)
        num += 1

        if num > limit:
            break

    return composites

def plot_factors_difference(composite_numbers):
    for num in composite_numbers:
        factors = prime_factors(num)
        if len(factors) > 1:
            factors.sort()
            factor_diff = [abs(factors[i] - factors[i+1]) for i in range(len(factors)-1)]
            plt.plot(factor_diff, label=f"Composite {num} Factors")

    plt.xlabel('Index')
    plt.ylabel('Absolute Difference')
    plt.title('Absolute Difference of Factors of Composite Numbers')
    #plt.legend()
    plt.show()

# Generate one million composite numbers
random.seed(42)  # Set seed for reproducibility
composite_numbers = generate_composite_numbers(1000, 1000)

plot_factors_difference(composite_numbers)