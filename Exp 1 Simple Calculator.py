print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("SIMPLE DESKTOP CALCULATOR")#Title
print()
print("--------LIST OF OPERATIONS--------")# List of Operations that can be performed
print("----------------------------------")
print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")
print("Press 5 for Finding Reminder")
print("----------------------------------")

#Program
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
c=int(input("Enter the choice:"))
if c==1:#Perform Addition
    print(f"The Sum Of {a} and {b} is {a+b}")
    print()
elif c==2:#Perform Subtraction
    print(f"The Difference Of {a} and {b} is {a-b}")
    print()
elif c==3:#Perform Mutiplication
    print(f"The Product Of {a} and {b} is {a*b}")
    print()
elif c==4:#Perform Division
    if b==0:#Checking ZeroDivisionError
        print("Division cannot be performed")
    else:
        print(f"The Quotient Of {a} and {b} is {a/b}")
        print()
elif c==5:#Perform Division and Find Reminder
    if b==0:#Checking ZeroDivisionError
        print("Division cannot be performed")
    else:
        print(f"The Reminder Of {a}/{b} is {a%b}")
        print()
else:
    print("Enter a Valid Choice")
    print()
