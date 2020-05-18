lst1 = [] 
lst2=[]
n1 = int(input("Enter number of elements in list 1 "))
print("Enter the elements of list")
for i in range(0, n1): 
    ele = input() 
  
    lst1.append(ele)
n2 = int(input("Enter number of elements in list 2 "))
print("Enter the elements of list")
for i in range(0, n2): 
    ele2 = input() 
  
    lst2.append(ele2)
lst1=list(set(lst1)& set(lst2))
print(lst1)
