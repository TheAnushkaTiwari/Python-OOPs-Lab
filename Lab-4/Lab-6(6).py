num=int(input("enter the number of fibonacci numbers to be printed "))
def fibonacci(n):
    (n1,n2)=(0,1)
    (sum,c)=(0,0)
    while c<=n:
        print(n1,end=' ')
        sum=n1+n2
        (n1,n2)=(n2,sum)
        c=c+1
fibonacci(num)
