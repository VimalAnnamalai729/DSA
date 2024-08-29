def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Finding the middle of the array
    mid = len(arr) // 2

    # Dividing the array elements into 2 halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    # Merging the two halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Collecting the remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Example usage
# arr = [12, 11, 13, 5, 6, 7]
# print("Given array is:", arr)


# sorted_arr = merge_sort(arr)
# print("Sorted array is:", sorted_arr)


def merge_sort1(arr):
    if len(arr) == 1:
        return arr
    mid_pos = len(arr) // 2
    left_array = merge_sort(arr[:mid_pos])
    right_arary = merge_sort(arr[mid_pos:])

    return merge(left_array, right_arary)


def merge1(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    result.append(left[i:])
    result.append(right[j:])

    return result

# Example usage
arr = [12, 11, 13, 5, 6, 7]
print("Given array is:", arr)


sorted_arr = merge_sort(arr)
print("Sorted array is:", sorted_arr)
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self, value):
        self.stack.pop(value)

    def is_empty(self, index):
        if not self.stack:
            return True
        return False

    def peek(self, value):

        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        pass

    def size(self):
        pass