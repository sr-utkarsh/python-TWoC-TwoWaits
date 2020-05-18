n=int(input("Enter the size of list: "))
lst=[]
print("Enter the elements: ")
for i in range (n):
    el=int(input())
    lst.append(el)
lst.sort()
i=0
while(i==lst[i]):
    i+=1
    if(i==n):
        break
print(i)


