# -----------------------------------------------------------
# project euler problem 9
#
# Torjus Nilsen, Kongsberg, Norway
# email tornil1996@hotmail.com
# -----------------------------------------------------------

import numpy as np

###
# PROBLEM DEFINITION
###

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


###
# IDEAS
###

# Resources: 
# https://stackoverflow.com/questions/2817848/find-pythagorean-triplet-for-which-a-b-c-1000
# https://www.mathblog.dk/pythagorean-triplets/

# Euclids theorem states following general properties:
# a = k(p^2 - q^2)
# b = k(2pq)
# c = k(p^2 + q^2)
# p > q > 0

# k(p^2 - q^2) + k(2pq) + k(p^2 + q^2) = 1000
# => 2kp^2 + 2kpq = 1000
# => kp(p + q) = 500
#
# set s = p + q
# kps = 500
#
# From above expression we get that both k, p and s MUST be divisible 
# by 500 to be integer factors. We can extract possible divisors, i.e. p
# and s candidates, try them


###
# SOLUTION
###

pythagorean_sum = 1000

def find_divisors(my_number):

	divisors = []

	# largest possible divisor is number / 2
	for i in range(1, int(my_number) + 1):
		if (my_number % i == 0):
			divisors.append(i)

	return divisors

def solve_pythagorean_triplet(pythagorean_sum):

	factor_product = pythagorean_sum / 2

	lst_divisors = find_divisors(factor_product)

	lst_pythagorean_triplets = []

	for p in lst_divisors:
		for s in lst_divisors:
			if (p < s) and (s < 2*p) and (factor_product % (p*s) == 0):

				lst_current = []
				q = s - p
				k = ((pythagorean_sum / 2) / p ) / s

				lst_current.append(int(k*(p*p - q*q)))
				lst_current.append(int(2*k*p*q))
				lst_current.append(int(k*(p*p + q*q)))
				lst_current.sort()
				lst_current = tuple((lst_current))
				lst_pythagorean_triplets.append(lst_current)

	#remove duplicates from list
	lst_pythagorean_triplets = list(set(lst_pythagorean_triplets))

	return lst_pythagorean_triplets



pythagorean_triplets = solve_pythagorean_triplet(pythagorean_sum)
pythagorean_product = int(np.product(pythagorean_triplets[0]))
print(pythagorean_product)
