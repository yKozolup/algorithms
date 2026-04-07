def bin_search(arr : list, key : int) -> bool:
    """
    This function is useful for searching items in sorted array (with binary searchn algorithm).
    :param arr: your sorted array
    :return: True if items found or False if not.
    """
    L = 0
    R = len(arr)-1
    while L<=R:
        mid = (L + R) // 2
        if key == arr[mid]:
            return True
        if key < arr[mid]:
            R = mid - 1
        else:
            L = mid + 1
    if arr[L] == key:
        return True
    else:
        return False


array = [-4, 2, 5, 8, 19, 23, 35, 36, 48, 49, 67, 72, 85, 105, 107]

print(bin_search(array, 5))