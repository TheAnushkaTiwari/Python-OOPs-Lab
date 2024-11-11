num=int(input("enter a number"))
n=num
c=0
sum=0
while(n!=0):
    n=n//10
    c=c+1
n=num
k=0
for i in range(c,0,-1):
    k=n%10
    n=n//10
    sum=k**i+sum
if(sum==num):
    print(f"{num} is disarium number")
else:
    print(f"{num} is not disarium number")
