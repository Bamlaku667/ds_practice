def findIndexofZero(arr) -> int:
    max_index = -1 
    left = 0
    right = 0
    max_len = 0
    count = 0
    prev_zero_index = -1 

    for right in range(len(arr)):
        if arr[right] == 0:
            prev_zero_index = right
            count += 1
        
        if count == 2: 
            while arr[left]: 
                left += 1
            left  += 1
            count = 1

        
        if right - left + 1 > max_len:
            max_len = max(max_len, right - left + 1)
            max_index = prev_zero_index

    return max_index

if __name__ == '__main__':
 
    A = [0, 0, 1, 1, 0, 1, 1, 1, 0, 1]
 
    index = findIndexofZero(A)
    if index != -1:
        print("Index to be replaced is is", index)
    else:
        print("Invalid input")
 

