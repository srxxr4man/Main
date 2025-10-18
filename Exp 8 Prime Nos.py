print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO PRINT ALL THE PRIME NUMBERS LESS THAN A GIVEN NUMBER")#Title
print()

n = int(input("Enter a range:"))
print(f"Prime Numbers less than {n} are:")
# Iterate through numbers from 2 to n-1
for num in range(2, n):
    is_prime = True
# Check divisibility from 2 to sqrt(num)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
# Print the number if prime
    if is_prime:
        print(num,end=" ")
