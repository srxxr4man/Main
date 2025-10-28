print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO FIND WHETHER A NUMBER IS AMSTRONG")
print()

n=int(input("Enter the Number:"))
l=len(str(n))
sum=0
num=n
while n!=0:
    n1=n%10
    sum+=n1**l
    n=n//10
if num==sum:
    print(f"{num} is an Amstrong Number")
else:
    print(f"{num} is NOT an Amstrong Number")
