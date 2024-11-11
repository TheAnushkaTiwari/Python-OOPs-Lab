a=int(input("enter a number"))
n=a
sum=0
c=0
while(n!=0):
    n=n//10
    c=c+1
n=a
for i in range(0,c):
    k=n%10
    n=n//10
    sum=sum+k
if(a%sum==0):
    print(f"{a} is harshad number ")
else:    
    print(f"{a} is not harshad number")
