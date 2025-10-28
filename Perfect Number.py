print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO FIND WHETHER A NUMBER IS PERFECT NUMBER")
print()

n=int(input("Enter the Number:"))
sum=0
for i in range(1,(n//2)+1):
    if n%i==0:
        sum+=i
if n==sum:
    print(f"{n} is a Perfect Number")
else:
    print(f"{n} is NOT a Perfect Number")
