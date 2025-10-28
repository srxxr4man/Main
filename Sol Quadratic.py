print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO FIND THE SOLUTIONS OF A QUADRATIC EQUATION")
print()

import math as m
import cmath as cm
a=int(input("Enter the coefficient of X^2:"))
b=int(input("Enter the coefficient of X:"))
c=int(input("Enter the Constant:"))
D=(b**2)-(4*a*c)

if D>0:
    print("There are 2 Distinct Real Roots")
    sol1=(-b+m.sqrt(D))/(2*a)
    sol2=(-b-m.sqrt(D))/(2*a)
    print(f"The Solutions Are {sol1} and {sol2}")
elif D==0:
    print("There is Only 1 Distinct Root")
    sol1=(-b)/(2*a)
    print(f"The Solution Is {sol1}")
else:
    print("There are 2 Distinct Complex Roots")
    sol1=(-b+cm.sqrt(D))/(2*a)
    sol2=(-b-cm.sqrt(D))/(2*a)
    print(f"The Solutions Are {sol1} and {sol2}")
