def check_pattern(text, pattern):
    n = len(text)
    m = len(pattern)
    p=[]
    for i in range(n - m + 1):
        substring = text[i:i+m]
        if substring == pattern:
            p.append(i)
    return p


text = input("Enter the Text:").upper()
pattern = input("Enter the Pattern:").upper()

index=check_pattern(text,pattern)

if index!=-1:
    print(f"Pattern At Index Position {index}")
else:
    print("Pattern NOT Found")
