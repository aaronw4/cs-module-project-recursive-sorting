# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    # Your code here
    while elements > 0:
        if len(arrA) == 0:
            merged_arr.append(arrB[0])
            arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr.append(arrA[0])
            arrA.pop(0)
        elif arrA[0] > arrB[0]:
            merged_arr.append(arrB[0])
            arrB.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA.pop(0)
        elements -= 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) < 2:
        return arr
    else:
        rest = arr.pop(0)
        return merge([rest], merge_sort(arr))

    

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

