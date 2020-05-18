
lst = [] 
n = int(input("Enter number of elements : ")) 
  
print("Enter the elements of list")
for i in range(0, n): 
    ele = input() 
  
    lst.append(ele)
lst=list(dict.fromkeys(lst))
print(lst)