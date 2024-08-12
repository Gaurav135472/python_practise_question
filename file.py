################## Reading file ###

# f = open('myFile.txt', 'r')
# f = open('myFile.txt') r is default mode and t is default with r
# f = open('myFile.txt', 'rb')

# # print(f)

# txt = f.read()
# print(txt)
# f.close()

############ Write file ###########

# f = open('myFile.txt', 'w')
# f.write("Gaurav Patel")
# f.close()

########### append file ##########

# f = open('myFile.txt', 'a')
# f.write("Gaurav Patel")
# f.close()

########### with use #############

# with open("myFile.txt","a") as f:
#     f.write("Patel Patel")

########## readline method #####

# f = open('myFile.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

######## writelines ###############
# f = open('myFile.txt2', 'w')
# lines = ['line 1\nn', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()

############# seek() #####

# with open('myFile.txt', 'r') as f:
#     print(type(f))

#     f.seek(5) // start reading after 5 letter
#     print(f.tell()) tells the value of seek fun
#     data = f.read(5 ) // how many character wants to read
#     print(data)

############# tryncate ############

# with open('myFile.txt2', 'w') as f:
#     f.write('hello world3!')
#     f.truncate(3)

# with open('myFile.txt', 'r') as f:
#     print(f.read())
    

# with open("poem.txt","r") as f:
#     txt = f.read()
#     listText = txt.split()
#     print(listText)
# index = 0   
# newList = []
# highestWOrd = {}
# Counter = 0
# for j, i in enumerate(listText):
#     if i in newList:
#         pass
#     else:
#         newList.append(i)
#         Counter = listText.count(i)
#         if index < Counter:
#             highestWOrd.clear()
#             highestWOrd.update({i:Counter})
#             index = Counter
#         elif index == Counter:
#             highestWOrd.update({i:Counter})

# print("Bellow display the highest number of elements in the given poem file")

# print(f"{highestWOrd.keys()} ==> {highestWOrd.values()}")

# import csv

# dataList = [["Company Name","PE Ratio", "PB Ratio"],["Reliance","22.23	","2.25"], ["Tata Steel", "4.39", "0.68"]]

# with open("Output.csv", "w",newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(dataList)

