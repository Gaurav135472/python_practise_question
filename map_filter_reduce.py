######### MAP ###############
# l = [1,2,3,5,4,6]
# newl = []
# def cube(x):
#     return x*x*x
# for i in l:
#     newl.append(cube(i))

# print(newl)

# newl = list(map(cube,l))
# newl = list(map(lambda x: x*x*x,l))

# print(newl)

# ####### Filter #########

# def filter_Function(a):
#     return a >4

# newnewL = list(filter(filter_Function,l))

# print(newnewL) 

######### reduce ##########

from functools import reduce

numbers  = [1,2,3,4,5]

sum = reduce(lambda x,y: x+y, numbers)
print(sum)