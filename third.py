
  
n = int(input("Enter the size of pattern "))
for i in range(n//2):
    print(" " * i + "*" + "  " * (n//2 - 1 - i) + "*")
for i in range(n//2):
    print(" " * (n//2 - 1 - i) + "*" + "  " * i + "*")