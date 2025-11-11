print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO PRINT PASCALS TRIANGLE")
print()

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

n=int(input("Enter the Size:"))

for i in range (n):
    for j in range (n-i+1):
        print(" ",end="")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()
