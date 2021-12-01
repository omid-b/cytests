#!/usr/env/bin python3
import os
from timeit import timeit
from cytests import funcs
from cytests import _funcs


def print_report(py_time, cy_time):
	if py_time > cy_time:
		print("  Cython is %.2f times faster.\n" %(py_time/cy_time))
	else:
		print("  Python is %.2f times faster\n" %(cy_time/py_time))

def main():
	os.system('clear')
	# TEST 1
	print("Test: hello(); number = 100000")
	py = timeit('funcs.hello()', setup='from cytests import funcs',number=100)
	cy = timeit('_funcs.hello()', setup='from cytests import _funcs',number=100)
	print_report(py,cy)
	# TEST 2
	print("Test: fib(n); n = 1000, number = 10000")
	py = timeit('funcs.fib(1000)', setup='from cytests import funcs',number=100)
	cy = timeit('_funcs.fib(1000)', setup='from cytests import _funcs',number=100)
	print_report(py,cy)
	# TEST 3
	print("Test: calc_pi(niter); niter = 10000, number = 10")
	py = timeit('funcs.calc_pi(10000)', setup='from cytests import funcs',number=100)
	cy = timeit('_funcs.calc_pi(10000)', setup='from cytests import _funcs',number=100)
	print_report(py,cy)
	# TEST 4
	print("Test: nested_sum_2(ni,nj); ni,nj = 100, number = 10")
	py = timeit('funcs.nested_sum_2(100,100)', setup='from cytests import funcs',number=10)
	cy = timeit('_funcs.nested_sum_2(100,100)', setup='from cytests import _funcs',number=10)
	print_report(py,cy)
	# TEST 5
	print("Test: nested_sum_3(ni,nj,nk); ni,nj,nk = 100, number = 10")
	py = timeit('funcs.nested_sum_3(100,100,100)', setup='from cytests import funcs',number=10)
	cy = timeit('_funcs.nested_sum_3(100,100,100)', setup='from cytests import _funcs',number=10)
	print_report(py,cy)
	# TEST 6
	print("Test: numpy_range(lst_numbers); number = 10")
	lst_numbers = [20, 13, 12314, 1 , 324, 12, -22]
	py = timeit(f'funcs.numpy_range({lst_numbers})', setup='from cytests import funcs',number=10)
	cy = timeit(f'_funcs.numpy_range({lst_numbers})', setup='from cytests import _funcs',number=10)
	print_report(py,cy)


	





if __name__ == "__main__":
	exit(main())