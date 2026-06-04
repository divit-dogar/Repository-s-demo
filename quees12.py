# magic square validation

matrix = [[8, 1, 6], 
         [3, 5, 7],
         [4, 9, 2]
        ]
n= len(matrix)

magic_sum= sum(matrix[0])
# check rows.
for row in matrix:
    if sum(row) != magic_sum:
        print ("Not a magic square")
        break

#check columns

for col in range(n):
    col_sum=0
    for row in range(n):
        col_sum += matrix[row][col]

    if col_sum != magic_sum:
        print ("Not a magic square")
        break

    diag1_sum =0
    diag2_sum =0
    
    for row in range(n):
        diag1_sum += matrix[row][row]
        diag2_sum += matrix[row][n-row-1]
    

    if (diag1_sum==magic_sum and diag2_sum== magic_sum):
        print ("It is a magic square")
    else:
        print ("Not a magic square")