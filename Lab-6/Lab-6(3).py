#take variable length argument in function and cube each ele
def cube_ele(*args):
    cubed=[x**3 for x in args]
    return cubed
result=cube_ele(2,3,4,5)
print("Cube of elements is: ",result)
