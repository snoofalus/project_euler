# -----------------------------------------------------------
# project euler problem 4
#
# Torjus Nilsen, Kongsberg, Norway
# email tornil1996@hotmail.com
# -----------------------------------------------------------

import numpy as np

###
# PROBLEM DEFINITION
###

# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit 
# numbers.


###
# IDEAS
###

# 1. Write a palindrome checker (If even number of digits check outwards
# from middle, else exclude middle number).
# 2. Exclude all non x-digit numbers from iteration
# 3. Iterate top-down


###
# SOLUTION
###

def reverse_string(my_string):
	return my_string[::-1]

def check_if_palindrome(candidate_number):

	str_candidate_number = str(candidate_number)

	#candidate is even
	if (len(str_candidate_number) % 2 == 0):
			
		first_half = str_candidate_number[:len(str_candidate_number) // 2]
		last_half = str_candidate_number[len(str_candidate_number) // 2:]
		
		last_half_reversed = reverse_string(last_half)

		if (first_half == last_half_reversed):
			return True
		else:
			return False

	#candidate is odd
	else:

		first_half = str_candidate_number[:len(str_candidate_number) // 2]
		last_half = str_candidate_number[(len(str_candidate_number) // 2 + 1):]

		last_half_reversed = reverse_string(last_half)

		if (first_half == last_half_reversed):
			return True
		else:
			return False

def list_to_number(my_list):

	#join list of str numbers to one string then convert to int
	my_str = ''.join(my_list)
	my_number = int(my_str)

	return my_number

def get_largest_palindrome(count_product_digits):

	#find largest and lowest possible digit numbers as lists
	largest_digit_list = []
	for i in range(count_product_digits):
		largest_digit_list.append('9')

	lowest_digit_list = ['1']
	for i in range(count_product_digits - 1):
		lowest_digit_list.append('0')
	
	largest_digit_number = list_to_number(largest_digit_list)
	lowest_digit_number = list_to_number(lowest_digit_list)

	#init empty list
	palindromes = []

	#walk downwards from largest product between digits
	for product1 in range(largest_digit_number, (lowest_digit_number - 1), -1):
		for product2 in range(largest_digit_number, (lowest_digit_number - 1), -1):
			candidate_number = product1 * product2
			is_palindrome = check_if_palindrome(candidate_number)

			if is_palindrome:
				palindromes.append(candidate_number)

	largest_palindrome = np.max(palindromes)

	return largest_palindrome

largest_palindrome = get_largest_palindrome(3)
print(largest_palindrome)