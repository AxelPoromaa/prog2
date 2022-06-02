#!/usr/bin/env python3.9
import time
from numba import njit

@njit
def fib_python(n):
	if n <= 1:
		return n
	else:
		return fib_python(n-1) + fib_python(n -2)


print("hello")
from person import Person

def main():
	n = 10
	t = Person(n)
	tstart = time.perf_counter()
	result = t.fib_py()
	tstop = time.perf_counter()
	print(f"Measured time for c++ : {tstop - tstart} seconds")
	print("C++ fib:", result)
	
	#pythontstart = time.perf_counter()
	#this = fib_python(n)
	#pythontstop = time.perf_counter()
	#print(f"Measured time for python: {pythontstop - pythontstart} seconds")
	#print("python:", this)



	#f = Person(5)
	#print(f.get())
	#f.set(7)
	#print(f.get())
	#this = f.get()
	#fib_result = f.fib_py()
	#print("fib", this, "is equal to:", fib_result)
	#f = Person(0)
	#fib_result = f.fib_py()
	#print("fib", f.get(), "is equal to:", fib_result)
	#f = Person(1)
	#fib_result = f.fib_py()
	#print("fib", f.get(), "is equal to:", fib_result)
	#f = Person(2)
	#fib_result = f.fib_py()
	#print("fib", f.get(), "is equal to:", fib_result)
	#f = Person(3)
	#fib_result = f.fib_py()
	#print("fib", f.get(), "is equal to:", fib_result)
	#f = Person(4)
	#fib_result = f.fib_py()
	#print("fib", f.get(), "is equal to:", fib_result)
	#f = Person(5)
	#fib_result = f.fib_py()
	#print("fib", f.get(), "is equal to:", fib_result)
	#f = Person(6)
	#fib_result = f.fib_py()
	#print("fib", f.get(), "is equal to:", fib_result)
	#f = Person(7)
	#fib_result = f.fib_py()
	#print("fib", f.get(), "is equal to:", fib_result)
	#f = Person(8)
	#fib_result = f.fib_py()
	#print("fib", f.get(), "is equal to:", fib_result)
	#f = Person(9)
	#fib_result = f.fib_py()
	#print("fib", f.get(), "is equal to:", fib_result)
	#f = Person(10)
	#fib_result = f.fib_py()
	#print("fib", f.get(), "is equal to:", fib_result)
	#f = Person(18)
	#fib_result = f.fib_py()
	#print("fib", f.get(), "is equal to:", fib_result)
	#f = Person(47)
	#fib_result = f.fib_py()
	#print("fib", f.get(), "is equal to:", fib_result)
if __name__ == '__main__':
	main()
