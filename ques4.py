# get an array from the user and sort it with different sorting algorithms.
# selection sort.

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