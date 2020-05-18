def findElement(arr, n):  
    leftMax = [None] * n  
    leftMax[0] = float('-inf')  
    for i in range(1, n):  
        leftMax[i] = max(leftMax[i-1], arr[i-1])  
    rightMin = float('inf')  
    for i in range(n-1, -1, -1):  
        if leftMax[i] < arr[i] and rightMin > arr[i]:  
            print(arr[i])  
        rightMin = min(rightMin, arr[i])
        
n=int(input("Enter the size of list: "))
A=[]
print("Enter the elements: ")
for i in range (n):
    el=int(input())
    A.append(el)
findElement(A,n)
