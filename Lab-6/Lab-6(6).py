#compute gcd of two numbers
def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if m%n==0:
        return n
    else:
        return(gcd(n,m%n))
m=int(input("enter  1st number"))
n=int(input("enter  2nd number"))
result=gcd(m,n)
print(f"gcd of {m} and {n} is {result}")
