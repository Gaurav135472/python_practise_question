# marks = [3, 5, 8, "Failure", "new adminition"]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[8])

# print(marks[-3]) # LENGTH OF MARKS + (NEGATIVE INDEX) = 5 + (-3)

# print(marks)
# print(marks[:])
# print(marks[:-1])
# print(marks[1:]) 
# print(marks[1:-1])
# print(marks[1:4:2])
# we can remove the value and add another value in list in one line by useing this 
# marks[1:3]= "Gaurav" it will remove the fist and second index and add the Gaurav name at that place

###############################################

# if "3" in marks:
#     print("No")
# elif 3 in marks:
#     print("Yes")
    
########### STRING ##############

# if "au" in "Gaurav":
#     print("Yes")

################################
    
# lst = [iteam for iteam in range(10)]
# lst2: list[int] = [iteam for iteam in range(10) if iteam%2==0]
# lst3: list[int] = [iteam*iteam for iteam in range(10) if iteam%2==0]
# print(lst)
# print(lst2)
# print(lst3)

# l = [11, 45, 8 , 45, 21, 90, 7, 6]
# print(l)
# l.append(5)
# print(l)
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
# l.reverse()
# print(l)
# print(l.index(11))
# print(l.count(11))


# coping referance and change the main list as well
# m = l
# m[0] = 0
# print(l)

# make the onther the copy adn by chaning m not going to change l
# m= l.copy()
# m[0] = 0
# print(l)

# l.insert(1,888)
# print(l)

# m = [900, 15, 22]
# k = l+m
# print(k)
# k = m+l
# print(k)
# l.extend(m)
# print(l)

# expense = [2200, 2350, 2600, 2130, 2190]

# differenceCost = expense[0] - expense[1]
# print(differenceCost)
# sum =0

# for index, cost in enumerate(expense) :
#     sum = sum + cost
#     if(index == 2):
#         break
# print(sum)

# if 2000 in expense:
#     print("We spend 2000 ")
# else:
#     print("Not spend 2000")

# expense.append(1980)
# print(expense)

# expense[-2] = 1930
# exp[3] = exp[3] - 200
# print(expense)



# heros=['spider man','thor','hulk','iron man','captain america']

# heros.append("black panther")
# print(heros)

# heros.pop()
# heros.insert(2,"black panther")
# print(heros)

# heros.remove("thor","hulk")
# heros.insert(1, "doctor strange")
# print(heros)


# heros[2:3] = ["doctor strange"]
# print(heros)

A = [10,15,20,22]

print(dir(A))

