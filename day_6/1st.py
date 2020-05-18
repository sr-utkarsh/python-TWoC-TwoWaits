from collections import Counter
n=input("Enter the string: ")
lst=list(n)
dic=Counter(lst)
abc=list(dic.values())
abc=[i for i in abc if i%2!=0 ]
total=sum(abc)
maxi=max(abc)
print(total-maxi)
