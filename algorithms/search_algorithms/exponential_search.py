from binary_search import binary_search_recursive

def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    i, n = 1, len(arr)

    while i < n and arr[i] <= target:
        i = i * 2

    # i//2 last point where we knew that the value was too small
    # end is either i or the end of the array
    start = i // 2
    end = min(i, n - 1)

    result = binary_search_recursive(arr[start : end + 1], target)
    if result == -1:
        return -1

    return start + result

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40, 50, 60, 70, 80, 90]
    target = 60
    result = exponential_search(arr, target)
    print(f"Element {target} found at index {result}")
