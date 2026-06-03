# Remove duplicates from an array.

n= int (input("enter the number of elements in the array:"))
arr=[]
for x in range (n):
    num = int (input("enter the elements :"))
    arr.append(num)
    
unique_arr = []
for x in arr:
    if x  not in unique_arr:
        unique_arr.append(x)
print("unique num arr is :",unique_arr)