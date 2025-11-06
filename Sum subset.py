import itertools

def sub(num, target):
    subsets = []
    for i in range(len(num) + 1):
        for j in itertools.combinations(num, i):
            if sum(j) == target:
                subsets.append(j)
    return subsets

num = list(map(int,input("Enter the Element WITH SPACES:").split()))
target = int(input("Enter the Target:"))

result = sub(num, target)

if result:
    print("SUBSETS ARE:")
    for _ in result:
        print(_)
else:
    print("NO SUBSET")
