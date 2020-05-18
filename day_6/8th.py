def spiralPrint(m, n, a) : 
    k = 0; l = 0
    while (k < m and l < n) : 
        for i in range(l, n) : 
            print(a[k][i], end = " ") 
        k += 1
        for i in range(k, m) : 
            print(a[i][n - 1], end = " ") 
        n -= 1
        if ( k < m) : 
            for i in range(n - 1, (l - 1), -1) : 
                print(a[m - 1][i], end = " ") 
            m -= 1
        if (l < n) : 
            for i in range(m - 1, k - 1, -1) : 
                print(a[i][l], end = " ") 
            l += 1
m=int(input("Enter the no.of rows: "))
n=int(input("Enter the no.of columns: "))
lst=[]
for i in range (m):
    a=[]
    print("Enter the elements in row ",i+1)
    for i in range (n):
        a.append(int(input()))
    lst.append(a)

spiralPrint(m,n,lst)
