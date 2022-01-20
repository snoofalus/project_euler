# -----------------------------------------------------------
# project euler problem 1
#
# Torjus Nilsen, Kongsberg, Norway
# email tornil1996@hotmail.com
# -----------------------------------------------------------

import numpy as np

c, sum_multiples = 1, 0
current_3_multiple, current_5_multiple = 0, 0


while (current_3_multiple < 1000 or current_5_multiple < 1000):

	current_3_multiple = c*3
	current_5_multiple = c*5

	if current_3_multiple < 1000:
		sum_multiples += current_3_multiple
	if current_5_multiple < 1000:
		if current_5_multiple %15 != 0:
			sum_multiples += current_5_multiple
	c += 1
print('sum of 3 and 5 multiples below 1000:\n {}'.format(sum_multiples))



