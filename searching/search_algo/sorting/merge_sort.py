# with O(nlogn) time complexity (divide and conququer)
# recursive method



# this is to show how merging is done between two sorted arrays
def merge_two_sorted(arr1, arr2):
    i = 0;
    j = 0;

    arr3 = []
    while i< len(arr1) and j< len(arr2):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+= 1
        
    while i < len(arr1):
        arr3.append(arr1[i])
        i += 1

    while j< len(arr2):
        arr3.append(arr2[j])
        j+= 1

    return arr3

print(merge_two_sorted([2, 8, 15, 18], [5, 9, 12, 17, 19, 25, 30]))


# two way merge sort
# let A = [9, 3, 7, 5, 6, 4, 8, 2]
# assume each value is a list 

def merge(arr):
    
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    if len(arr) > 1:
        merge(left_arr)
        merge(right_arr)
        merge_two_sorted(left_arr, right_ar
    return arr





print(merge([38, 27, 43, 3, 9, 82, 10]
))
