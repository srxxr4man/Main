print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO FIND THE PRODUCT OF TWO NUMBERS USING RECURSION")#Title
print()

def mul(a,b):
    if b==0:
        return 0
    else:
        return a+mul(a,b-1)

x=int(input("Enter the First Number:"))
y=int(input("Enter the Second Number:"))
result=mul(x,y)

print(f"The Product Of {x} and {y} is:",result)
