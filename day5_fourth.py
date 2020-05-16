values=[]
weight=[]
n=int(input("Enter the no. of items: "))
print("Enter the values of the items:")
for i in range (n):
    ele=int(input())
    values.append(ele)
print("Enter the weight of the items:")
for i in range (n):
    ele=int(input())
    weight.append(ele)
w=int(input("Enter the capacity of the knapsack: "))
t = [[-1 for i in range(w+1)] for j in range(n+1)] 
  
  
def knapsack(weight, values, w, n):     
    if n == 0 or w == 0: 
        return 0
    if t[n][w] != -1: 
        return t[n][w]  
    if weight[n-1] <= w: 
        t[n][w] = max(values[n-1] + knapsack(weight, values, w-weight[n-1], 
                                          n-1), knapsack(weight, values, w, n-1)) 
        return t[n][w] 
    elif weight[n-1] > w: 
        t[n][w] = knapsack(weight, values, w, n-1) 
        return t[n][w] 
  
print(knapsack(weight, values, w, n-1))
