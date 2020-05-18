n=int(input("Enter the size of list: "))
lst=[]
print("Enter the elements: ")
for i in range (n):
    el=int(input())
    lst.append(el)
x=sum(lst)
fibo=set()
prev , curr = 0, 1
fibo.add(prev) 
fibo.add(curr) 
while (curr <= x): 
    temp = curr + prev 
    if temp <= x: 
        fibo.add(temp) 
    prev = curr 
    curr = temp
sum = 0
for i in range( n ): 
        if (lst[i] in fibo): 
            sum += lst[i] 
if (sum in fibo): 
    print("Sum of fibonaaci elements is a fibonacci element")
else:
    print("Sum of fibonaaci elements is not a fibonacci element")
