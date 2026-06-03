# print this pattern .

#      1
#     212
#    32123
#   4321234
#  543212345

n = int (input("enter the number of rows:"))
for i in range (1, n+1):
    #print spaces
    for y in range (n-i):
        print (" ", end ="") 
    #print  decending number
    for y in range (i, 0, -1):   # range (start, stop, step)
        print (y, end ="")
    #print ascending number
    for y in range (2,i+1):
        print (y , end="")
    print()
    




   
'''
n = 6

for i in range(1, n + 1):

    # Print spaces
    for j in range(n - i):
        print(" ", end="")

    # Print descending numbers
    for j in range(i, 0, -1):
        print(j, end="")

    # Print ascending numbers
    for j in range(2, i + 1):
        print(j, end="")

    print()

    '''