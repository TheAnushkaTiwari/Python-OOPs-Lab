def factorial(n):
    if (n==0):
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter n value"))
r=int(input("enter r value"))
ans=factorial(n)/(factorial(r)*factorial(n-r))
print(ans)
