# -----------------------------------------------------------
# project euler problem 6
#
# Torjus Nilsen, Kongsberg, Norway
# email tornil1996@hotmail.com
# -----------------------------------------------------------

import numpy as np

###
# PROBLEM DEFINITION
###

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten 
# natural numbers and the square of the sum is
# 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one 
# hundred natural numbers and the square of the sum.

###
# IDEAS
###

# functions for sum of square, square of sums and difference


###
# SOLUTION
###

my_number = 100

def calculate_sum_of_squares(number):

	numbers = np.arange(1, number + 1)

	squares = np.square(numbers)

	sum_of_squares = np.sum(squares)

	return sum_of_squares

def calculate_square_of_sum(number):

	numbers = np.arange(1, number + 1)

	sum_numbers = np.sum(numbers)

	square_of_sums = sum_numbers**2

	return square_of_sums

def find_difference_squares(number):

	square_of_sum = calculate_square_of_sum(my_number)
	sum_of_squares = calculate_sum_of_squares(my_number)

	difference = square_of_sum - sum_of_squares
	pos_difference = np.positive(difference)

	return pos_difference

difference = find_difference_squares(my_number)
print(difference)
