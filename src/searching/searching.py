def linear_search(arr, target):
    # Your code here
    for index, value in enumerate(arr):
        if value == target:
            return index


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr)<=0:
        return -1
    found = False
    index = (len(arr)-1)//2
    max_index = len(arr)-1
    min_index = 0
    while not found:
        if arr[index] == target:
            return index
        elif max_index == min_index:
            return -1
        elif target < arr[index]:
            max_index = index
            index = index - (index - min_index)//2
        elif target > arr[index]:
            min_index = index
            index = index + (max_index-index)//2


    return -1  # not found
