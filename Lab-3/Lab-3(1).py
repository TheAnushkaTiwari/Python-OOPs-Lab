a=int(input("enter a number"))
j=0
for i in range(1,a+1):
    if a%i==0:
        j=j+1
if j>2:
    print("number is not prime")
else:
    print("number is prime")
