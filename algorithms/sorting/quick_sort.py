
# using first as a pivot
def partition(l, h, arr):
    pivot = arr[l]
    i = l + 1
    j = h

    while True:
        while i <= j and arr[i] < pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[l], arr[j] = arr[j], arr[l]
    return j


#using second as a pivot
def partiton2(l, h, arr):
    pivot = arr[h]
    i = l 
    j = h - 1
    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[h], arr[i] = arr[i], arr[h]
    return i

#using middle as a pivot
def partition3(low, high, arr):
    mid = low + (high-low) // 2
    pivot = arr[mid]
    i = low
    j = high
    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            
        else:
            
            return j



def quick_sort(l, h, arr):
    if l < h:
        i = partition3(l, h, arr)
        quick_sort(l, i-1, arr)
        quick_sort(i + 1, h, arr)

arr2 = [10, 6, 9, 8, 7, 2, 2, 1, 9]
quick_sort(0, len(arr2) -1, arr2)
print(arr2)







