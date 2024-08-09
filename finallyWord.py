def fun1():

    try:
        l = [1,2,3,4]
        i = int(input("Enter the endex"))
        print(l[i])
        return 1
    except:
        print("Some error occures")
        return 0
        
    finally:
        print("I will always executed after the return statemane we cannot print anything but whatever we write inside the finally it will execute")
        
    print("I will always executed")

x = fun1()
print(x)