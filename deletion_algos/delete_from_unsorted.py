# element to be deleted find by linear search 
# delete then shift elements 


#find the number to be deleted using linear search 
def find_num(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
        
    return -1

def delete_from_unsorted(arr, key_to_delete):
    #find the position of the number
    key_index = find_num(arr, key_to_delete)
    if key_index == -1:
        return 
    
    del arr[key_index]

    print(arr)


arr = [5, 1, 4, 3, 2, 6]
delete_from_unsorted(arr, 3)
