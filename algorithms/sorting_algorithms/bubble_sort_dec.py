def bubble_sort_dec(arr):
    n = len(arr)
    for i in range(n):
        is_sorted = True
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_sorted = False
        if is_sorted:
            break
    return arr