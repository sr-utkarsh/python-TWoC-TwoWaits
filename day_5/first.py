n=input()
a=list(n)
z=len(a)
a=['0'  if i=='5' else i for i in a]
x= [str(j) for j in a]
y = "".join(x)

print(y)
