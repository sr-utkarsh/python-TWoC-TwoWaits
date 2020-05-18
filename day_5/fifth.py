lst=[]
n=int(input("Enter the size of list: "))
print("Enter the elements of list: ")
for i in range (n):
    ele=int(input())
    if(ele%2!=0):
        ele*=-1
    lst.append(ele)
    
lst.sort()
lst=[i*-1 if i%2!=0  else i for i in lst]
print(lst)
