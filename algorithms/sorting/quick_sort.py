def partition(l, h, arr):
    pivot = arr[l]
    i = l
    j = h

    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(l, h, arr):
    if l < h:
        j = partition(l, h, arr)
        quick_sort(l, j, arr)
        quick_sort(j + 1, h, arr)

arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]
quick_sort(0, len(arr) - 1, arr)
print(arr)
