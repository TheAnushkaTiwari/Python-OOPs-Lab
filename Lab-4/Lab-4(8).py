n=int(input("enter a number"))
rev_num=0
while n!=0:
    d=n%10
    n=n//10
    rev_num=d+rev_num*10
print(rev_num)
