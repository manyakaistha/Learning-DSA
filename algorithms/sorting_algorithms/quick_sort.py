def partition(arr, start, end):
    idx = start - 1
    pivot = arr[end]
    for i in range(start, end):
        if arr[i] <= pivot:
            idx += 1
            arr[i], arr[idx] = arr[idx], arr[i]
    idx += 1
    arr[end], arr[idx] = arr[idx], arr[end]
    return idx

def quick_sort(arr, start, end):
    if start < end:
        pivot_idx = partition(arr, start, end)
        quick_sort(arr, start, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, end)

arr = [1, 5, 2, 4, 3]
quick_sort(arr, 0, len(arr) - 1)
print(arr)