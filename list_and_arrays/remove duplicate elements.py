#
# def removeDuplicates(nums):
#     uniques_nums = set(nums)
#     j = 0
#     for i in uniques_nums:
#         count = nums.count(i)
#         if count > 2:
#             while count > 2:
#                 nums.remove(i)
#                 nums.append('_')
#                 count -= 1
#         j += count
#     print(nums)
#
#
# removeDuplicates([1,1,1,2,2,3])
# removeDuplicates([0,0,1,1,1,1,2,3,3])

def sol(wood):
    unique_wood = list(set(wood))
    optimal_len = max(wood)
    unique_wood.remove(optimal_len)
    no_of_planks = wood.count(optimal_len)
    used_wood = []
    for ind, val in enumerate(unique_wood):
        if used_wood.count(val) < wood.count(val):
            for j in range(ind+1, len(unique_wood)):
                if optimal_len == val + unique_wood[j]:
                    no_of_planks += 1
                    used_wood.append([val, unique_wood[j]])
    print(no_of_planks)


sol([22, 12, 13, 22,22,22,14, 22, 17, 22])
sol([10, 10, 10, 10, 3, 10, 3, 4, 10])
sol([8, 13, 7, 13, 5, 13, 4, 13, 6, 13])


def remove_duplicates(nums):
    if not nums:
        return 0

    left = 0

    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]

    return left + 1


# Example usage
nums = [1, 2, 2, 3, 4, 4, 1]
new_length = remove_duplicates(nums)
print(nums[:new_length])  # Output: [1, 2, 3, 4]


