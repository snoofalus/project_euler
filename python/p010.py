# -----------------------------------------------------------
# project euler problem 10
#
# Torjus Nilsen, Kongsberg, Norway
# email tornil1996@hotmail.com
# -----------------------------------------------------------

import numpy as np

###
# PROBLEM DEFINITION
###

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


###
# IDEAS
###

# Reuse sieve of sundaram to find primes below 2m.
# Sum primes.


###
# SOLUTION
###

upper_limit = int(2e+6)

def sieve_of_sundaram(total_limit):

	#list of primes below 2n + 2
	primes_below = (total_limit - 2) // 2 

	#start with list of True and iteratively remove non primes
	check_list = [True] * (primes_below + 1)

	for i in range(1, primes_below + 1):

		# start from smallest possible j
		j = i
		while (i + j + 2*i*j <= primes_below):
			check_list[i + j + 2*i*j] = False
			j = j + 1

	primes = [2] # sieve only catches primes from 3 and above
	for i in range (1, primes_below + 1):
		if check_list[i]:
			primes.append(2*i + 1)

	return primes

primes = sieve_of_sundaram(upper_limit)

sum_of_primes = np.sum(primes)
print(sum_of_primes)