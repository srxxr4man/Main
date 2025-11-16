print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO SORT AND MERGE A LIST")
print("PROBLEM SOLVING STRATEGY DIVIDE AND CONQUER")
print()

def merge_sort(l): #Funtion Definition
    if len(l)>1: #Similar To Base Case
        mid=len(l)//2

        #Splitting the List into 2 Halves
        left=l[:mid]
        right=l[mid:]
        merge_sort(left)
        merge_sort(right)

        i=j=k=0 #To move Index Positions

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                l[k]=left[i]
                i+=1
            else:
                l[k]=right[j]
                j+=1
            k+=1

        while i<len(left):
            l[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            l[k]=right[j]
            j+=1
            k+=1

    return l 

l=list(map(int,input("Enter the Elements with SPACES:").split())) # User Input List

print("The Sorted List Is:",merge_sort(l)) #Displaying Sorted List by Calling Function
