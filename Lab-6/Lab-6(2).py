def sum_of_list_eles(list1):
  sum=0
  for i in list1:
    sum=sum+i
  return sum
l=[1,2,3,4,5]
result=sum_of_list_eles(l)
print("Sum of elements of the list is ",result)
