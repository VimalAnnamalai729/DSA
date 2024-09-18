#  Sum the until it gets single digit
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


# Find the index of numbers which sums to get the target

def sum_of_target(numbers, target):
    result = []
    for ind, val in enumerate(numbers):
        remain = target - val
        if remain in numbers[ind + 1:]:
            result.append([ind, numbers.index(remain, ind + 1)])
    return result


print(sum_of_target([4, 5, 8, 5, 3, 6], 10))
print('==================\n')
"""
# 3 Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    result = []
    # if len(nums) < 3:
    #     return []
    # elif len(nums) == 3:
    #     return [nums] if sum(nums) == 0 else []
    nums.sort()
    print(nums)
    i, k = 0, len(nums) - 1
    while i < k:
        print(f'value of i : {i}')
        for j in range(i, len(nums) - 1):
            if j + 1 < k and sum([nums[i], nums[j + 1], nums[k]]) > 0:
                k -= 1
            if j + 1 < k and sum([nums[i], nums[j + 1], nums[k]]) == 0:
                if [nums[i], nums[j + 1], nums[k]] not in result:
                    result.append([nums[i], nums[j + 1], nums[k]])
                # print(result)
        i += 1
    print(result)


three_sum([-1, 0, 1, 2, -1, -4])
# three_sum([0,0,0,0])
# three_sum([3,0,-2,-1,1,2])
# [-4, -1, -1, 0, 1, 2]


# Add without + symbol

def add(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

print(add(8, 8))