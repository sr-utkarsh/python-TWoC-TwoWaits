n=input("Enter the no.: ")
arr=list(n)

l=len(arr)

x=arr[l-1]

i=l-2

while(arr[i]>x):
    i-=1

if(i==-1):
    print(arr)
    strings = [str(i) for i in arr]
    print(int("".join(strings)))
else:
    
    arr[l-1]=arr[i]
    arr[i]=x
    l1=arr[:i+1]
    
    l2=arr[i+1:]
    
    l2.sort()
    
    strings = [str(i) for i in l1+l2]
    print(int("".join(strings)))
    
    