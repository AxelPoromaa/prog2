
""" Python interface to the C++ Person class """
import ctypes
#from numba import njit
lib = ctypes.cdll.LoadLibrary('./libperson.so')


class Person(object):
	def __init__(self, age):
		lib.Person_new.argtypes = [ctypes.c_int]

		lib.Person_fib_py.argtypes = [ctypes.c_void_p]
		lib.Person_fib_py.restype = ctypes.c_int

		lib.Person_new.restype = ctypes.c_void_p
		lib.Person_get.argtypes = [ctypes.c_void_p]
		lib.Person_get.restype = ctypes.c_int
		lib.Person_set.argtypes = [ctypes.c_void_p,ctypes.c_int]
		lib.Person_delete.argtypes = [ctypes.c_void_p]
		self.obj = lib.Person_new(age)

	def get(self):
		return lib.Person_get(self.obj)

	def set(self, age):
		lib.Person_set(self.obj, age)

	def __del__(self):
		return lib.Person_delete(self.obj)

	#@njit(nopython=True)
	def fib_py(self):
		if lib.Person_get(self.obj) <= 1:
			return lib.Person_fib_py(self.obj)
		else:
			return lib.Person_set(lib.Person_fib_py(), lib.Person_get(self.obj) -1) + lib.Person_set(lib.Person_fib_py(), lib.Person_get(self.obj) -2) 
#lib.Person_fib_py(lib.Person_set(self.obj, self.obj -1)) + lib.Person_fib_py(lib.Person_set(self.obj, self.obj -2))
			

			#a = Person(lib.Person_get(self.obj) -1)
			#b = Person(lib.Person_get(self.obj) -2)
			#return a.fib_py() + b.fib_py()
