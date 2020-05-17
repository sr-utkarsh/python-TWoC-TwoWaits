
n=int(input("Enter the size of list: "))
lst=[]
print("Enter the elements: ")
for i in range (n):
    el=int(input())
    lst.append(el)
lst.sort()
print(lst)
k=int(input("Enter the value of k:"))
print("The kth smallest element in the given list is:",lst[k-1])