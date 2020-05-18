n=int(input("size of pattern"))
for i in range(n//2):
    print("*" * (n//2-i)+"  " * i+" " + "*"*(n//2-i))
for i in range(n//2-1,-1,-1):
    print("*" * (n//2-i)+"  " * i+" " + "*"*(n//2-i))