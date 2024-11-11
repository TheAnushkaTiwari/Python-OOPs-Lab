n=int(input("enter number of rows"))
c='B'
for i in range(1,n+1):
    for j in range(1,2*i):
        if(c=='A'):
            c='B'
        else:
            c='A'
        print(c,end=' ')
    print()
