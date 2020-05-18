 
    
    
n=int(input("Enter the size of list: "))
A=[]
print("Enter the elements: ")
for i in range (n):
    el=float(input())
    A.append(el)
A.sort()
flag=0
for i in range(0,n-2):
    j=i+1
    k=n-1
    
    while (j < k): 
        if( A[i] + A[j] + A[k]>1 and A[i] + A[j] + A[k]<2): 
            print(A[i]," ",A[j]," ",A[k])
            flag=1
            j=k
            
        elif( A[i] + A[j] + A[k]>=2):    
            k-=1  
        else:
            j+=1
            
if(flag==0):
    print("No such triplets")
