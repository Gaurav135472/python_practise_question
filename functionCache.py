import functools
import time

@functools.lru_cache(maxsize=None) 
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("Done for 20")
print(fx(10))
print("Done for 10")
print(fx(15))
print("Done for 15")
print(fx(20))
print("Done for 20")
print(fx(10))
print("Done for 10")
print(fx(15))   