def nums_greater_than_t(arr, t):
    right = 0
    window_sum = 0
    count = 0
    while right < len(arr):
        window_sum += arr[right]
        if window_sum >= t:
            count += 1

        right += 1