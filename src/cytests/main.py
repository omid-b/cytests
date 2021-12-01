#!/usr/env/bin python3
import os
from timeit import timeit

def print_report(py_time, cy_time):
	if py_time > cy_time:
		print("  Cython is %.2f times faster.\n" %(py_time/cy_time))
	else:
		print("  Python is %.2f times faster\n" %(cy_time/py_time))

def main():
	os.system('clear')
	############################
	# test: Hello from Python/Cython!
	# print("Test: hello(); number = 1")
	# py = timeit('funcs.hello()', setup='from cytests import funcs',number=1)
	# cy = timeit('_funcs.hello()', setup='from cytests import _funcs',number=1)
	# print_report(py,cy)
	print("Test: hello(); number = 100000")
	py = timeit('funcs.hello()', setup='from cytests import funcs',number=100000)
	cy = timeit('_funcs.hello()', setup='from cytests import _funcs',number=100000)
	print_report(py,cy)
	############################
	# test: n's Fibunacci number
	# print("Test: fib(n); n = 90, number = 1")
	# py = timeit('funcs.fib(90)', setup='from cytests import funcs',number=1)
	# cy = timeit('_funcs.fib(90)', setup='from cytests import _funcs',number=1)
	# print_report(py,cy)
	# print("Test: fib(n); n = 90, number = 10000")
	# py = timeit('funcs.fib(90)', setup='from cytests import funcs',number=10000)
	# cy = timeit('_funcs.fib(90)', setup='from cytests import _funcs',number=10000)
	# print_report(py,cy)
	# print("Test: fib(n); n = 1000, number = 1")
	# py = timeit('funcs.fib(1000)', setup='from cytests import funcs',number=1)
	# cy = timeit('_funcs.fib(1000)', setup='from cytests import _funcs',number=1)
	# print_report(py,cy)
	print("Test: fib(n); n = 1000, number = 10000")
	py = timeit('funcs.fib(1000)', setup='from cytests import funcs',number=10000)
	cy = timeit('_funcs.fib(1000)', setup='from cytests import _funcs',number=10000)
	print_report(py,cy)
	#######################
	# print("Test: calc_pi(niter); niter = 1000, number = 1")
	# py = timeit('funcs.calc_pi(1000)', setup='from cytests import funcs',number=1)
	# cy = timeit('_funcs.calc_pi(1000)', setup='from cytests import _funcs',number=1)
	# print_report(py,cy)
	print("Test: calc_pi(niter); niter = 100000, number = 100")
	py = timeit('funcs.calc_pi(100000)', setup='from cytests import funcs',number=100)
	cy = timeit('_funcs.calc_pi(100000)', setup='from cytests import _funcs',number=100)
	print_report(py,cy)


	





if __name__ == "__main__":
	exit(main())