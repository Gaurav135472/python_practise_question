##################################  
# usrInput = int(input("Enter the number which list you want in i : i * i format "))

# # list = [i for i in range(usrInput)]

# dictNum = {i : i* i for i in range(usrInput) }

# print(dictNum)

##################################

# listNum  = []
# toupleNum = ()

# while True: 
    
#     userInput = input("Enter the number you want to input")
    
#     if userInput == "quit":
#         break
#     else:
#         listNum.append(userInput)
#         toupleNum = toupleNum + (userInput,)
    
# print(listNum)
# print(toupleNum)
    
##################################

# Write a program that accepts neighbors(set of 2D co-ordinates) and a point(single 2D co-ordinate) and tells nearest neighbor(in terms of euclidean distance)



# import math


# corrdinated_list = [[1,2],[3,4],[5,6],[7,8]]


# result_list = []

# def calculate_Distance(a,b):
    
#     distance = ((a[0] - b[0]) ** 2 ) + ((a[1] - b[1]) ** 2 )
    
#     final_distance = math.sqrt(distance)
    
#     return final_distance

# for i in range(len(corrdinated_list)):
    
#     result =  calculate_Distance([6,5],corrdinated_list[i])
    
#     result_list.append(result)
    
# min_result = min(result_list)

# for i in range(len(result_list)):
#     if min_result == result_list[i]:
#         print(f"The minimum distance from the given point to youlr point is {corrdinated_list[i]} and the distance is {result_list[i]}")
        

# import math

# corrdinated_list = [[1, 2], [3, 4], [5, 6], [7, 8]]

# def calculate_distance(a, b):
#     # Calculate the Euclidean distance between points a and b
#     distance = ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)
#     return math.sqrt(distance)

# # Point to find the nearest neighbor for
# point = [6, 5]

# # Initialize minimum distance as a very large number and the nearest neighbor as None
# min_distance = float('inf')
# nearest_neighbor = None

# for neighbor in corrdinated_list:
#     distance = calculate_distance(point, neighbor)
#     if distance < min_distance:
#         min_distance = distance
#         nearest_neighbor = neighbor

# print(f"The nearest neighbor to the point {point} is {nearest_neighbor} with a distance of {min_distance}")

###################################################

# Write a dummy program that can perform login and registration using a menu driven program

# userDict = {}

# print("Please SignIn or SignUp ")

# userInput1 = input("  ")

# if userInput1.lower() == "signin":
    
#     username_input = input("Enter the username ")
    
#     if username_input in userDict.keys():
        
#         password_input = input("Enter the password ")
        
#         if password_input == userDict[username_input]:
            
#             print(f"{username_input} ==> {password_input}")
#         else:
#             print("Wrong password ")
#     else:
#         print("Usernaem coudent found ")
        
# else:
    
#     username_input = input("Enter the username ")
#     password_input = input("Enter the password ")
#     confirm_password = input("Enter the confirm password ")
    
#     if password_input == confirm_password:
#         userDict.update({username_input:confirm_password})
        
#         print(f"{username_input} ==> {password_input}")
#     else:
#         print("Password didnt math with confirmation password")

#####################################################

# Write a function that accepts a list of strings and performs Bag of words and convert it to numerical vectors.
 # https://en.wikipedia.org/wiki/Bag-of-words_model

# documents = [
#     "the cat sat on the mat",
#     "the dog sat on the log",
#     "the cat chased the dog"
# ]

# def bag_of_words(documents):
    
#     takinise_Doc = [doc.split(" ") for doc in documents]
    
#     vocab = set()
    
#     for doc in takinise_Doc:
#         vocab.update(doc)
    
#     sorted_vocab  = sorted(vocab)
    
#     first_final = takinise_Doc[0]
#     second_Final = first_final + takinise_Doc[1]
#     finalString = second_Final + takinise_Doc[2]  
    
#     final_dict = {}
    
#     Vector_list = [] 
        
#     for i in range(len(sorted_vocab)):
#         counter_num = finalString.count(sorted_vocab[i])
#         print(sorted_vocab[i])
#         print(counter_num)
#         final_dict.update({sorted_vocab[i]: counter_num})
    
#     for i in range(len(takinise_Doc)):
#         for j in range(len(takinise_Doc[i])):
#             if  takinise_Doc[i][j] in final_dict.keys():
#                 storer = takinise_Doc[i][j]
#                 takinise_Doc[i][j] = final_dict[storer]
#     print(takinise_Doc)
#     print(final_dict)
        
# bag_of_words(documents)

