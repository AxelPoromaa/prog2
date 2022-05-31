import random
import math
#import numpy as np
#import functools
import time
import concurrent.futures as future




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
    print(iterations, dimension)
    return inside_space


#n_throws = 20
#n_processes = 4

#process = dimension
#n_processes = 10

# dim 11, it 10000000 time = 116 sekunder

if __name__ == '__main__':
    dimension = 11
    number_of_iterations = 10000000

    n_processes = 10
    dim = n_processes * [dimension]
    itr = [number_of_iterations // n_processes for _ in range (n_processes)]

    with future.ProcessPoolExecutor() as ex:
        tstart = time.perf_counter()
        results = ex.map(volume_hypersphere, dim, itr)
        tstop = time.perf_counter()

    print (f"Measured time : {tstop - tstart} seconds ")
    result = list(results)
    # print("Approximation with dimension '", dimension, "' and number of iterations '", number_of_iterations, "' is:", results) #, number_within_sphere)
    # print("Proof:", (math.pi ** (dimension / 2)) / math.gamma(dimension / 2 + 1)) # floor division '//' because of division with factorial
    # print("Approximate volume:", ((results / number_of_iterations) * (2 ** dimension)))
