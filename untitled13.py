# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qu5X42A8dHFzCaak6dAn6-WJeMK2gkzu
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

# Function to compute primes
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to compute cumulative sum of primes up to a range
def sum_of_primes_up_to_range(n):
    primes_sum = 0
    primes_sums = []

    for i in range(2, n + 1):
        if is_prime(i):
            primes_sum += i
            primes_sums.append(primes_sum)

    return primes_sums

# Functions for fitting
def linear(x, a, b):
    return a * x + b

def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

def cubic(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

if __name__ == "__main__":
    range_limit = int(input("Enter the range limit for primes: "))

    primes_sums_list = sum_of_primes_up_to_range(range_limit)
    primes_list = list(range(2, len(primes_sums_list) + 2))  # Generating the list of primes for x-axis

    # Fit different functions to the data
    x = np.array(primes_list)
    y = np.array(primes_sums_list)

    popt_linear, _ = curve_fit(linear, x, y)
    popt_quadratic, _ = curve_fit(quadratic, x, y)
    popt_cubic, _ = curve_fit(cubic, x, y)

    # Create plots for fitted functions
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', linestyle='', label='Actual Data')
    plt.plot(x, linear(x, *popt_linear), label='Linear Fit')
    plt.plot(x, quadratic(x, *popt_quadratic), label='Quadratic Fit')
    plt.plot(x, cubic(x, *popt_cubic), label='Cubic Fit')

    plt.title('Cumulative Sum of Primes with Different Curve Fits')
    plt.xlabel('Prime Numbers')
    plt.ylabel('Cumulative Sum of Primes')
    plt.legend()
    plt.grid(True)
    plt.show()