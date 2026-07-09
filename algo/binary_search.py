def binary_search(arr, target):
    """Return the index of target in sorted arr, or -1 if not found."""
    low, high = 0, len(arr) - 1
    while low < high:  # BUG: should be low <= high, misses single-element window
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
