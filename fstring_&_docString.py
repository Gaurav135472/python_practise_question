#############################fString

# from os import name


# letter = "My name is {} and I am from {}"
# country = "India"
# Name= "Gaurav"

# print(letter.format(Name,country))
# print(f"hey My name is {Name} and I am from {country}")

# price = 49.22222
# txt = f"Hy price is {price:.2f}"
# print(txt)

#########DocString

def square(n):
    '''Takes in a number n, return the square of n'''
    print(n**2)
    
square(5)
print(square.__doc__)