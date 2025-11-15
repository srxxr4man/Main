print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO FIND INDEX OF A GIVEN PATTERN")
print()

def check_pattern(text, pattern):
    a = len(text)
    b = len(pattern)
    p=[]
    for i in range(a-b+1):
        substring = text[i:i+b]
        if substring == pattern:
            p.append(i)
    return p


text = input("Enter the Text:").upper()
pattern = input("Enter the Pattern:").upper()

index=check_pattern(text,pattern)

if index:
    print(f"Pattern At Index Position {index}")
else:
    print("Pattern NOT Found")
