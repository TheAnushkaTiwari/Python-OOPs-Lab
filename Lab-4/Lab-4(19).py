n = 6

triangle = [[1] * (i + 1) for i in range(n)]

for i in range(2, n):
    for j in range(1, i):
        triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

for i in range(n):

    print(" " * 2 *(n-i+1) , end="")
    
    for j in range(i + 1):
        print(f" {triangle[i][j]}", end=" ")
        
    print()
