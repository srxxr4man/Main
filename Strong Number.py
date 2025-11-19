print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO CHECK WHETHER A GIVEN NUMBER IS A STRONG NUMBER")
print()

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

n=int(input("Enter the Number:"))
sum=0
num=n

while n!=0:
    n1=n%10
    sum+=fact(n1)
    n=n//10

if num==sum:
    print("STRONG NUMBER")
else:
    print("NOT A STRONG NUMBER")
