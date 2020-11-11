class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Link to problem: https://leetcode.com/problems/rotate-array/
        - Given an array, rotate the array to the right by k steps,
          where k is non-negative.
        - Do not return anything, modify nums in-place instead.

        Time complexity: O(n)
        Space complexity: O(n)

        """
        nums_length = len(nums)

        # No need to rotate
        if nums_length == 1:
            return

        # No need to rotate more than the length of an array
        k =  k % nums_length

        temp = nums.copy()
        for i in range(nums_length):
            new_i = i + k
            if new_i >= nums_length:
                new_i = new_i - nums_length
            nums[new_i] = temp[i]


from fractions import gcd
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        In-place Solution

        Time complexity: O(n)
        Space complexity: O(1)

        - Here we shift by `k` amount until a cycle is completed
          (ie. we return to the starting index)
        - There are `gcd(len(nums), k)` cycles to go through
        """
        nums_length = len(nums)

        # No need to rotate
        if nums_length == 1:
            return

        # No need to rotate more than the length of an array
        k =  k % nums_length

        cycles = gcd(nums_length, k)

        for starting_index in range(cycles):
            index = starting_index
            first_loop = True
            temp = nums[index]
            while index != starting_index or first_loop:
                first_loop = False
                next_index = (index + k) % nums_length
                temp, nums[next_index] = nums[next_index], temp
                index = next_index
