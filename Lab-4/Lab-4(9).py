n=int(input("enter a number"))
sum=0
for i in range(1,n+1):
    if n%i==0:
        sum=sum+i
if (sum-n==n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")
