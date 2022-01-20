# -----------------------------------------------------------
# project euler problem 2
#
# Torjus Nilsen, Kongsberg, Norway
# email tornil1996@hotmail.com
# -----------------------------------------------------------

import numpy as np

'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def next_fibonacci(last_fib, current_fib):

	next_fib = last_fib + current_fib

	return current_fib, next_fib

def get_even_fibsum():

	last_fib = 1
	current_fib = 2
	even_fibonacci_sum = 2

	while(current_fib < 4e+06):
		last_fib, current_fib = next_fibonacci(last_fib, current_fib)

		if current_fib % 2 == 0:
			even_fibonacci_sum = even_fibonacci_sum + current_fib

	return even_fibonacci_sum

even_fibonacci_sum = get_even_fibsum()
print(even_fibonacci_sum)