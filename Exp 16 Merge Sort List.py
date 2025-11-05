print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO MERGE TWO LIST WITH EVEN AND ODD NUMBER SORTING")#Title
print()

def merge_sort_list(l1,l2):
    l12=l1+l2
    even=[x for x in l12 if x%2==0]
    odd=[x for x in l12 if x%2!=0]
    even.sort()
    odd.sort()
    return even+odd

x=list(map(int,input("Enter the Elements WITH SPACES:").split()))
y=list(map(int,input("Enter the Elements WITH SPACES:").split()))
result=merge_sort_list(x,y)

print("The List Is:",result)
