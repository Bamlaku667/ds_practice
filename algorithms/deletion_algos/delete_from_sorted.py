# we find the element to be deleted using binary search 
# then we will delete by shifting 

#here is the binary search to find the number recursively
def find_num(arr, num):
    low = arr[0]
    high = len(arr) - 1
    mid = low + (high - low) // 2
    if low <= high:
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            return find_num(arr[:mid], num)
        elif arr[mid] < num:
            return find_num(arr[mid+1:])
        
    return -1


def delete_from_sorted(arr, key_to_delete):
    pos_of_key = find_num(arr, key_to_delete)
    if pos_of_key == -1:
        print("not found")
        return 
    
    del arr[pos_of_key]
    print(arr)

arr = [1, 2, 4, 5, 6, 7, 8, 10]
delete_from_sorted(arr, 4)