


""" Python interface to the C++ Person class """
import ctypes
lib = ctypes.cdll.LoadLibrary('./libperson.so')


class Person(object):
	def __init__(self, age):

		# argtypes är vad funktionen tar emot
		# restypes är vad funktionen returnerar
		lib.Person_new.argtypes = [ctypes.c_int]

		lib.Person_fib.argtypes = [ctypes.c_void_p]
		lib.Person_fib.restype = ctypes.c_int

		lib.Person_new.restype = ctypes.c_void_p
		lib.Person_get.argtypes = [ctypes.c_void_p]
		lib.Person_get.restype = ctypes.c_int
		lib.Person_set.argtypes = [ctypes.c_void_p,ctypes.c_int]
		lib.Person_delete.argtypes = [ctypes.c_void_p]
		self.obj = lib.Person_new(age)

	def get(self):
		return lib.Person_get(self.obj)

	# person_a.set(1337)
	def set(self, age):
		lib.Person_set(self.obj, age)


	def __del__(self):
		return lib.Person_delete(self.obj)


	def fib(self):
		return lib.Person_fib(self.obj)


	
	#def fib_py(self):
#		print("Type self:", type(self))
#		print("Type get:", self.get())
		#print("Type set:", self.set(1337))
		#age = lib.Person_get(self.obj)
		#if lib.Person_get(self.obj) <= 1:
		#if age <= 1:
		
		#age = self.get()    #Person_get(self.obj)
		#print("age before set:", age)
		#self.set(1337)
		#print("age after set:", age)
		#print("self.obj:", self.obj)
		#lib.Person_set(self.obj, 2050)
		#print("age_after set 2050", self.get())
		#self.set(420)
		#print("age after 420:", self.get())
		#print("self.obj after", self.obj)
		#print("AGE:", age)


#		if self.get() <= 1:
#			return self.get()
#			#return lib.Person_fib_py(self.obj)
#		else:	
			

			


			#b = Person(self.get()-2)
			#self.set(self.get()-1)
			#return self.fib_py() + b.fib_py()
			#print("Type?", type(self.get()))
			

			#return self.get()


			# vill köra fib_py() med den nya personen. men self.get()-1 är en int och inte en person...
			#return (self.get()-1).fib_py() + (self.get()-2).fib_py()
			



#return (self.set(self.get()-1)).fib_py() + (self.set(self.get()-2)).fib_py()
			#return self.get() #self.set(self.get()-1).fib_py()) + (self.set(self.get() -2).fib_py())


			#self.set(self.get()-1).fib_py() + self.set(self.get()-2).fib_py()
			#a = self.set(age -1)
			#b = self.set(age -2)
			#return a.fib_py() + b.fib_py()
			#a = Person(age -1)
			#b = Person(age -2)
			#return a.fib_py() + b.fib_py()
			#return self.set(age -1).fib_py() + self.set(age -2).fib_py()


			#return self.obj.set(age -1).fib_py() + self.obj.lib.set(age -2).fib_py()
			#return (self.obj.Person_set(lib.Person_get(self.obj) -1)).fib_py() + (self.obj.Person_set(lib.Person_get(self.obj) -2)).fib_py()

			#return lib.Person_set(lib.Person_fib_py(), lib.Person_get(self.obj) -1) + lib.Person_set(lib.Person_fib_py(), lib.Person_get(self.obj) -2) 
			#lib.Person_fib_py(lib.Person_set(self.obj, self.obj -1)) + lib.Person_fib_py(lib.Person_set(self.obj, self.obj -2))


			#a = Person(lib.Person_get(self.obj) -1)
			#b = Person(lib.Person_get(self.obj) -2)
			#return a.fib_py() + b.fib_py()
