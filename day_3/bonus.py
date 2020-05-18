 
  
lst=[]  
n1 = int(input("Enter number of elements in list "))
print("Enter the elements of list")
res=1
for i in range(0, n1): 
    ele = int(input())
    lst.append(ele)
    if lst[i] <= res: 
        res = res + lst[i] 
    
     
print(res)
