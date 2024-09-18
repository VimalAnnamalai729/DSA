def change(cash):
    result = {'two': 0, 'five': 0, 'ten': 0}

    if cash in [1, 3]:
        return None

    result['ten'] = cash // 10
    cash %= 10

    result['five'] = cash // 5
    cash %= 5

    result['two'] = cash // 2
    cash %= 2

    if cash != 0:
        return None

    return result


# Example usage:
print(change(99999))  # Expected Output: {'two': 2, 'five': 0, 'ten': 1}
print(change(11))  # Expected Output: None
