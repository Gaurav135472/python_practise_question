# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n* factorial(n-1)
    
# print(factorial(5))


def fibonachiSeries(n):
   
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonachiSeries(n-1) + fibonachiSeries(n-2)
    
print(fibonachiSeries(5))