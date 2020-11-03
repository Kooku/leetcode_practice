class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Link to problem: https://leetcode.com/problems/two-sum/

        Brute force solution is O(n^2)
        Optimal solution is O(n)

        One pass solution where you build the dictionary as you iterate
        and check for the difference in the dictionary
        """
        nums_map = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in nums_map:
                return [nums_map[difference], index]
            else:
                nums_map[num] = index
