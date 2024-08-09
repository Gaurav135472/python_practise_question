# def calculateAddition(a=5,b=3):
#     add = (a+b)
#     print(add)


# def isGreater(a,b):
#     if(a>b):
#         print(a," is grater")
        
#     else:
#         print(b, "is greater")
        
# def isLesser(a,b):
#     pass
        
# def averageNum(*numbers):
#     sum=0
#     for i in numbers:
#         sum = sum + i
#     print ("average is" , sum / len(numbers))
    
# a=9
# b=8

# isGreater(a,b)
# calculateAddition(a,b)
# calculateAddition()
# averageNum(1,2,3,4)

# def calculate_area(base,hight,shape):
#     if shape == "rectangle":
#         area=hight*base
#     elif shape == "tringle":
#         area = (1/2)*base*hight
#     print(area)
    
# calculate_area(12,3,"rectangle")

def print_pattern(number):
    for i in range(1,number+1):
        print(i * ("*"))

print_pattern(18)