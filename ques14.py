# Draw chrimas tree
height = int(input("Enter the height of the tree: "))
for i in range(height):
    spaces= " " * (height-i-1)
    stars= "*" * (2*i+1)
    print (spaces +stars)

print (" " *(height-1)+"||")
print (" " *(height-1)+"||")
    