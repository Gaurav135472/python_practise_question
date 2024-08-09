# def double(x):
#     return x*2

from multiprocessing import Value


def CalculateComplex(fx,y,z):
    return (fx(y+z))


print(CalculateComplex(lambda x:x*2,10,5))