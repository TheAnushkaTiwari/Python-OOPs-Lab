n=int(input("enter number of rows"))
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(i,2*i):
        print(k,end=' ')
    for j in range(2 * i - 2, i - 1, -1):
        print(j, end=" ")
    print()
