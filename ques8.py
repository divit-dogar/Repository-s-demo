# Write a program to form Pascal Triangle using numbers.
#         1 
#       1   1  
#    1   2   1  
#  1   3   3   1  
# 1   4   6   4   1

# the formula of pascal triangle is =num of rows*(i-j)/(j+1)


def pascal_triangle(n):
    for x in range(n):
        # print spaces
        for y in range (n-x-1): # (5-0-1)
            print(" ", end="")

        # print numbers
        num = 1 

        for y in range (x+1):
            print (num, end=" ")
            num= num*(x-y)//(y+1)
            
        print()

pascal_triangle(5)
