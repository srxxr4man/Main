print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO FIND PADLOCK WITH A GIVEN KEY ( 3 DIGIT COMBINATION )")
print()

def padlock(key):
    for i in range(1000):
        guess=f"{i:03}"
        print(f"Tying Combination {guess}")
        if guess==key:
            print(f"Padlock Opened with {guess}")
            break

n=input("Enter the Key:")
padlock(n)
