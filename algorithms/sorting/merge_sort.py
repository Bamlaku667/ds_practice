def merge_sort(arr):
    # since low = hight ----> single element remains
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        merge(arr, left_half, right_half)

def merge(arr, left, right):
    i = j = k = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    for _ in range(i, len(left)):
        arr[k] = left[i]
        k += 1
        i += 1

    for _ in range(j, len(right)):
        arr[k] = right[j]
        k += 1
        j += 1

    

arr = [0, 1, 2]
merge_sort(arr)
print(arr)