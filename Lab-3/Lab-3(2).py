num=input("enter a number")
str_num = str(num)
if str_num == str_num[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
