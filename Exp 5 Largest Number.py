print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("PROGRAM TO FIND LARGEST OF 3 NUMBERS")#Title
print()
a=float(input("Enter the First Number:"))#Receiving num1 to a
b=float(input("Enter the Second Number:"))#Receiving num2 to b
c=float(input("Enter the Third Number:"))#Receiving num3 to c
print()
if a>b and a>c:
    print(f"The Largest Number among {a},{b},{c} is:",a)
if b>a and b>c:
    print(f"The Largest Number among {a},{b},{c} is:",b)
else:
    print(f"The Largest Number among {a},{b},{c} is:",c)
