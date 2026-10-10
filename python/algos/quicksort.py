arr = [87, 23, 45, 2, 1, 0, 100]

def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    
    smaller_than = [i for i in arr[1:] if i < pivot]
    greater_than = [i for i in arr[1:] if i > pivot]

    return quicksort(smaller_than) + [pivot] + quicksort(greater_than)

sorted = quicksort(arr)
print(sorted)