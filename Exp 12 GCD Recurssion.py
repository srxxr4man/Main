print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO FIND THE GREATEST COMMON DIVISOR OF TWO NUMBERS USING RECURSION")#Title
print()

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

x=int(input("Enter the First Number:"))
y=int(input("Enter the Second Number:"))
result=gcd(x,y)

print(f"The GCD Of {x} and {y} is:",result)
