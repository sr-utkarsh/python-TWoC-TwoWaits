import math
def prime(n):
    if (n <= 1): 
        return False
    for i in range (2,int(math.sqrt(n))):
        if (n % i == 0): 
            return False
  
    return True

def pallindrome(n):
    sum=0
    rev=n
    while(n>0):
        rem=n%10
        sum=sum*10+rem
        n//=10
    if(sum==rev):
        print(rev, "is a pallindrome no.")

def armstrong(n):
    sum=0
    rev=n
    while(n>0):
        rem=n%10
        sum+=rem**3
        n//=10
    if(sum==rev):
        print(rev, "is an armstrong no.")
    
n=int(input("Enter the no. to be checked"))
if(n%2==0):
    print(n," is a even no.")
else:
    print(n," is a odd no.")
if(prime(n)):
    print(n," is a prime no.")
pallindrome(n)
armstrong(n)
