num=int(input("enter a number"))
def fibonacci(n):
    l=[]
    (n1,n2)=(0,1)
    (k,s)=(0,0)
    while k<n:
        l.append(s)
        s=n1+n2
        n1=n2
        n2=s
        k=k+1
    return l
print(fibonacci(num))
result=list(map(lambda x: x*x ,fibonacci(num)))
print(result)
