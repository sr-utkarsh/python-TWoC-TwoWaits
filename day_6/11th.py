n=int(input("Enter the size of list: "))
A=[]
print("Enter the elements: ")
for i in range (n):
    el=int(input())
    A.append(el)
A.sort()
print("The highest product possible by multiplying 3 elements is: ",A[n-1]*A[n-2]*A[n-3])
