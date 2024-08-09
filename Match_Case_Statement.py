a = input("Enter something")

match a: 
    
    case "A":
        print("This is the A")
        
    case "4": 
        print("This is the 4")
        
    case _ if(a == "M"):
        print("Har Har mahadev")
        
    case _:
        print("None match")
        
        