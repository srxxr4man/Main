print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO CHECK WHETHER LEAP YEAR OR NOT")
print()

y=int(input("Enter the Year:"))
if (y%4==0 and y%100!=0) or y%400==0:
    print(f"{y} is a Leap Year")
else:
    print(f"{y} is NOT a Leap Year")
