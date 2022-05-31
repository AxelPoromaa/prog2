import random
import matplotlib.pyplot as plt
import math
#import numpy as np

n = 1000
n_for_approximation_of_pi = n

inside = []
inside_x = []
inside_y = []

#outside = []
outside_x = []
outside_y = []

while n > 0:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        inside.append(x ** 2 + y ** 2)
        inside_x.append(x)
        inside_y.append(y)
        #print("Inside!")
    else:
        #outside.append(x ** 2 + y ** 2)
        outside_x.append(x)
        outside_y.append(y)
        #outside += 1
        #print("Outside")
    n -= 1

# Assignment 1.
print("\nNumber of dots inside the cirkle:", len(inside))

# Assignment 2.
print("\nApproximation of pi:", 4 *  len(inside)  / n_for_approximation_of_pi)

# Assignment 3.
print("\nMath pi:", math.pi)

# Assignment 4.
plt.title("Monte carlo pi approximation")
plt.scatter(inside_x,  inside_y,  c ='red',  s = 25, label = 'Inside')
plt.scatter(outside_x, outside_y, c ='blue', s = 25, label = 'Outside')
plt.show()
