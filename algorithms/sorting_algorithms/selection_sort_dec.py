def selection_sort_dec(arr):
    n = len(arr)
    for i in range (n):
        max_mindex = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr