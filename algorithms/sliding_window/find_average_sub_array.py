def find_averages(arr, k ):
    left = 0
    right = 0
    window_sum = 0
    while right < len(arr):
        window_sum += arr[right]
        if right - left + 1 == k: 
            average = window_sum / k
            yield average
            window_sum -= arr[left]
            left += 1
        right += 1

arr = [1, 3, 5, 7, 9, 2]
k = 3
generator = find_averages(arr, k)

for next in generator:
    print(next)