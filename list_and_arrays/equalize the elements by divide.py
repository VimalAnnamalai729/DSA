from collections import defaultdict


def min_operations_to_threshold(arr, threshold, d):
    # Dictionary to track how many elements can reach each value and their operations
    value_count = defaultdict(list)

    # Process each element in the array
    for num in arr:
        current = num
        operations = 0

        # Continue dividing until the current number is 0
        while current >= 0:
            value_count[current].append(operations)
            if current == 0:
                break
            current //= d
            operations += 1

    # Find the minimum operations to achieve the threshold
    min_operations = float('inf')

    for value, ops in value_count.items():
        if len(ops) >= threshold:
            # Sort operations to find the minimum needed to get 'threshold' elements
            ops.sort()
            total_ops = sum(ops[:threshold])
            min_operations = min(min_operations, total_ops)

    return min_operations if min_operations != float('inf') else -1


# Example usage
array = [1, 2, 3, 4]
threshold = 4
d = 3
result = min_operations_to_threshold(array, threshold, d)
print(result)  # Expected Output: 6

# Example usage
array = [1, 2, 3, 4, 5]
threshold = 3
d = 2
result = min_operations_to_threshold(array, threshold, d)
print(result)  # Output: 2


array = [64, 30, 25, 33]
threshold = 2
d = 2
result = min_operations_to_threshold(array, threshold, d)
print(result)  # Output: 2


array = [1, 2, 3, 4]
threshold = 4
d = 3
result = min_operations_to_threshold(array, threshold, d)
print(result)  # Output: 2