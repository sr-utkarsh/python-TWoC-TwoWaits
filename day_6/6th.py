n=int(input("Enter the size of list: "))
lst=[]
print("Enter the elements: ")
for i in range (n):
    el=int(input())
    lst.append(el)
minIndex=lst.index(min(lst))
flag1=1
for i in range(1, minIndex): 
    if lst[i] < lst[i - 1]: 
        flag1 = 0
        break
flag2 = 2
for i in range(minIndex + 1, n) : 
    if lst[i] < lst[i - 1]: 
        flag2 = 0
        break
if (flag1 and flag2 and lst[n - 1] < lst[minIndex - 1]):
         
        print("YES, array is sorted and rotated") 
else: 
    print("NO,array is not sorted and rotateds") 
