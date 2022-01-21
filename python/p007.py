# -----------------------------------------------------------
# project euler problem 7
#
# Torjus Nilsen, Kongsberg, Norway
# email tornil1996@hotmail.com
# -----------------------------------------------------------

import numpy as np

###
# PROBLEM DEFINITION
###

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
# see that the 6th prime is 13.
#
# What is the 10 001st prime number?


###
# IDEAS
###

# Consider ways of effectively generating/separating primes:
# - [x] Sieves of Erastothenes, Sundaram
# - [ ] Reuse our previous prime checker (not as efficient)


###
# SOLUTION
###

# ALG: SIEVE OF SUNDARAM
# https://en.wikipedia.org/wiki/Sieve_of_Sundaram
#
# Start with a list of the integers from 1 to n. From this list, remove 
# all numbers of the form i + j + 2ij where: 
# - i, j in N, 1 <= i <= j
# - i + j + 2ij <= n
# The remaining numbers are doubled and incremented by one, giving a 
# list of the odd prime numbers (i.e., all primes except 2) below 2n + 1 

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

	primes = []
	for i in range (1, primes_below + 1):
		if check_list[i]:
			primes.append(2*i + 1)

	return primes

primes = sieve_of_sundaram(150000)
print(len(primes))

#sundaram primes start with 3, i.e. move 1 extra index for 2.
print(primes[10001-2])