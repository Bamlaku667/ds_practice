def insert_at_any_pos(arr, n, key_to_insert, pos_of_insert):
    if n == pos_of_insert:
        arr.append(key_to_insert)
        return 
    
    arr.append(None) # one additional space creation 

    for i in range(n - 1, pos_of_insert-2, -1):
        arr[i+1] = arr[i]

    arr[i]  = key_to_insert
   

arr = [1, 2, 4, 5, 6]
insert_at_any_pos(arr, len(arr), 89, 5)  # insert at the fifth position of the array (i.e at the 6th index)
print(arr)
