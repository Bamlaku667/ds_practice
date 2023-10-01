
# o(n) --> average time complexity
# o(1) --> space complexity

def linear_search(arr, n, key):
    for i in range(n):
        if arr[i] == key:
            return i 
    return -1

