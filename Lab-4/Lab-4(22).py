n=int(input("enter number of rows"))
c=0
for i in range(1,n+1):
    for j in range(1,2*i):
        if (c==0):
            c=1
        else:
            c=0
        print(c,end=' ')
    print()
