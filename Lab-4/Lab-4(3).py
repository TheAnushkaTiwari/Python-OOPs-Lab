for i in range(1,1000):
    num=i
    sum=0
    n=num
    c=0
    while(n!=0):
        c=c+1
        n=n//10
    n=i
    while (n!=0):
        k=n%10
        n=n//10
        sum=sum+k**c
    if(sum==i):
        print(i)
