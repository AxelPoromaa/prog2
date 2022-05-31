

# # Taking list as iterator
# evennum = [2,4,6,8]
# #res = map(cube,evennum)
# #print(list(res))
#
#
# def cube(n):
#     return n**2
#
# def map_cube(a_list):
#     #print(a_list)
#     res = map(cube, a_list)
#     #print(list(res))
#     return list(res)
#
# def something_else(a_list):
#     print(a_list)
#     inside = 0
#     new_list = map_cube(a_list)
#     #print(a_list)
#     #new_list = list(map(cube, a_list))
#     print(new_list)
#     test_func = lambda x : 1 if x < 1 else 0
#     for x in new_list:
#       inside += test_func(x)
#     return inside#inside
#
# print(something_else(evennum))


import functools
lst=[1,-2,3,4]
#this = functools.reduce(lambda x,y : x+y, lst)
this = list(map(lambda x,y : x+y, lst))

print(this)
