print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO FIND THE FACTORIAL OF A NUMBER USING RECURSION")#Title
print()

def fact(n):
    if n>-1:
        if n<2:
            return 1
        else:
            return n*fact(n-1)
    else:
        print("No Factorial")
n=int(input("Enter the Number:"))
fact=fact(n)
print(f"Factorial of {n} is:",fact)
