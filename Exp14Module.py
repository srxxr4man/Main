print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO DEFINE A FUNCTION AND IMPORT IN ANOTHER FILE")#Title
print()

def fib(n):
    fib=[]
    a,b=0,1
    for _ in range(n):
        fib.append(a)
        a,b=b,a+b
    return fib
