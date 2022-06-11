# Task 4.1 wage script
"""
import sys
n, hour, wage, prem = sys.argv
print (f'total wage: {int(hour) * int(wage) + int(prem)}$')

#Task 4.2 transform some list
x = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([y for y in x if y > x [x.index(y) - 1]])


# Task 4.3 multiple of 20, 21
print([y for y in range(20, 240) if (y % 20 == 0) or (y % 21 == 0)])


# Task 4.4 without repeted number
x = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([i for i in x if x.count(i) == 1])


# Task 4.5 multiply even number in 100 to 1000
import functools
even_numbers = [even_number for even_number in range(100,1001,2)]
def mult_func(prev_el, el):
	return prev_el*el
print(functools.reduce(mult_func, even_numbers))


# Task 4.6 some scripts
from sys import argv 
import itertools
name, start_numb, cycle_var= argv
start_numb = int(start_numb)
for i in itertools.count(start_numb):
	print(i)
	if i > start_numb + 15:
		break
count = 0
for i in itertools.cycle(cycle_var):
	if count < 7:
		print(i)
		count += 1
	else:
		break

# Task 4.7 
from math import factorial
def gen_fact(n):
	for el in range(1, n + 1):
		yield factorial(el)
for el in gen_fact(6) :
	print(el)
"""






