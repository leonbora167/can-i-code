arr = [1, 2, 45,231, 51, 0, 62 , 72]

def find_smallest_element(arr):
    smallest = arr[0] 
    smallest_element_index = 0 
    for i in range(0, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i] 
            smallest_element_index = i  
    return smallest_element_index 

def find_largest_element(arr):
    largest = arr[0] 
    largest_element_index = 0 
    for i in range(0, len(arr)):
        if arr[i] > largest:
            largest_element_index = i 
            largest = arr[i]
    return largest_element_index 

def selection_sort(arr):
    new_list = []
    for i in range(0, len(arr)):
        #smallest_index = find_smallest_element(arr) 
        largest_index = find_largest_element(arr)
        new_list.append(arr.pop(largest_index))

    print("Sorted array is ", new_list)

selection_sort(arr)