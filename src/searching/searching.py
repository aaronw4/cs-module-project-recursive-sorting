# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if len(arr) == 0:
        return -1
    else:
        mid = (start + end) // 2

        if target > arr[mid]:
            return binary_search(arr, target, mid + 1, end)
        elif target < arr[mid]:
            return binary_search(arr, target, start, mid - 1)
        else:
            return mid

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    first = 0
    last = len(arr) - 1
    start = arr[0]
    end = arr[last]
    mid = (first + last) // 2

    if len(arr) == 0:
        return -1
    elif start < end:
        while arr[mid] != target:
            if first + 1 == last:
                return -1
            elif target > arr[mid]:
                first = mid
            elif target < arr[mid]:
                last = mid
            mid = (first + last) // 2
        return mid
    else:
        while arr[mid] != target:
            if first + 1 == last:
                return -1
            if target < arr[mid]:
                first = mid
            elif target > arr[mid]:
                last = mid
            mid = (first + last) // 2
        return mid
            

    # elif start < end:
    #     if target > arr[mid]:
    #         return agnostic_binary_search(arr[mid:], target)
    #     elif target < arr[mid]:
    #         return agnostic_binary_search(arr[:mid], target)
    #     else:
    #         return mid
    # else:
    #     if target > arr[mid]:
    #         return agnostic_binary_search(arr[:mid], target)
    #     elif target < arr[mid]:
    #         return agnostic_binary_search(arr[mid:], target)
    #     else:
    #         return mid
