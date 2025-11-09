print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO CHECK PALINDROME USING RECURSION")
print()

def pali(s):
    if len(s)<=1:
        return True
    elif s[0]!=s[-1]:
        return False
    else:
        return pali(s[1:-1])

s=input("Enter the Text:").upper()

if pali(s):
    print(f"{s} is PALINDROME")
else:
    print(f"{s} is NOT PALINDROME")

