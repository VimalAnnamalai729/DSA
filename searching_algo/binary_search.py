def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        # mid_val = len(arr) // 2
        mid_val = (left + right) // 2

        if arr[mid_val] == target:
            return mid_val
        elif arr[mid_val] < target:
            left = mid_val + 1
        else:
            right = mid_val - 1
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 3

print(binary_search(arr, target))


def bin_search(arr, target):
    left, right = 0, len(arr) -1

    while left <= right:
        mid_pos = (left + right) // 2

        if arr[mid_pos] == target:
            return mid_pos
        elif arr[mid_pos] < target:
            left = mid_pos + 1
        else:
            right = mid_pos - 1
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 9

print(bin_search(arr, target))



def bin_search2(arr, target):
    left, right = 0, len(arr) -1

    while left <= right:
        mid_pos = (left+right)// 2
        if arr[mid_pos] == target:
            return mid_pos
        elif arr[mid_pos] < target:
            left = mid_pos + 1
        else:
            right = mid_pos - 1
    return -1
