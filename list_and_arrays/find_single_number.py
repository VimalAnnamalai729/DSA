def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR each number with result
        print(num, result)
    return result




def singleNumber1(nums):
    result = 0
    for num in nums:
        print(f'num : {num}')
        result ^= num  # XOR each number with result
        print(f'result: {result}')
        print('\n')
    return result

print(singleNumber1([4, 1, 2, 1, 2]))

# solution 2

# def singleNumber2(nums):
#     return ((2*sum(set(nums)))-sum(nums))//2
#
#
# print(singleNumber([4, 1, 2, 1, 2]))
# # print(singleNumber2([2,2,3,2]))
# # print(singleNumber2([4, 1, 2, 1, 2]))