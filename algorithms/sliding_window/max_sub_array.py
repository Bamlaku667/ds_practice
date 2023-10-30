# def max_subarray(arr, k):
#     left = 0
#     right = 0
#     max_sum = 0
#     window_sum = 0

#     while right < len(arr):
#         window_sum += arr[right]
#         if right - left + 1 == k: 
#             max_sum = max(window_sum, max_sum)
#             window_sum -= arr[left]
#             left += 1


#         right += 1

#     return max_sum

# arr = [2, 1, 5, 1, 3, 2]
# k  = 3
# max_sum = max_subarray(arr, k)
# print(max_sum)



def max_sub_array(arr, k):
    left = 0 
    right = 0
    max_sum = 0
    window_sum = 0
    for right in range(len(arr)):
        window_sum += arr[right]
        if right - left + 1 == k:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[left]
            left += 1

        right += 1
    return max_sum

array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = max_sub_array(array, 4)
print(max_sum)