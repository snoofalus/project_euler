# -----------------------------------------------------------
# project euler problem 3
#
# Torjus Nilsen, Kongsberg, Norway
# email tornil1996@hotmail.com
# -----------------------------------------------------------

import numpy as np

###
# PROBLEM DEFINITION
###

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
#
# A prime number can be divided, without a remainder, only by itself and 
# by 1. For example, 17 can be divided only by 17 and by 1.


###
# IDEAS
###

# Divide by small numbers to get the larger factors then check them for 
# prime properties.


###
# SOLUTION
###

my_number = 600851475143

def is_prime(candidate_number):

	# largest possible natural cofactor for it not to be prime is 2
	# so only need to check up to half
	for i in range(2, np.ceil(candidate_number / 2).astype('int')+1):
		if (candidate_number % i == 0):
			return False

	return True


def get_largest_primefactor(my_number):

	#start bottoms up dividing by numbers and check their cofactor

	for i in range(2, np.ceil(my_number / 2).astype('int')+1):

		if (my_number % i == 0):

			candidate_number = my_number // i
			prime = is_prime(candidate_number)
			if prime:
				return candidate_number 

largest_primefactor = get_largest_primefactor(my_number)
print(largest_primefactor) #6857
