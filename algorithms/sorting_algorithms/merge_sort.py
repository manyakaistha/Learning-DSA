def merge_two_sorted_lists(a, b):
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    arr = []
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr.append(a[i])
            i += 1
        else:
            arr.append(b[j])
            j += 1
    
    while i < len_a:
        arr.append(a[i])
        i += 1
    while j < len_b:
        arr.append(b[j])
        j += 1
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_list = arr[:mid]
    right_list = arr[mid:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return merge_two_sorted_lists(left_list, right_list)

