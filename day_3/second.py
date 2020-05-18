from itertools import permutations  
str1=input("Enter the string ")
 
permutation = [''.join(p) for p in permutations(str1)] 
print("list of permutations are ", str(permutation)) 
