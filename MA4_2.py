#!/usr/bin/env python3.9

import time
from numba import njit
from person import Person
from matplotlib import pyplot as plt
import numpy as np
@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return fib_numba(n-1) + fib_numba(n-2)



def fib_python(n):
	if n <= 1:
		return n
	else:
		return fib_python(n-1) + fib_python(n -2)


def main():
	n = 5
	t = Person(n)
	tstart = time.perf_counter()
	result_fib = t.fib()
	tstop = time.perf_counter()
	print(f"Measured time for c++ : {tstop - tstart} seconds")
	print("C++ fib:", result_fib)

	tstart = time.perf_counter()
	result_python_fib = fib_python(n)
	tstop = time.perf_counter()
	print(f"Measured time for python: {tstop - tstart} seconds")
	print("Python fib:", result_python_fib)

	tstart = time.perf_counter()
	result_python_numba_fib = fib_numba(n)
	tstop = time.perf_counter()
	print(f"Measured time for python + numba: {tstop - tstart} seconds")
	print("Python + numba fib", result_python_numba_fib)

	
	#plt.xlabel("n")
	#plt.ylabel("seconds")
	#plt.plot(n, result_fib)
	#plt.show()
	
	x = np.arange(1, 11)
	y = 2 * x + 5
	plt.xlabel("X")
	plt.plot(x, y)
	plt.show()
	

if __name__ == '__main__':
	main()
