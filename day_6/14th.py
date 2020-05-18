n = int(input("Enter the value of n "))
List = []
for i in range(n):
    b = []
    print("Enter the elements in row ",i+1)
    for j in range(n):
        b.append(input())
    List.append(b)
print("After rotating 90 degrees clockwise the array will become: ")
for j in range(n):
    for i in range(n - 1, -1, -1):
        print(List[i][j], end = " ")
    print()







