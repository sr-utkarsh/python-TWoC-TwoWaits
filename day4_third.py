n=int(input("Enter the no. of elements in the dictionary "))
arr=dict()
for i in range (n):
    key=int(input("Enter the key "))
    value=int(input("Enter the value "))
    arr[key]=value
print"The second largest value in the dictionary is ",(list(sorted(arr.values()))[-2])