print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO CHECK PRIME NUMBERS USING RECURSION")
print()

def is_prime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)

n = int(input("Enter a number: "))

if is_prime(n):
    print(f"{n} is a Prime Number")
else:
    print(f"{n} is Not a Prime Number")
