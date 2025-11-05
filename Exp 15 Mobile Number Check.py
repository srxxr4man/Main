print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO CHECK WHETHER THE GIVEN NUMBER IS A MOBILE NUMBER")#Title
print()

def mob(a):
    if a.isdigit and len(a)==10:
        if a[0] in '987':
            return True
        return False
x=input("Enter the Number:")
if mob(x):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
