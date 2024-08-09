# dic = {
#     "Harry" : "Human being",
#     "spoon" : "Object"
# }

# print(dic)
# print(dic["Harry"])
# print(dic.get('Harry'))
# print(dic.keys())
# print(dic.values())

# for key in dic.keys():
#     print(dic[key])

# Define lists of integers and their binadry equivalents
# integer = [0, 1, 2, 3, 4]
# binary = ["0", "1", "10", "11", "100"]

# Pair up each integer with its binary equivalent
# z = zip(integer, binary)

# Create a dictionary from the zipped pairs
# binary_dict = {integer: binary for integer, binary in z}

# Output the resulting dictionary
# print(binary_dict)
# print(z)
# Output: {0: '0', 1: '1', 2: '10', 3: '11', 4: '100'}

# integer = [1, -1, 2, 3, 5, 0, -7]

# additive_inverse = [0-i for i in integer]

# print(additive_inverse)

# integer = [1, -1, 2, -2, 3, -3]
# sq_set = {i*i for i in integer}
# print(sq_set)
    
# dictpp = {"China": 143, "India" : 136, "USA" : 32, "Pakistan": 21}


# opt = input("Enter the option ")

# if opt == "print":
#     for k,v in dictpp.items():
#         print(f"{k} ==> {v}")

# elif opt == "add":
#     addCon = input("Enter the Country name: ") 
#     if addCon in dictpp.keys():
#         print("Already exist")
#     else:
#         population = int(input("Enter the Country population"))
#         dictpp.__setitem__(addCon, population)
#         for k,v in dictpp.items():
#             print(f"{k} ==> {v}")

# elif opt == "remove":
#     remCountry = input("Enter the country name you want to remove ")
#     if remCountry in dictpp.keys():
#         dictpp.pop(remCountry)
#     else:
#         print("Country dosent exist ")
        
#     for k,v in dictpp.items():
#         print(f"{k} ==> {v}")

# elif opt == "query":
#     propleNum = input("Enter the Country name")
#     print(dictpp.get(propleNum))
            
dictapp = {"info":[600,630,620],"ril":[1430,1490,1567], "mtl":[234,180,160]}

userInput = input("Enter the Option ")

if userInput == "print1":
    for k,v in dictapp.items():
        sum = 0
        for valp in v:
            sum = sum + valp
        print(f"{k} ==> {v} ==> {sum/len(v)}")
        
if userInput == "add":
    StockName = input("Enter the stock ticker ")
    if StockName in dictapp.keys():
        print("Add a price to existing stock")
        stockPrice = int(input("Enter the stock Price "))
        listValue = dictapp.get(StockName)
        listValue.append(stockPrice)
        sum = 0
        for k,v in dictapp.items():
            for valp in v:
                sum = sum + valp
            print(f"{k} ==> {v} ==> {sum/len(v)}")
    else:
        stockPrice = int(input("Enter the stock Price ")) 
        stockpriceList= [stockPrice]
        dictapp.__setitem__(StockName,stockpriceList)
        sum = 0
        for k,v in dictapp.items():
            for valp in v:
                sum = sum + valp
            print(f"{k} ==> {v} ==> {sum/len(v)}")
        