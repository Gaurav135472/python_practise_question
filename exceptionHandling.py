from sys import exception


a = input("Enter the number")
print(f"Multiplication table of {a} is")
try:
    for i in range(1,11):
        print(f"{int(a)} * {i} = {int(a)*i}") 
except Exception as e:
    print(e)
    print("Error in code")

print("Some of the line of code")