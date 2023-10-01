#inserting an element in a sorted array

def insert_in_sorted(arr, n , key_to_insert):
    i = n - 1
    arr.append(None)
    while i >= 0 and arr[i] >= key_to_insert:
        arr[i+1] = arr[i]
        i -= 1

    arr[i + 1] = key_to_insert

arr = [1, 2, 4, 5, 6]
insert_in_sorted(arr, len(arr), 3) 