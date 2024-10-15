#count lowercase and uppercase leeter in a string
s=input("enter a string")
lcount=0
ucount=0
for i in s:
    if i.islower():
        lcount=lcount+1
    elif i.isupper():
        ucount=ucount+1
print(f"count of lowercase letters is:{lcount}")
print(f"count of uppercase letters is {ucount}")
