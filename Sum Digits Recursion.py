print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("PRINT SUM OF DIGITS USING RECURSION")
print()

def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

n = int(input("Enter a number:"))
result=sum_digits(n)

print(f"Sum of digits of {n} is {result}")

