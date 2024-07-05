# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ha1NbUyWkHtn30RdcEWh-145r76Z0u2W
"""

import random
import matplotlib.pyplot as plt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors_count(num):
    count = 0
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            count += 1
    return count

def generate_numbers_and_plot(num_count):
    numbers = []  # List to store lengths of numbers
    factors = []  # List to store counts of prime factors

    # Generate random numbers and calculate their properties
    for _ in range(num_count):
        num = random.randint(10, 1000)  # Random number between 10 and 1000
        length = len(str(num))
        factors_count = prime_factors_count(num)

        numbers.append(length)
        factors.append(factors_count)

    # Create a scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(numbers, factors, color='blue', alpha=0.7)
    plt.title('Number Length vs. Number of Prime Factors')
    plt.xlabel('Length of Number')
    plt.ylabel('Number of Prime Factors')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    number_count = int(input("Enter the number of random numbers to generate: "))
    generate_numbers_and_plot(number_count)