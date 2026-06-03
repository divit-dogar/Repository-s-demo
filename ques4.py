# get an array from the user and sort it with different sorting algorithms.
# selection sort.
  

# Function to perform selection sort
'''
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
result= selection_sort([12, 11, 13, 5, 6, 7])
print("Sorted array is:", result)

'''

# without function.

'''
n=int(input("Enter the number of elements in the array: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i + 1}"))
    arr.append(element)
    
for i in range(n-1):
    min_index = i
        
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print( arr)
'''

# insertion sort.

'''
n=int (input ("enter the number of elements in the array:"))
arr=[]
 
for x in range(n):
    elements =int(input(f"enter elements  {x+1}"))
    arr.append(elements)

for y in range (1,n):
    key =arr[y]
    z=y-1
    while z>=0 and key < arr[z]:
        arr[z+1]=arr[z]
        z-=1
    arr[z+1]=key
print(arr) 

'''


# bubble sort.

'''
n=int (input ("enter the number of elements in the array:"))
arr=[]

for x in range(n):
    elements =int(input(f"enter elements  {x+1}"))
    arr.append(elements)

for y in range(n):
    for z in range( n-y-1):
        if arr[z] > arr[z+1]:
            arr[z], arr[z+1] = arr[z+1], arr[z]

print(arr)
'''

# quick sort.

def quick_sort(arr):
    if len(arr)<=0:
        return []

    pivot = arr[-1]
    left= []
    right = []
    for i in range(len(arr)-1):
        if arr[i]<pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

result=quick_sort([10, 7, 8, 9, 1, 5])
print(result) 