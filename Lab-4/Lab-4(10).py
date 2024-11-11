n=int(input("enter a number"))
rev_num=0
num=n
while num!=0:
    d=num%10
    num=num//10
    rev_num=rev_num*10+d
print(rev_num)
if (rev_num==n):
    print(f"{n} is a pallindrome number")
else:
    print(f"{n} is not a pallindrome number")
