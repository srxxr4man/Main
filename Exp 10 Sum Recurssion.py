print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO FIND THE SUM OF TWO NUMBERS USING RECURSION")#Title
print()

def add(a,b):
    if b==0:
        return a
    else:
        return add(a+1,b-1)

num1=int(input("Enter the First Number:"))
num2=int(input("Enter the Second Number:"))
result=add(num1,num2)

print(f"The Sum Of {num1} and {num2} is:",result)
