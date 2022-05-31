import random
import math
import numpy as np
import functools
import time

#dimension = [1, 1, 1, 1]


# some_list = []
# for x in dimension:
#     point = random.uniform(-1.0, 1.0)
#     some_list.append(point)
# print(some_list)


# def rand_func(dimension):
#     point = lambda a : random.uniform(-1.0, 1.0)
#     #some_list = []
#     some_list = [value for x in dimension for point] #in dimension]
#         # while x > 0:
#         #
#         #     some_list.append(point)
#         #     x -= 1
#     return some_list

# def rand_func(dimension):
#     some_list = []
#     for x in dimension:#some_list = [point for x in dimension #if point = random.uniform(1.0, 1.0) > 0]
#         while x > 0:
#             point = random.uniform(-1.0, 1.0)
#             some_list.append(point)
#             x -= 1
#     return some_list
#
#
# print(rand_func(dimension))
#zip()

# point = np.random.uniform(-1.0, 1.0, dimension)
# print(point)
# print(type(point))
# print(np.linalg.norm(point))

# def xy(a_list):
#     var = 0
#     for x in a_list:
#        var += x ** 2
#     #var = functools.reduce(a_list)
#     # this = lambda x : x ** 2
#     # #for x in a_list:
#     # for x in a_list:
#     #     print(x)
#     #     var += list(map(this, x))
#     # #print(var)
#     return var
#
# def volume_hypersphere(iterations, dimension):
#     inside = 0
#     spear = [[random.uniform(-1.0, 1.0) for i in range(dimension)] for j in range(iterations)]
#
#     #new_list = [value for xy(x) in spear]
#     new_list = []
#     for x in spear:
#         new_list.append(xy(x))   #((functools.reduce(xy(x))))
#     #print(new_list)
#     test_func = lambda x : 1 if x < 1 else 0
#     #map(test_func, new_list)
#     for x in new_list:
#        inside += test_func(x)
#     return inside

# a_list element ska ^ 2 och plusas ihop


# def x_squared(a_list):
#     var = 0
#     # this = lambda x : x ** 2
#     # plus = lambda x : x + y
#     # #for x in a_list:
#     # var = functools.reduce(plus, map(this, a_list))
#     #var = functools.reduce(x ** 2, a_list)
#     #print(type(a_list))
#     #var = map(cube, a_list)
#
#
#     for x in a_list:
#      var += x ** 2
#     return var#list(var)


def squared(point_in_space):
    res = 0
    for y in point_in_space:
        res += y ** 2
    return res

def volume_hypersphere(iterations, dimension):
    inside_space = 0
    space = [[random.uniform(-1.0, 1.0) for i in range(dimension)] for j in range(iterations)]
    norm_list = list(map(squared, space))
    in_space = lambda x : 1 if x < 1 else 0

    for x in norm_list:
      inside_space += in_space(x)
    return inside_space



dimension = 11
number_of_iterations = 10000000

#print(volume_hypersphere(number_of_iterations, dimension))

#for d in dimension:
tstart = time.perf_counter()
#fib(fib_n)
number_within_sphere = volume_hypersphere(number_of_iterations, dimension)
tstop = time.perf_counter()
# dim 11, it 10000000 time = 116 sekunder


print ( f" Measured time : {tstop - tstart} seconds ")
#print(fib_n)
new_stuff = tstop - tstart
print(new_stuff)
#print(1.1618 ** fib_n)



print("Approximation with dimension '", dimension, "' and number of iterations '", number_of_iterations, "' is:", number_within_sphere) #, number_within_sphere)
print("Proof:", (math.pi ** (dimension / 2)) / math.gamma(dimension / 2 + 1)) # floor division '//' because of division with factorial
print("Approximate volume:", ((number_within_sphere / number_of_iterations) * (2 ** dimension)))

# (, 2), (n, d) = (100000, 11)
# Vd(r) = π
#d/2
#Γ(d/2 + 1)r
#d
