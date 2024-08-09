#Conditonal operator

# >, <, >=, <=, ==, !=

# a = int(input("Enter your age: ")) 

# if(a>18): 
#     print("Your are adult")

# else:
#     print("YOur are not adult")
#     print(("Baby"))
    
# print("Your are done!")

####################### Exercise #######################

# import time

# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)

# # timestampH = int(time.strftime('%H')) 
# # timestampH = int(15)
# timestampH = 11
# timestampM =int( time.strftime('%M'))
# timestampS =int( time.strftime('%S'))

# print(timestampH, timestampM, timestampS)

# if(timestampH <= 12 and timestampH >= 5):
#     print("Good Morning")

# elif (timestampH > 12 and timestampH < 18): 
#     print("Good Afternoon")
# else:
#     print("Good night")

####################### Exercise #######################

# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]

# city = input("Enter the City name ")
# city2 = input("Enter the City2 name ")


# if city in india:
#     if city2 in india:
#         print("City belongs to India")
#     else:
#         print("They dont belong to same country")
# elif city in pakistan:
#      if city2 in pakistan:
#         print("City belongs to palistan")
#      else:
#         print("They dont belong to same country")
# elif city in bangladesh:
#      if city2 in bangladesh:
#         print("City belongs to bangladesh")
#      else:
#         print("They dont belong to same country")   
# else:
#     print("City not belongs to any of above country")

# sugarlevel = int(input("Enter your sugar level"))

# if(sugarlevel <80):
#     print("Sugar is low")
# elif(sugarlevel > 100):
#     print("Sugar level is high")
# else:
#     print("Sugar level in normal")

# city1 = input("Enter city 1: ")
# city2 = input("Enter city 2: ")

# if city1 in india and city2 in india:
#     print("Both cities are in india")
# elif city1 in pakistan and city2 in pakistan:
#     print("Both cities are in pakistan")
# elif city1 in bangladesh and city2 in bangladesh:
#     print("Both cities are in bangladesh")
# else:
#     print("They don't belong to same country")