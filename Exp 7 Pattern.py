print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("PROGRAM TO PRINT VARIOUS PATTERNS")#Title
print()

n=int(input("Enter the Size:"))
print("SQUARE PATTERN")
print()
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()
print()


print("RIGHT ANGLED TRIANGLE PATTERN")
print()
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
print()


print("PYRAMID PATTERN")
print()
for i in range(n):
# Print leading spaces
    for j in range(n-i-1):
        print(" ",end=" ")
# Print stars
    for k in range(2 * i + 1):
        print("*",end=" ")
    print()
