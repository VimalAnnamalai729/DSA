from typing import Tuple


def atoi(string: str) -> bool | tuple[bool, str] | int:
    string = string.strip().split()
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    number = eval(string[0]) if not string[0].isalpha() else False
    if number:
        if INT_MIN < number < INT_MAX:
            return number
        else:
            return number, 'clamped'
    else:
        return 0
    # negative = string[0] == '-'





# Test cases
print(atoi("42"))  # Output: 42
print(atoi("   -42"))  # Output: -42
print(atoi("4193 with words"))  # Output: 4193
print(atoi("words and 987"))  # Output: 0
print(atoi("-91283472332"))  # Output: -2147483648 (clamped)
