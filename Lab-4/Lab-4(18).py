n=int(input("enter number of rows"))
for i in range(n):
    print(" "*i,end=' ')
    print("*"*(2*(n-i)-1),end=' ')
    print()