# maximum sum of a subarray of size k

def max_sum(arr, k):
    if len(arr) < k:
        return -1

    # starting window
    window_sum = sum(arr[:k])

    # first sum available
    max_sum = window_sum

    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
    return max_sum


arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4

max_sum(arr, k)
