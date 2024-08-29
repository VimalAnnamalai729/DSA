def sum_of_digits(digit):
    s_digit = str(digit)
    # Approach 1
    # if len(s_digit) > 1:
    #     sum_of_digits(sum([int(i) for i in s_digit]))
    # else:
    #     print(digit)

    # Approach 2
    while len(s_digit) > 1:
        s_digit = str(sum([int(i) for i in s_digit]))

    print(s_digit)


sum_of_digits(16)
sum_of_digits(942)
sum_of_digits(132189)
sum_of_digits(493193)

print('==================\n')
# Counting Duplicates With Counter

from collections import Counter


def count_input(data, target):
    s = Counter(data)

    print(s.total(target))


# find the index of numbers which sums to get the target

def sum_of_target(numbers, target):
    result = []
    for ind, val in enumerate(numbers):
        remain = target - val
        if remain in numbers[ind + 1:]:
            result.append([ind, numbers.index(remain, ind + 1)])
    return result


print(sum_of_target([4, 5, 8, 5, 3, 6], 10))

from datetime import timedelta


def convert_seconds_into_time(seconds):
    str(timedelta(seconds=359999))


# Brute Force Approach
def convert_seconds_into_time_logic(seconds):
    if seconds > 359999:
        return 'Time Seconds Exceeds The Range'

    hour = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 3600) % 60

    print(f'{hour}:{minutes}:{seconds}')


convert_seconds_into_time_logic(seconds=3600)


def sum_of_equal_sides(num):
    for i, n in enumerate(num[1:]):
        if sum(num[0:i + 1]) == sum(num[i:]):
            return i
    return -1


print(sum_of_equal_sides([20, 10, -80, 10, 10, 15, 35]))
print(sum_of_equal_sides([1, 2, 3, 8, 3, 2, 1]))
print(sum_of_equal_sides([1, 100, 50, -51, 1, 1]))
