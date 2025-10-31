print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO CHECK WHETHER THE GIVEN SIDES ARE OF RIGHT ANGLED TRIANGLE")#Title
print()

def ri_tri(a,b,c):
    hyp=max(a,b,c)
    if hyp==a:
        s1,s2=b,c
    elif hyp==b:
        s1,s2=a,c
    else:
        s1,s2=a,b
    return hyp**2==(s1**2)+(s2**2)


x=float(input("Enter the First Side:"))
y=float(input("Enter the Second Side:"))
z=float(input("Enter the Third Side:"))

if ri_tri(x,y,z):
    print("The Triangle Is A Right Angled Triangle")
else:
    print("The Triangle Is NOT a Right Angled Triangle")
