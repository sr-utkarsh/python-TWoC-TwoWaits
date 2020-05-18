n=int(input("Enter the size "))
for i in range (n,0,-1):
    print((str(i) + "*") * (i-1)+ str(i))
for i in range (1,n+1):
    print((str(i) + "*") * (i-1)+ str(i)) 
