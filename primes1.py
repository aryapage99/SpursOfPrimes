# -*- coding: utf-8 -*-
"""primes1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aYw91ayDWIF7hkqIE-wji2cbXy5pbEn5
"""

import random
import math
import matplotlib.pyplot as plt

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# atleast two factor which are also primes
def generate_semiprimes(start_number, end_number):
    semiprimes = []
    for i in range(start_number, end_number + 1):
        for j in range(2, int(math.sqrt(i)) + 1):
            if is_prime(i) and is_prime(j) and i * j <= end_number:
                semiprimes.append(i * j)
    return semiprimes

# prime factors of any number
def prime_factors(number):
    factors = []
    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            factors.append(i)
    return factors

def get_number_of_digits(number):
    return len(str(number))

def absolute_difference_factors(factors):
    return abs(factors[0] - factors[1])

def main():
    start_number = int(input("Enter the starting semiprime: "))
    end_number = int(input("Enter the ending semiprime: "))
    semiprimes = generate_semiprimes(start_number, end_number)

    semiprimes.sort()

    # Separate even and odd semiprimes
    even_semiprimes = [semiprime for semiprime in semiprimes if semiprime % 2 == 0]
    odd_semiprimes = [semiprime for semiprime in semiprimes if semiprime % 2 != 0]

    # Generate a dictionary to store semiprime numbers based on their quotient of prime factors
    even_quotients_1 = {}  # quotients: factors[0] / factors[1] for even semiprimes
    even_quotients_2 = {}  # quotients: factors[1] / factors[0] for even semiprimes

    odd_quotients_1 = {}   # quotients: factors[0] / factors[1] for odd semiprimes
    odd_quotients_2 = {}   # quotients: factors[1] / factors[0] for odd semiprimes

    '''
    for each semiprime in even
    '''
    for semiprime in even_semiprimes:
        factors = prime_factors(semiprime)
        quotient_1 = factors[0] / factors[1] if factors[1] != 0 else 0
        quotient_2 = factors[1] / factors[0] if factors[0] != 0 else 0

        if quotient_1 not in even_quotients_1:
            even_quotients_1[quotient_1] = []
        even_quotients_1[quotient_1].append(semiprime)

        if quotient_2 not in even_quotients_2:
            even_quotients_2[quotient_2] = []
        even_quotients_2[quotient_2].append(semiprime)

    for semiprime in odd_semiprimes:
        factors = prime_factors(semiprime)
        quotient_1 = factors[0] / factors[1] if factors[1] != 0 else 0
        quotient_2 = factors[1] / factors[0] if factors[0] != 0 else 0

        if quotient_1 not in odd_quotients_1:
            odd_quotients_1[quotient_1] = []
        odd_quotients_1[quotient_1].append(semiprime)

        if quotient_2 not in odd_quotients_2:
            odd_quotients_2[quotient_2] = []
        odd_quotients_2[quotient_2].append(semiprime)

    # Generate the plot for even semiprimes (factors[1]/factors[0])
    plt.figure()
    for quotient, semiprime_list in even_quotients_2.items():
        plt.plot(semiprime_list, [quotient] * len(semiprime_list), 'bo', label=f"Quotient: {quotient:.2f}")
    plt.xlabel('Even Semiprime Numbers')
    plt.ylabel('Quotient of Prime Factors (factors[1] / factors[0])')
    plt.title('Even Semiprime Numbers vs. Quotient of Prime Factors (factors[1] / factors[0])')
    plt.grid(True)
  #  plt.legend()
    plt.show()

    # Generate the plot for odd semiprimes (factors[0]/factors[1])
    plt.figure()
    for quotient, semiprime_list in odd_quotients_1.items():
        plt.plot(semiprime_list, [quotient] * len(semiprime_list), 'bo', label=f"Quotient: {quotient:.2f}")
    plt.xlabel('Odd Semiprime Numbers')
    plt.ylabel('Quotient of Prime Factors (factors[0] / factors[1])')
    plt.title('Odd Semiprime Numbers vs. Quotient of Prime Factors (factors[0] / factors[1])')
    plt.grid(True)
   # plt.legend()
    plt.show()

    # Generate the plot for all semiprimes (factors[0] / factors[1])
    plt.figure()
    all_quotients = [factors[0] / factors[1] for factors in map(prime_factors, semiprimes)]
    plt.plot(semiprimes, all_quotients, 'go', label="All Semiprimes")
    plt.xlabel('Semiprime Numbers')
    plt.ylabel('Quotient of Prime Factors (factors[0] / factors[1])')
    plt.title('All Semiprimes vs. Quotient of Prime Factors (factors[0] / factors[1])')
    plt.grid(True)
   # plt.legend()
    plt.show()

if __name__ == "__main__":
    main()