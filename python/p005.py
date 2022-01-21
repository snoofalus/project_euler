# -----------------------------------------------------------
# project euler problem 5
#
# Torjus Nilsen, Kongsberg, Norway
# email tornil1996@hotmail.com
# -----------------------------------------------------------

import numpy as np

###
# PROBLEM DEFINITION
###

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

###
# IDEAS
###

# BRUTE FORCE WAS TOO SLOW
# 1. Range to 20
# 2. Create a test for evenly divisible
# 3. Iterate bottoms up

# ATTEMPT DIVISOR COMBINATIONS WITH PRIME BASE
# 2520 prime base is [2, 3, 5, 7] 
# prime product = 210
# 2520/210 = 12
# 12 is the first number larger than 10 and divisible by 2, 3

###
# SOLUTION
###


'''
#brute force

one_to_twenty = np.arange(2, 20 + 1)


def check_evenly_divisible(my_number, divisors):

	for divider in divisors:
		if (my_number % divider != 0):
			return False
	return True


def get_smallest_number_divisible(divisors):

	for i in range(1, 100000000):
		is_divisible = check_evenly_divisible(i, divisors)
		if is_divisible:
			return i

#smallest_number = get_smallest_number_divisible(one_to_twenty)
#print(smallest_number)
'''

my_number = 20

def is_prime(candidate_number):

	# largest possible natural cofactor for it not to be prime is 2
	# so only need to check up to half
	for i in range(2, np.ceil(candidate_number / 2).astype('int')+1):
		if (candidate_number % i == 0):
			return False

	return True

def get_primes_until(number):

	prime_numbers = []

	for i in range(2, number + 1):

		prime = is_prime(i)
		if prime:
			prime_numbers.append(i)

	return prime_numbers

def get_prime_base(prime_numbers):
	prime_base = np.prod(prime_numbers)
	return prime_base

def get_first_larger(number):

	while (number % 2 != 0) or (number % 3 != 0):

		number = number + 1

	return number

def get_smallest_number_divisible(number):

	prime_numbers = get_primes_until(number)
	prime_base = get_prime_base(prime_numbers)

	first_larger = get_first_larger(number)

	smallest_number_divisible = prime_base * first_larger

	return smallest_number_divisible

smallest_number_divisible = get_smallest_number_divisible(my_number)
print(smallest_number_divisible)