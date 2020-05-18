lst=[]

n=int(input("Enter the size of the list :"))
print("Enter the elemnts:")
for i in range (0,n):
    ele=input()
    lst.append(ele)
m= lst[n-1] 
lst[n-1] = -1
for i in range(n-2,-1,-1): 
    temp = lst[i]  
    lst[i]=m 
    if m< temp: 
        m=temp
print("The modified list is",lst) 
    
