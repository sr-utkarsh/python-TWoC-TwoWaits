def reemovNestings(List): 
    for i in List: 
        if type(i) == list: 
            reemovNestings(i) 
        else: 
            output.append(i) 

size = int(input("Enter the number of sorted lists you want to merge: "))
List= []
for i in range(size):
    List.append(list(map(int,input("Enter the elements seprated by space for sorted list number " + str(i + 1) + ": ").strip().split(" "))))
print(List)
output=[]

reemovNestings(List)
output.sort()
print("The sorted list is: ",output)

