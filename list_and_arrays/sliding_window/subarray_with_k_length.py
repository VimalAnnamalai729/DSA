"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.



Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length
"""


def sub_arrays_with_k_distinct(nums, k):
    def at_most_k_distinct(nums, k):
        freq = {}
        left = 0
        count = 0

        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            while len(freq) > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            count += right - left + 1

        return count

    return at_most_k_distinct(nums, k) - at_most_k_distinct(nums, k - 1)


# Example usage:
nums = [1, 2, 1, 2, 3]
k = 2
print(sub_arrays_with_k_distinct(nums, k))  # Output: 7


class MySolution(object):
    def subarrays_with_k_distinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        good_subarrays = []
        print(nums)
        for j in range(2, len(nums)):
            for c, i in enumerate(nums):
                # for i in nums:
                print(f"ind= {c}, val = {i}, j = {j}")
                temp = nums[c:c + j]
                print(temp)
                if len(set(temp)) == k and len(temp) == j:
                    good_subarrays.append(temp)
        return good_subarrays


nums = [1, 2, 1, 2, 3]
k = 2
print(MySolution().subarrays_with_k_distinct(nums, k))