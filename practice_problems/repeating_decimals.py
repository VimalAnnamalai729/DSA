"""
1) numerator & denominator should not be zero
2) Check numerator & denominator sign for negative
3) return immediately if division remainder is zero
"""


def repeating_decimal(numerator: int, denominator: int) -> str:
    if numerator == 0 or denominator == 0:
        return "Both numbers should be greater than zero"

    if numerator % denominator == 0:
        return str(numerator / denominator)

    negative = False
    if numerator * denominator < 0:
        negative = True

    num = abs(numerator)
    den = abs(denominator)

    output = ""
    output += str(num // den)
    # output += "."
    q_presence = []

    while True:
        remainder = num % den
        if remainder == 0:
            for element in q_presence:
                output += str(element[-1])
            break
        new_numerator = remainder * 10
        q = new_numerator / den

        if [new_numerator, q] not in q_presence:
            q_presence.append([new_numerator, q])
        elif [new_numerator, q] in q_presence:
            ind = q_presence.index([new_numerator, q])
            for element in q_presence[:ind]:
                output += str(element[-1])
            output += "("
            for element in q_presence[ind:]:
                output += str(element[-1])
            output += ')'
            break

    print(output)


# repeating_decimal(1, 3)
# repeating_decimal(1, 4)
# repeating_decimal(1, 5)
# repeating_decimal(1, 6)
# repeating_decimal(1, 7)


def repeating_decimal(numerator: int, denominator: int) -> str:
    if denominator == 0:
        return "Undefined"  # Division by zero is not allowed

    # Handling negative numbers
    negative = (numerator < 0) ^ (denominator < 0)

    num = abs(numerator)
    den = abs(denominator)

    # Integral part
    integral_part = num // den
    remainder = num % den

    if remainder == 0:
        return f"{'-' if negative else ''}{integral_part}"  # No decimal part

    output = f"{'-' if negative else ''}{integral_part}."
    remainder_map = {}
    decimal_part = ""

    # Start calculating the decimal part
    idx = 0
    while remainder != 0:
        # If the remainder has been seen before, it's repeating
        if remainder in remainder_map:
            repeat_index = remainder_map[remainder]
            decimal_part = decimal_part[:repeat_index] + "(" + decimal_part[repeat_index:] + ")"
            break

        # Store the index of this remainder
        remainder_map[remainder] = idx

        # Update the remainder
        remainder *= 10
        decimal_digit = remainder // den
        decimal_part += str(decimal_digit)
        remainder %= den
        idx += 1

    return output + decimal_part


# Test cases
print(repeating_decimal(1, 3))  # Expected: "0.(3)"
print(repeating_decimal(1, 6))  # Expected: "0.1(6)"
print(repeating_decimal(22, 7))  # Expected: "3.(142857)"
print(repeating_decimal(1, 2))  # Expected: "0.5"
print(repeating_decimal(0, 1))  # Expected: "0"
print(repeating_decimal(-1, 3))  # Expected: "-0.(3)"
print(repeating_decimal(1, -3))  # Expected: "-0.(3)"
print(repeating_decimal(0, 0))  # Expected: "Undefined"
