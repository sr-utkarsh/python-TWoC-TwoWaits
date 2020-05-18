
def longestCommonPrefix( a,n): 
    if (n == 0): 
        return "" 
  
    if (n== 1): 
        return a[0] 
    a.sort() 
    end = min(len(a[0]), len(a[n - 1])) 
    i = 0
    while (i < end and 
           a[0][i] == a[n - 1][i]): 
        i += 1
    if(i==0):
        print("No common prefix is found")
    else:
        print("The common prefix is ",a[0][0: i]) 
    
    
n=int(input("Enter the size of list: "))
A=[]
print("Enter the elements: ")
for i in range (n):
    el=input()
    A.append(el)
longestCommonPrefix(A,n)
